import streamlit as st
from openai import OpenAI
from langchain_utils import invoke_chain
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()
st.title("Langchain NL2SQL Chatbot ~Ashish")




# Load environment variables from .env

api_key = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=api_key)

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    # print("Creating session state")
    st.session_state.messages = []

# Tabs: Database Schema + Sample Input + Chatbot
tab1, tab2, tab3 = st.tabs(["Database Schema", "Sample Input", "Chatbot"])

# -----------------------------
# Database Schema tab (upload image)
# -----------------------------
with tab1:
    st.subheader("Database Schema")
    try:
        st.image("schema.png", caption="Database ER Diagram")
    except FileNotFoundError:
        st.error("⚠️ schema.png not found. Please place it in the app folder.")

# -----------------------------
# Sample Input tab (table of sample queries)
# -----------------------------
sample_data = {
    "Sample #": [1, 2, 3, 4, 5],
    "Sample Question": [
        "What is the price of `1968 Ford Mustang`?",
        "How many customers have an order count greater than 5?",
        "How many products are there?",
        "How many employees do we have?",
        "How many customers have a credit limit more than 50,000?"
    ]
}
df = pd.DataFrame(sample_data)

with tab2:
    st.subheader("Sample Input Questions")
    st.table(df)


with tab3:
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.spinner("Generating response..."):
            with st.chat_message("assistant"):
                response = invoke_chain(prompt,st.session_state.messages)
                st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

