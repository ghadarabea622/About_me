import streamlit as st
from PIL import Image
from pathlib import Path
import requests


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"
resume_file = current_dir / "assets" / "Resume.pdf"

page_title = "Digital CV | Ghada Rabea"
page_icon = ":wave:"
name = "Ghada Rabea"
description = """
Freelancer | AI Engineer | Data Scientist | Machine Learning Engineer 
"""
email = "grabea160@gmail.com"
social_media = {
    "LinkedIn": "https://www.linkedin.com/in/ghada-rabea-97a236277?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
    "WhatsApp": "https://api.whatsapp.com/send?phone=201126576575&text=%F0%9F%93%9E"
}
projects = {
    "📝 Digit-classification - Deep Learning-based digit-classification.": "https://www.kaggle.com/code/ghadarabea/digit-classification",
    "📊 Housing-classification ": "https://www.kaggle.com/code/ghadarabea/housing",
    "📚 Spam-mails ": "https://www.kaggle.com/code/ghadarabea/fork-of-spam-mails-code",
    "🖼️ Titanic Dataset.": "https://www.kaggle.com/code/ghadarabea/titanic"
}

st.set_page_config(page_title=page_title, page_icon=page_icon)
# --- load CSS, resume and profile picture ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

col2, col1 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(name)
    st.write(description)
    # st.download_button(
    #     # label=" 📄 Download Resume",
    #     # data=PDFbyte,
    #     # file_name="Resume.pdf",
    #     # mime='application/octet-stream'
    # )
    st.write("📫", email)

st.write("#")
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("Experience & Qualifications")
st.divider()
st.write("""
    - ✔️ AI Engineer | Specializing in Machine Learning & Computer Vision.
    - ✔️ problem-solving skills.
""")

st.write("#")
st.subheader("Hard Skills")
st.divider()
st.write("""
- 👨‍💻 Programming: Python ( NumPy, Pandas, Scikit-learn, TensorFlow)
- 📊 Data Visualization: Matplotlib, Seaborn, Plotly
- 🧠 Machine Learning: Deep Learning, Computer Vision
""")

st.write("#")
st.subheader("Projects & Accomplishments")
st.write('---')

for project, link in projects.items():
    st.write(f"[{project}]({link})")