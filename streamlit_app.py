import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API__KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------ SESSION STATE ------------------
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ------------------ APP TITLE ------------------
st.set_page_config(page_title="AI NLP Toolkit", layout="centered")
st.title("🤖 NLP Toolkit")

# ------------------ AUTH SECTION ------------------
if not st.session_state.logged_in:

    menu = st.radio("Choose an option", ["Login", "Register"])

    if menu == "Register":
        st.subheader("📝 Registration")

        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Register"):
            if email in st.session_state.users:
                st.error("Email already exists!")
            else:
                st.session_state.users[email] = [name, password]
                st.success("Registration successful! Please login.")

    else:
        st.subheader("🔐 Login")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if email in st.session_state.users and st.session_state.users[email][1] == password:
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid email or password")

# ------------------ MAIN APP ------------------
else:
    st.success("Welcome to AI NLP Toolkit 🚀")

    task = st.selectbox(
        "Select NLP Task",
        [
            "Sentiment Analysis",
            "Language Translation (English → Bangla)",
            "Language Detection",
            "Text Summarization",
            "Keyword Extraction",
            "Named Entity Recognition",
            "Part-of-Speech Tagging",
            "Topic Modeling",
            "Text Classification",
            "Question Answering",
            "Text Generation",
            "Emotion Detection",
            "Intent Detection",
            "Paraphrase Detection"
        ]
    )

    if task != "Paraphrase Detection":
        user_text = st.text_area("Enter your text")

    if st.button("Run"):
        with st.spinner("Processing..."):

            if task == "Sentiment Analysis":
                prompt = f"Give me the sentiment of this sentence: {user_text}"

            elif task == "Language Translation (English → Bangla)":
                prompt = f"Give me Bangla translation of this sentence: {user_text}"

            elif task == "Language Detection":
                prompt = f"Detect the language of this sentence: {user_text}"

            elif task == "Text Summarization":
                prompt = f"Summarize this sentence: {user_text}"

            elif task == "Keyword Extraction":
                prompt = f"Extract important keywords from this sentence: {user_text}"

            elif task == "Named Entity Recognition":
                prompt = f"Identify named entities in this sentence: {user_text}"

            elif task == "Part-of-Speech Tagging":
                prompt = f"Tag each word with its part of speech: {user_text}"

            elif task == "Topic Modeling":
                prompt = f"Identify the main topic of this sentence: {user_text}"

            elif task == "Text Classification":
                prompt = f"Classify this sentence into a category: {user_text}"

            elif task == "Question Answering":
                prompt = f"Answer this question: {user_text}"

            elif task == "Text Generation":
                prompt = f"Generate a short text based on this prompt: {user_text}"

            elif task == "Emotion Detection":
                prompt = f"Detect the emotion expressed in this sentence: {user_text}"

            elif task == "Intent Detection":
                prompt = f"Detect the intent of this sentence: {user_text}"

            elif task == "Paraphrase Detection":
                text1 = st.text_input("First sentence")
                text2 = st.text_input("Second sentence")
                prompt = f"Do these sentences mean the same?\n1. {text1}\n2. {text2}"

            response = model.generate_content(prompt)
            st.subheader("✅ Result")
            st.write(response.text)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
