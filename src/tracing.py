import os
from dotenv import load_dotenv

# Automatically loads the keys from your .env file
load_dotenv()

def setup_tracing():
    """Configures environment variables for LangSmith tracing and observability."""
    os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
    os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langsmith.io")
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
    os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "health-agent-rag")
    print("LangSmith tracing initialized for project:", os.environ["LANGCHAIN_PROJECT"])

if __name__ == "__main__":
    setup_tracing()