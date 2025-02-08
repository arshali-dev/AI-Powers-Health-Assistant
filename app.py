import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from transformers import pipeline

# Load the GPT-2 model
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult Doctor for Accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointment with the Doctor? "
    elif "medication" in user_input:
        return " It's important to take prescribed medicines regularly. If you have concerns, consulting your doctor."
    else:
        response= chatbot(user_input,max_lenth=500,num_return_sequences=1)
    return response[0]['generated_text']


def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("Hello! How can i assist you today?")  # Input for user message
    
    if st.button("Submit"):
        if user_input:
            st.write("user:",user_input)
            with st.spinner("Processing your query, please wait..."):
                response=healthcare_chatbot(user_input)
            st.write("healthcare Assistant :",response)
            print(response)
        else:
            st.write("please enter the message to get a response")

if __name__ == "__main__":
    main()
