Got it! Here is the entire README in one single `.md` file content for you to save as `README.md`:

```markdown
# Darshan-e-Sanskriti

**Darshan-e-Sanskriti** is a Streamlit-based AI-powered travel assistant that helps users explore Indian cultural heritage. It leverages large language models (LLMs) like Gemini to generate personalized travel itineraries and present cultural insights in an interactive, user-friendly web interface.

---

## 🌐 Live Demo

Access the live app here: [darshan-e-sanskriti.streamlit.app](https://darshan-e-sanskriti.streamlit.app)


## 🚀 Features

- AI-powered personalized travel planning  
- Integration with Google Gemini generative AI  
- Modular agentic design for extensibility  
- Real-time data fetching and processing  
- Simple, intuitive Streamlit UI  
- Easy deployment on Streamlit Cloud

---

## ⚙️ Local Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Satyam-Mishra-1/darshan-e-sanskriti.git
cd darshan-e-sanskriti
````

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
# Add other variables as needed
```

5. **Run the app**

```bash
streamlit run app.py
```

---

## ☁️ Deploying on Streamlit Cloud

1. Push your repo to GitHub.

2. In Streamlit Cloud, create a new app pointing to:

* Your GitHub repo
* Branch: `main`
* Main file: `app.py`

3. Add the required environment variables in **Manage App → Settings → Secrets**:

```
GOOGLE_API_KEY = "your-google-api-key"
MODEL_NAME = "gemini-pro"
```

These will be securely injected as environment variables.

---

## 🔐 Required Environment Variables

| Variable Name    | Description                                     |
| ---------------- | ----------------------------------------------- |
| `GOOGLE_API_KEY` | API key for Google Gemini or generative AI      |
| `MODEL_NAME`     | Name of the LLM model to use (e.g., gemini-pro) |

Make sure these are set both locally in `.env` and in Streamlit Cloud Secrets.

---

## 📦 requirements.txt

Your `requirements.txt` should include:

```
taskflowai
python-dotenv
streamlit
ipykernel
from_root
google-generativeai
```

**Note:**
Remove `-e .` unless you have a `setup.py` or `pyproject.toml` file, as Streamlit Cloud expects your project to be a proper Python package if using `-e .`.

---

## 🛠 Troubleshooting

* **ModuleNotFoundError:** Verify that all your source code files (`src.agentic.agents.travel_agent` etc.) are correctly committed to the repo and the import paths are correct.

* **Missing environment variables error:** Ensure `.env` exists locally and all required variables are added to Streamlit Secrets.

* **`ERROR: ... does not appear to be a Python project`:**
  Remove `-e .` from `requirements.txt` if you don't have `setup.py` or `pyproject.toml`.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

* [Streamlit](https://streamlit.io)
* [Google Gemini API](https://ai.google.dev/)
* [TaskflowAI](https://pypi.org/project/taskflowai/)
