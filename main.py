from fastapi import FastAPI

from models.request_models import QuestionRequest
from services.ai_service import get_ai_response

from database.db import (
    create_table,
    save_message,
    load_messages
)

from database.db import (
    get_total_messages,
    get_agent_stats
)

app = FastAPI()

# Create database table on startup
create_table()


@app.get("/")
def home():

    return {
        "message": "AI Cloud Assistant Running"
    }


@app.get("/about")
def about():

    return {
        "project": "AI Cloud Support Assistant",
        "developer": "Prathik",
        "version": "1.0"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    # Save user message
    save_message(
        request.agent,
        "user",
        request.question
    )

    # Get AI response
    answer = get_ai_response(
        request.question,
        request.agent,
        request.history
    )

    # Save AI response
    save_message(
        request.agent,
        "assistant",
        answer
    )

    return {
        "question": request.question,
        "answer": answer
    }


@app.get("/history")
def history():

    messages = load_messages()

    return {
        "messages": messages
    }
    
    
@app.get("/analytics")
def analytics():

    return {
        "total_messages": get_total_messages(),
        "agent_stats": get_agent_stats()
    }   
