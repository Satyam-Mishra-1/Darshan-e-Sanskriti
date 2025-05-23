# Darshan-e-Sanskriti

**Darshan-e-Sanskriti** is a Streamlit-based AI-powered travel assistant that helps users explore Indian cultural heritage. It leverages large language models (LLMs) like Gemini to generate personalized travel itineraries and present cultural insights in an interactive, user-friendly web interface.

---

## 🌐 Live Demo

👉 [Launch Live App](https://darshan-e-sanskriti-rdehpyno22fhefwaddtv9z.streamlit.app/)

---

## 📸 Screenshots

<div align="center">

<img src="images/image1.png" alt="Home Screen" width="300"/>  
<br/><br/>

| Image 1 | Image 2 | Image 3 | Image 4 |
|--------|--------|--------|--------|
| ![Image 1](images/image1.png) | ![Image 2](images/image2.png) | ![Image 3](images/image3.png) | ![Image 4](images/image4.png) |

| Image 5 | Image 6 | Image 7 | Image 8 |
|--------|--------|--------|--------|
| ![Image 5](images/image5.png) | ![Image 6](images/image6.png) | ![Image 7](images/image7.png) | ![Image 8](images/image8.png) |

| Image 9 | Image 10 | Image 11 | Image 12 |
|--------|---------|----------|----------|
| ![Image 9](images/image9.png) | ![Image 10](images/image10.png) | ![Image 11](images/image11.png) | ![Image 12](images/image12.png) |

| Image 13 | Image 14 | Image 15 | Image 16 |
|---------|---------|----------|----------|
| ![Image 13](images/image13.png) | ![Image 14](images/image14.png) | ![Image 15](images/image15.png) | ![Image 16](images/image16.png) |

</div>

---

## 🚀 Features

- ✅ AI-powered personalized travel planning  
- 🤖 Integration with Google Gemini generative AI  
- 🧠 Modular agentic design for extensibility  
- ⚡ Real-time data fetching and processing  
- 🖥️ Simple, intuitive Streamlit UI  
- ☁️ Easy deployment on Streamlit Cloud  

---

## ⚙️ Local Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Satyam-Mishra-1/darshan-e-sanskriti.git
   cd darshan-e-sanskriti
   ```

2. **Create and activate a Python virtual environment**

   ```bash
   python -m venv myenv
   # Windows:
   myenv\Scripts\activate
   # macOS/Linux:
   source myenv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory**

   Add your environment variables here:

   ```env
   GOOGLE_API_KEY=your-google-api-key
   MODEL_NAME=gemini-pro
   ```

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deploying on Streamlit Cloud

1. Push your repo to GitHub.

2. In Streamlit Cloud, create a new app pointing to:

   - Your GitHub repo
   - Branch: `main`
   - Main file: `app.py`

3. Add environment variables in **Manage App → Settings → Secrets**:

   ```
   GOOGLE_API_KEY = your-google-api-key
   MODEL_NAME = gemini-pro
   ```

---

## 🔐 Required Environment Variables

| Variable Name    | Description                                     |
|------------------|-------------------------------------------------|
| `GOOGLE_API_KEY` | API key for Google Gemini or generative AI      |
| `MODEL_NAME`     | Name of the LLM model to use (e.g., gemini-pro) |

---

## 📦 `requirements.txt`

```txt
taskflowai
python-dotenv
streamlit
ipykernel
from_root
google-generativeai
```

**Note:**  
Remove `-e .` unless you have a `setup.py` or `pyproject.toml`.

---

## 🛠 Troubleshooting

- **ModuleNotFoundError:** Ensure all source files (e.g., `src/agentic/agents/travel_agent.py`) are included and import paths are valid.
- **Missing environment variables:** Ensure `.env` is present locally and variables are added to Streamlit Cloud Secrets.
- **Project error on deployment:** Remove `-e .` from `requirements.txt` unless packaging your app.

---

## 📜 License

Licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io)
- [Google Gemini API](https://ai.google.dev/)
- [TaskflowAI](https://pypi.org/project/taskflowai/)
