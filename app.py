import streamlit as st
from datetime import datetime
from assistant import get_response, safe_calculate, get_quote

st.set_page_config(page_title="Student AI Virtual Assistant", page_icon="🎓", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Student AI Assistant. Ask me about study topics, use the calculator, or manage your tasks."}
    ]
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("🎓 Student AI Virtual Assistant")
st.caption("A simple Python + Streamlit mini project for students")

with st.sidebar:
    st.header("About this project")
    st.write("A rule-based virtual assistant that supports students with study FAQs, calculations, date/time, motivation and task management.")
    st.divider()
    st.subheader("Quick actions")
    if st.button("💡 Show a motivational quote", use_container_width=True):
        st.session_state.messages.append({"role": "assistant", "content": get_quote()})
    if st.button("🕒 Show current date and time", use_container_width=True):
        st.session_state.messages.append({"role": "assistant", "content": "Current date and time: " + datetime.now().strftime("%d %B %Y, %I:%M:%S %p")})
    if st.button("🧹 Clear chat", use_container_width=True):
        st.session_state.messages = []

    st.divider()
    st.subheader("Example questions")
    st.markdown("- What is Artificial Intelligence?\n- Explain machine learning\n- What is Python?\n- Give me study tips\n- What is NLP?")

chat_col, task_col = st.columns([1.7, 1], gap="large")

with chat_col:
    st.subheader("💬 Chat with your assistant")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Type your question here...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        answer = get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()

with task_col:
    st.subheader("📝 Student To-Do List")
    with st.form("add_task_form", clear_on_submit=True):
        task_text = st.text_input("Enter a task", placeholder="e.g. Complete AI assignment")
        submitted = st.form_submit_button("Add task", use_container_width=True)
    if submitted:
        if task_text.strip():
            st.session_state.tasks.append({"task": task_text.strip(), "done": False})
            st.rerun()
        else:
            st.warning("Please enter a task first.")

    if not st.session_state.tasks:
        st.info("No tasks yet. Add your first task above.")
    else:
        for index, item in enumerate(st.session_state.tasks):
            col_a, col_b = st.columns([0.8, 0.2])
            with col_a:
                checked = st.checkbox(item["task"], value=item["done"], key=f"task_{index}")
                st.session_state.tasks[index]["done"] = checked
            with col_b:
                if st.button("🗑️", key=f"delete_{index}", help="Delete task"):
                    st.session_state.tasks.pop(index)
                    st.rerun()
        completed = sum(1 for item in st.session_state.tasks if item["done"])
        st.progress(completed / len(st.session_state.tasks))
        st.caption(f"{completed} of {len(st.session_state.tasks)} tasks completed")

st.divider()
st.caption("Mini Project | Built using Python and Streamlit")
