# import streamlit as st
# import os
# from pathlib import Path
# import streamlit.components.v1 as components

# def show_cultural_analysis():
#     # Full paths
#     # notebook_path = r"D:\Desktop\Project-Pratice\Darshan-e-Sanskriti\src\India Tourism Analysis.ipynb"
#     # html_output_path = Path("D:/Desktop/Project-Pratice/Darshan-e-Sanskriti/src/india_analysis_rendered.html")
#     from pathlib import Path

#     notebook_path = Path("src/India Tourism Analysis.ipynb")
#     html_output_path = Path("src/india_analysis_rendered.html")


#     # Convert only if file doesn't exist
#     if not html_output_path.exists():
#         st.info("⚙️ Converting notebook to HTML...")

#         # Note: --output-dir sets where the file is written
#         os.system(
#             f"jupyter nbconvert --to html \"{notebook_path}\" --output \"{html_output_path.stem}\" --output-dir \"{html_output_path.parent}\" --no-input"
#         )

#     # Display if generated
#     if html_output_path.exists():
#         with open(html_output_path, "r", encoding="utf-8") as f:
#             notebook_html = f.read()
#         st.subheader("📊 India's Cultural Analysis")
#         components.html(notebook_html, height=900, scrolling=True)
#     else:
#         st.error("❌ Still couldn't find the rendered HTML file. Please check the notebook path and Jupyter installation.")













import streamlit as st
import os
from pathlib import Path
import streamlit.components.v1 as components

def show_cultural_analysis():
    # Define notebook and HTML output paths relative to the project directory
    notebook_path = Path("src/India Tourism Analysis.ipynb")
    html_output_path = Path("src/india_analysis_rendered.html")

    # Convert notebook to HTML if not already converted
    if not html_output_path.exists():
        st.info("⚙️ Converting notebook to HTML...")

        # Run nbconvert to export notebook as HTML
        conversion_cmd = (
            f"jupyter nbconvert --to html \"{notebook_path}\" "
            f"--output \"{html_output_path.stem}\" "
            f"--output-dir \"{html_output_path.parent}\" "
            f"--no-input"
        )

        conversion_result = os.system(conversion_cmd)

        if conversion_result != 0:
            st.error("❌ Jupyter conversion failed. Make sure Jupyter is installed and the path is valid.")
            return

    # Render the converted HTML if available
    if html_output_path.exists():
        with open(html_output_path, "r", encoding="utf-8") as f:
            notebook_html = f.read()
        st.subheader("📊 India's Cultural Analysis")
        components.html(notebook_html, height=900, scrolling=True)
    else:
        st.error("❌ Could not find the rendered HTML file. Please check the notebook path and conversion process.")
