# app.py

import streamlit as st
from agent_travel_planner import setup_agent_executor

st.set_page_config(page_title="AI Travel Planner", layout="centered")

st.title("🌍 AI Travel Planner")
st.markdown("Plan smart, personalized trips using AI + live tools 🧠")

query = st.text_input("✈️ Ask your travel agent", placeholder="e.g., Plan a 4-day trip to Japan under 2000 AED")

if "agent_executor" not in st.session_state:
    st.session_state.agent_executor = setup_agent_executor()

if query:
    with st.spinner("Thinking..."):
        result = st.session_state.agent_executor.invoke({"input": query})
        st.markdown("### 🧠 Agent says:")
        with st.expander("🧳 Detailed Plan", expanded=True):
          st.markdown(result["output"])
