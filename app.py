import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Streamlit app title
st.title("🤖 TalentScout Hiring Assistant")

# Session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_step" not in st.session_state:
    st.session_state.current_step = 0
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}

# Candidate questions
details_questions = [
    ("full_name", "What's your full name?"),
    ("email", "What's your email address?"),
    ("phone", "What's your phone number?"),
    ("experience", "How many years of experience do you have?"),
    ("position", "What position are you interested in?"),
    ("location", "Where are you currently located?"),
    ("tech_stack", "List the programming languages, frameworks, or tools you're familiar with."),
]

# Generate tech questions using OpenRouter API
def generate_questions(tech_stack):
    prompt = f"Generate 3 technical interview questions for someone skilled in: {tech_stack}."
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "system", "content": "You are a helpful AI hiring assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Failed to generate questions: {e}"

# Handle each question step-by-step
if st.session_state.current_step < len(details_questions):
    key, question = details_questions[st.session_state.current_step]
    st.markdown(f"**Bot:** {question}")
    user_input = st.text_input("You:", key=f"input_{st.session_state.current_step}")

    if user_input:
        st.session_state.candidate_info[key] = user_input
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", "Thanks!"))
        st.session_state.current_step += 1
        st.rerun()

# All details collected, generate questions
elif st.session_state.current_step == len(details_questions):
    tech_stack = st.session_state.candidate_info.get("tech_stack", "")
    with st.spinner("Generating technical questions..."):
        questions = generate_questions(tech_stack)
        st.markdown("**Bot:** Here are some questions based on your tech stack:")
        st.markdown(questions)
        st.session_state.current_step += 1

# Show chat history
st.markdown("---")
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
