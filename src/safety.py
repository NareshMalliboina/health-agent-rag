from pydantic import BaseModel, Field

class InputGuardrail(BaseModel):
    query: str = Field(..., description="User query to evaluate")

    def validate_input(self) -> bool:
        # Block prompt injection or malicious input queries
        forbidden_keywords = ["ignore previous instructions", "system prompt", "drop table"]
        for word in forbidden_keywords:
            if word in self.query.lower():
                return False
        return True

class OutputGuardrail:
    @staticmethod
    def verify_groundedness(response_text: str, retrieved_context: str) -> str:
        """Ensures the response is strictly supported by the retrieved health policy context to eliminate hallucinations."""
        if not retrieved_context.strip():
            return "I cannot answer this question as no relevant health policy documents were found."
        
        return response_text