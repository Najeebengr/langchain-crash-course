from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize the Chat Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# Streamlit App
st.title("Chat Model Basic")

# Input Text Box
user_input = st.text_input("Enter your question:", "What is the capital of France?")

if st.button("Get Answer"):
    try:
        # Invoke the model with the user input
        result = llm.invoke(user_input)
        
        # Display the result
        st.subheader("Answer:")
        st.write(result.content)
    except Exception as e:
        # Handle exceptions
        st.error(f"Error: {str(e)}")