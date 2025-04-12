import json
import streamlit as st
import re

# Load knowledge base
with open("knowledge_base.json", "r") as file:
    kb = json.load(file)

# Basic keyword search
def get_response(query):
    query = query.lower()

    if "syllabus" in query:
        return kb["syllabus_2025"]
    elif "english" in query and "questions" in query:
        return kb["english_questions"]
    elif "cut-off" in query or "cutoff" in query and "nlsiu" in query:
        return kb["nlsiu_cutoff_2024"]
    elif "exam date" in query or "when is clat" in query:
        return kb["exam_date"]
    elif "duration" in query:
        return kb["duration"]
    elif "marking scheme" in query or "marks" in query:
        return kb["marking_scheme"]
    elif "eligibility" in query:
        return kb["eligibility"]
    else:
        return "Sorry, I couldn't find an answer to that. Try asking about syllabus, cut-off, or eligibility."

# Streamlit app
st.title("CLAT FAQ Chatbot 🤖")
st.write("Ask me anything about CLAT 2025!")

query = st.text_input("Your question:")

if query:
    response = get_response(query)
    st.success(response)
