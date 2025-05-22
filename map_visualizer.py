import streamlit as st
import pydeck as pdk
from geopy.geocoders import Nominatim
import time

def show_trip_map(origin, visits, destination):
    geolocator = Nominatim(user_agent="trip_planner")
    locations = []
    all_places = [origin] + visits + [destination] if destination else [origin] + visits

    for place in all_places:
        loc = geolocator.geocode(place, timeout=10)
        if loc:
            locations.append({"name": place, "lat": loc.latitude, "lon": loc.longitude})
            time.sleep(1)  # To respect Nominatim API rate limits

    if not locations:
        st.warning("Could not find any valid locations to show on map.")
        return

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/streets-v11",
        initial_view_state=pdk.ViewState(
            latitude=locations[0]["lat"],
            longitude=locations[0]["lon"],
            zoom=4,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=locations,
                get_position='[lon, lat]',
                get_color='[255, 136, 0, 160]',
                get_radius=10000,
                pickable=True
            ),
            pdk.Layer(
                "PathLayer",
                data=[{
                    "path": [[loc["lon"], loc["lat"]] for loc in locations],
                    "name": "route"
                }],
                get_color=[0, 100, 255],
                width_scale=20,
                width_min_pixels=2,
                get_width=5,
            )
        ],
        tooltip={"text": "{name}"}
    ))
