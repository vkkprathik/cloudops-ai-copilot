from groq import Groq
from dotenv import load_dotenv
import os
from services.project_explainer_agent import PROJECT_EXPLAINER_PROMPT
from rag.vector_store import search_knowledge
from services.architecture_agent import ARCHITECTURE_PROMPT
from services.prompts import (
    AWS_PROMPT,
    CLI_PROMPT,
    DEVOPS_PROMPT,
    INTERVIEW_PROMPT,
    LINUX_PROMPT,
)
from services.terraform_agent import TERRAFORM_PROMPT

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


AGENT_PROMPTS = {
    "aws": AWS_PROMPT,
    "aws support": AWS_PROMPT,
    "linux": LINUX_PROMPT,
    "devops": DEVOPS_PROMPT,
    "cli": CLI_PROMPT,
    "aws-cli": CLI_PROMPT,
    "terraform": TERRAFORM_PROMPT,
    "tf": TERRAFORM_PROMPT,
    "interview": INTERVIEW_PROMPT,
    "interview coach": INTERVIEW_PROMPT,
    "resume": PROJECT_EXPLAINER_PROMPT,
    "mentor": PROJECT_EXPLAINER_PROMPT,
    "project explainer": PROJECT_EXPLAINER_PROMPT,
    "architecture": ARCHITECTURE_PROMPT,
}


def get_prompt(agent: str) -> str:
    normalized_agent = (agent or "aws").strip().lower()
    return AGENT_PROMPTS.get(normalized_agent, AWS_PROMPT)


def get_ai_response(
    question: str,
    agent: str,
    history=None
) -> str:

    agent_key = (agent or "aws").strip().lower()

    print(f"Selected Agent: {agent_key}")

    try:

        # ==========================================
        # RAG ENABLED AGENTS
        # ==========================================

        rag_agents = [
            "aws",
            "linux",
            "devops",
            "cli",
            "terraform"
        ]

        rag_context = ""

        if agent_key in rag_agents:

            rag_context = search_knowledge(
                question
            )

            print("\n========== RAG SEARCH ==========")
            print(question)
            print("\nRetrieved Context:\n")
            print(rag_context[:1000])
            print("\n================================\n")

        # ==========================================
        # BUILD USER PROMPT
        # ==========================================

        if rag_context:

            user_prompt = f"""
Cloud Knowledge Base:

{rag_context}

User Question:

{question}

Instructions:

1. Use the Cloud Knowledge Base whenever relevant.
2. Prioritize the retrieved knowledge.
3. If knowledge is insufficient, use your expertise.
4. Give practical troubleshooting steps.
5. Include commands whenever applicable.
"""

        else:

            user_prompt = question

        # ==========================================
        # SYSTEM PROMPT
        # ==========================================

        messages = [
            {
                "role": "system",
                "content": get_prompt(agent_key)
            }
        ]

        # ==========================================
        # CHAT HISTORY
        # ==========================================

        if history:

            for msg in history:

                role = msg.get("role")
                content = msg.get("content")

                if role and content:

                    messages.append(
                        {
                            "role": role,
                            "content": content
                        }
                    )

        # ==========================================
        # CURRENT USER MESSAGE
        # ==========================================

        messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        # ==========================================
        # GROQ CALL
        # ==========================================

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.3,
            max_tokens=2000
        )

        return response.choices[0].message.content

    except Exception as e:

        print(f"Groq Error: {e}")

        return f"Error: {str(e)}"

