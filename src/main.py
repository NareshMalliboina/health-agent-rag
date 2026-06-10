from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import run_health_agent
from src.tracing import setup_tracing

setup_tracing()
app = FastAPI(title="Health Insurance Policy Agent API")

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_agent(request: QueryRequest):
    response = run_health_agent(request.query)
    return {"query": request.query, "response": response}