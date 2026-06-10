from typing import TypedDict, List
from src.rag import get_vector_store
from src.safety import InputGuardrail, OutputGuardrail
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

class AgentState(TypedDict):
    query: str
    messages: List
    context: str
    response: str

def run_health_agent(user_query: str) -> str:
    # 1. Input Guardrail Check
    guard = InputGuardrail(query=user_query)
    if not guard.validate_input():
        return "Error: Input query violated safety guidelines."

    # 2. Retrieval Step
    retriever = get_vector_store()
    docs = retriever.invoke(user_query)
    context_text = "\n".join([doc.page_content for doc in docs])

    # 3. LLM Generation
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = f"Answer the user query based strictly on the following health policy context:\n\nContext:\n{context_text}\n\nQuery: {user_query}"
    
    result = llm.invoke([HumanMessage(content=prompt)])
    
    # 4. Output Guardrail Check (Groundedness)
    final_response = OutputGuardrail.verify_groundedness(result.content, context_text)
    return final_response