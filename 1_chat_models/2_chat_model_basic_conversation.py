import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Initialize the Chat Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Streamlit app setup
st.title("Ask an Expert with Google GEMINI")
st.markdown("Choose an expert type, describe how the AI should behave, and ask it your questions.")

# User input for profession/expertise
st.subheader("Expert Type")
expert_type = st.selectbox(
    "Select the type of expert you want to interact with:",
    ["General Expert", "Physician", "Dentist", "Mathematician", "Engineer", "Lawyer", "Scientist", "Custom"],
)

# User input for AI behavior
st.subheader("AI Behavior")
if expert_type == "Custom":
    ai_behavior = st.text_input(
        "Describe how the AI should behave (e.g., 'Provide legal advice', 'Explain physics concepts', etc.):",
        "Be a helpful assistant",
    )
else:
    ai_behavior = f"Act as a knowledgeable {expert_type.lower()} and assist with relevant questions."

# Section for user questions
st.subheader(f"Ask a {expert_type}")
input_question = st.text_input(f"Enter your question:", f"Ask anything from {expert_type}?")
if st.button("Ask"):
    # Messages for the model
    messages = [
        SystemMessage(content=ai_behavior),
        HumanMessage(content=input_question + " Be concise and to the point."),
    ]
    # Invoke the model
    result = llm.invoke(messages)
    st.write(f"**AI's Answer:** {result.content}")