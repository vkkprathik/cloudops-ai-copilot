from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str
    agent: str = "aws"
    history: list = []