import streamlit as st
import pandas as pd
import json
import altair as alt
import re
import requests
from src.agentic.tools.serper_search import SerperSearch
from src.agentic.agents.travel_agent import TravelAgent 
from map_visualizer import show_trip_map
from cultural_analysis import show_cultural_analysis

from PIL import Image
import requests
from io import BytesIO

def show_classic_header():
    try:
        st.markdown(
        """
        <div style='text-align: center;'>
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA9ziPtpCZbzQCLVYcb9OFDucnC4uUXGNAdQ&s" />
        </div>
        """,
        unsafe_allow_html=True
        )

    except Exception as e:
        st.warning("Couldn't load the header image.")



st.set_page_config(layout="wide", page_title="Travel Explorer")

def all_fields_filled(origin, visits, destination, trip_type, budget, travel_dates):
    return all([origin, visits, destination, trip_type, budget, travel_dates])

def main():
    
    show_classic_header()


    if 'view' not in st.session_state:
        st.session_state.view = "Analyze India's Cultural Tool"
    st.session_state.view = st.radio("Navigation", ["Show Attractions","Show Trip Map", "Analyze India's Cultural Tool"], horizontal=True)

    origin = visits = destination = trip_type = budget = travel_dates = None

    if st.session_state.view in ["Show Trip Map", "Show Attractions" , "Analyze India's Cultural Tool",]:
        with st.sidebar:
            st.markdown(
        """
        <h2 style='
            font-family: "Georgia", serif;
            color: #5D4037;  /* classic brown */
            text-align: center;
            font-weight: bold;
            margin-top: -20px;
            margin-bottom: 10px;
            text-shadow: 1px 1px 2px #C6A664; /* subtle gold shadow */
        '>Darshan-e-Sanskriti</h2>
        """, unsafe_allow_html=True
    )
            origin = st.text_input("Where do you want to start?")
            places_input = st.text_area("🗺️ Enter all the places you want to visit (comma-separated):")
            visits = [place.strip() for place in places_input.split(",") if place.strip()]
            destination = st.text_input("Where do you want to visit first?")
            trip_type = st.selectbox("Type of trip", ["Vacation", "Business", "Adventure", "Cultural"], index=0)
            budget = st.slider("Budget (in INR)", min_value=1000, max_value=500000, value=50000, step=1000)
            travel_dates = st.date_input("Travel dates", [])

    # Cultural Analysis
    if st.session_state.view == "Analyze India's Cultural Tool":
        show_cultural_analysis()
        return

    # --- Button Logic ---
    form_complete = all_fields_filled(origin, visits, destination, trip_type, budget, travel_dates)

    if st.session_state.view == "Show Trip Map":
        st.subheader("🗺️ View Trip Map")
        btn_clicked = st.button("Show Trip Map", disabled=not form_complete)

        if not form_complete:
            st.warning("Please complete all fields in the sidebar to enable the map.")

        if btn_clicked:
            show_trip_map(origin, visits, destination)

    elif st.session_state.view == "Show Attractions":
        st.subheader("🏰 View Attractions and Travel Details")
        btn_clicked = st.button("Show Attractions", disabled=not form_complete)

        if not form_complete:
            st.warning("Please complete all fields in the sidebar to see attractions.")

        if btn_clicked:
            st.success(f"Exploring {destination} for a {trip_type.lower()} trip on a budget of ₹{budget:,}.")
            agent = TravelAgent()

            st.header("🏰 Attractions")

            def search_google_images(query, max_results=3):
                try:
                    image_results = SerperSearch.search_images(query, max_results=max_results)
                    return [img['url'] for img in image_results[:max_results]]
                except Exception as e:
                    st.error(f"Error fetching images for '{query}': {e}")
                    return []

            def is_image_accessible(url):
                try:
                    response = requests.head(url, timeout=5)
                    return response.status_code == 200 and "image" in response.headers.get("Content-Type", "")
                except:
                    return False

            with st.spinner("Finding top attractions..."):
                attractions_raw = agent.research_attractions(destination)

            def extract_json_block(text):
                for pattern in [r"```json(.*?)```", r"```(.*?)```", r"(\[\s*\{.*?\}\s*\])"]:
                    match = re.search(pattern, text, re.DOTALL)
                    if match:
                        return match.group(1).strip()
                return None

            attractions_list = []
            try:
                json_string = extract_json_block(attractions_raw)
                if not json_string:
                    raise ValueError("No JSON block found.")
                attractions_list = json.loads(json_string)
            except Exception as e:
                st.error("❌ Failed to parse JSON from model response.")
                st.text(attractions_raw)

            if isinstance(attractions_list, list) and len(attractions_list) > 0:
                st.markdown("## Top Attractions")
                for idx, att in enumerate(attractions_list, start=1):
                    title = att.get("title", f"Attraction {idx}")
                    description = att.get("description", "No description available.")
                    image_url = att.get("image")

                    if not image_url or not is_image_accessible(image_url):
                        image_urls = search_google_images(title)
                    else:
                        image_urls = [image_url]

                    st.markdown(f"### {idx}. {title}")
                    st.markdown(description)
                    for img_url in image_urls:
                        st.image(img_url, use_container_width=True)
            else:
                st.warning("⚠️ No attraction data available.")

            # --- Weather ---
            st.header("🌦️ Weather")
            st.markdown(f"## {destination} Travel Guide: {travel_dates[0]} - {travel_dates[-1]}")
            with st.spinner("Fetching weather forecast..."):
                weather_report = agent.research_weather(destination, str(travel_dates))

            if isinstance(weather_report, str):
                weather_report = re.sub(r"^```(?:json)?\s*", "", weather_report.strip())
                weather_report = re.sub(r"\s*```$", "", weather_report)
                try:
                    weather_report = json.loads(weather_report)
                except Exception:
                    weather_report = {}

            weather_data = weather_report.get("forecast", [])
            recommendations = weather_report.get("recommendations", "")

            if weather_data:
                df_weather = pd.DataFrame(weather_data)
                high_bar = alt.Chart(df_weather).mark_bar(color="#b68b42").encode(x='date:N', y='high:Q')
                low_bar = alt.Chart(df_weather).mark_bar(color="#2b2d42", opacity=0.5).encode(x='date:N', y='low:Q')
                st.altair_chart(alt.layer(high_bar, low_bar), use_container_width=True)
                st.dataframe(df_weather[['date', 'high', 'low', 'weather_type', 'description']])

                for day in weather_data:
                    st.markdown(
                        f"📅 **{day['date']}** | 🌡️ High: {day['high']}°C | Low: {day['low']}°C  \n"
                        f"📝 {day['description']}"
                    )
                st.markdown("### Travel Recommendations")
                st.info(recommendations)
            else:
                st.warning("No weather data available.")

            # --- Flights ---
            import ast
            st.header("✈️ Flights")
            with st.spinner("Searching for flights..."):
                flight_report = agent.search_flights(origin, destination, str(travel_dates), budget)
                st.markdown(flight_report)

            if isinstance(flight_report, str):
                try:
                    flight_report = json.loads(flight_report)
                except:
                    try:
                        flight_report = ast.literal_eval(flight_report)
                    except:
                        flight_report = []

            if isinstance(flight_report, list) and flight_report:
                df_flights = pd.DataFrame(flight_report)
                for col in ['departure', 'arrival']:
                    df_flights[col] = pd.to_datetime(df_flights[col], errors='coerce').dt.strftime('%b %d, %Y %H:%M')

                st.subheader("📋 Available Flights")
                st.table(df_flights[['airline', 'departure', 'arrival', 'duration', 'price']])

                flights_chart = alt.Chart(df_flights).mark_bar().encode(
                    y=alt.Y('airline:N', sort='-x'),
                    x=alt.X('price:Q'),
                    color=alt.condition(
                        alt.datum.price <= budget,
                        alt.value("#b68b42"),
                        alt.value("#d9534f")
                    )
                )
                st.altair_chart(flights_chart, use_container_width=True)
                
                
            st.header("📋 Summary")
            with st.spinner("Summarizing your trip..."):
                summary = agent.summarize_trip(destination, trip_type, budget, str(travel_dates))
            st.success(summary)

if __name__ == "__main__":
    main()
