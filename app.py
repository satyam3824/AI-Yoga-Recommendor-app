import streamlit as st
from yoga_agent import get_agent_response
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="🧘 Yoga Recommender", layout="centered")
st.title("🧘‍♀️ AI Yoga Recommender")
st.subheader("Personalized yoga routine + AI pose assistant")

# Input form
with st.form("input_form"):
    name = st.text_input("Your Name")
    age = st.slider("Age", 10, 80)
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    goal = st.selectbox("Your Goal", ["Flexibility", "Strength", "Relaxation"])
    fitness_level = st.radio("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
    submitted = st.form_submit_button("Get My Yoga Plan")

# Mock routine based on goal
if submitted:
    st.success(f"Hi {name}, here’s your yoga routine for {goal} 👇")

    if goal == "Flexibility":
        poses = ["Downward Dog", "Seated Forward Bend", "Triangle Pose"]
    elif goal == "Strength":
        poses = ["Plank Pose", "Chair Pose", "Warrior II"]
    else:
        poses = ["Child's Pose", "Cat-Cow", "Legs Up the Wall"]

    for pose in poses:
        st.markdown(f"✅ **{pose}**")

# Gemini Assistant
st.divider()
st.subheader("💬 Ask AI about any yoga pose:")
question = st.text_input("Type your question here...")

if question:
    with st.spinner("Thinking..."):
        answer = get_agent_response(question)
    st.info(answer)
