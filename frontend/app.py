import streamlit as st
import requests

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CloudOps AI Copilot",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD CHAT HISTORY
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("👤 Prathik")

    st.markdown("---")

    st.subheader("☁️ Cloud Skills")

    st.markdown("☁️ AWS")
    st.markdown("🐳 Docker")
    st.markdown("⚙️ Terraform")
    st.markdown("☸️ Kubernetes")
    st.markdown("🐧 Linux")
    st.markdown("🚀 DevOps")

    st.markdown("---")

    # =========================
    # AGENT SELECTOR
    # =========================

    agent_options = {
        "AWS Support Engineer": "aws",
        "AWS CLI Generator": "cli",
        "Terraform Generator": "terraform",
        "Interview Coach": "interview",
        "Resume Project Explainer": "resume",
        "Linux Administrator": "linux",
        "DevOps Engineer": "devops",
        "Architecture Generator": "architecture"
    }

    selected_label = st.selectbox(
        "🤖 Choose Agent",
        list(agent_options.keys())
    )

    selected_agent = agent_options[selected_label]

    st.markdown("---")

    # =========================
    # ANALYTICS
    # =========================

    st.subheader("📊 Analytics")

    try:

        analytics = requests.get(
            "http://127.0.0.1:8000/analytics"
        ).json()

        st.metric(
            "Total Messages",
            analytics["total_messages"]
        )

        st.markdown("### Agent Usage")

        for agent, count in analytics["agent_stats"]:

            st.write(
                f"🤖 {agent.upper()} : {count}"
            )

    except Exception:

        st.warning(
            "Analytics unavailable"
        )

    st.markdown("---")

    # =========================
    # CHAT HISTORY
    # =========================

    st.subheader("📜 Chat History")

    st.write(
        f"Messages Stored: {len(st.session_state.messages)}"
    )

    if len(st.session_state.messages) > 0:

        st.success("History Loaded")

        for msg in st.session_state.messages[-5:]:

            st.caption(
                f"{msg['role']}: {msg['content'][:40]}..."
            )

    st.markdown("---")

    # =========================
    # CLEAR CHAT
    # =========================

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    st.caption("CloudOps AI Copilot v1.0")

# ==========================================
# MAIN HEADER
# ==========================================

st.title("☁️ CloudOps AI Copilot")

st.caption(
    "AWS • Linux • Docker • Terraform • Kubernetes • DevOps"
)

st.success(
    f"Active Agent: {selected_label}"
)

# ==========================================
# SERVICE CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("☁️ AWS")

with col2:
    st.info("🐳 Docker")

with col3:
    st.info("⚙️ Terraform")

with col4:
    st.info("☸️ Kubernetes")

st.markdown("---")

# ==========================================
# DISPLAY CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )

# ==========================================
# CHAT INPUT
# ==========================================

prompt = st.chat_input(
    "Ask your cloud question..."
)

if prompt:

    # Save User Message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # AI Response

    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={
                        "question": prompt,
                        "agent": selected_agent,
                        "history": st.session_state.messages[-10:]
                    }
                )

                answer = response.json().get(
                    "answer",
                    "No response received."
                )

            except Exception as e:

                answer = (
                    f"❌ Backend Error: {str(e)}"
                )

            st.markdown(answer)

    # Save AI Response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Built by Prathik Kulkarni | FastAPI • Groq • SQLite • Streamlit"
)