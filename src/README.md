# Enterprise Health Insurance Multi-Agent RAG System

An end-to-end, production-grade Agentic Retrieval-Augmented Generation (RAG) system built for processing health insurance policies, claim validations, and coverage queries.

This repository demonstrates a modular architecture featuring input/output safety guardrails, dynamic query routing, observability tracing, and automated RAG evaluation to ensure low hallucination rates and high domain accuracy.

---

## Key Features & Architecture

* **Multi-Agent Orchestration (`src/agent.py`):** Orchestrates domain intent routing between direct LLM responses, vector store retrievals, and safety fallback mechanisms.
* **Domain-Specific RAG Pipeline (`src/rag.py`):** Vector search pipeline backed by ChromaDB and OpenAI Embeddings to index and query complex health insurance policy documents.
* **Enterprise Guardrails & Safety (`src/safety.py`):** Enforces input validation and output filtering to mitigate prompt injection, medical/legal liability risks, and off-topic queries.
* **Observability & Tracing (`src/tracing.py`):** Integrates execution tracking across agent execution steps, tool calls, and retrieval contexts.
* **Automated Evaluation Suite (`src/evaluation.py`):** Quantitative benchmark testing for evaluating context precision, recall, and response groundedness.
* **REST API Layer (`src/main.py`):** Production-ready FastAPI interface with Uvicorn server integration.

---

## System Architecture

```text
[ User Query ]
       │
       ▼
┌──────────────┐
│  src/safety  │ ──(Rejected)──► [ Return Guardrail Error ]
└──────┬───────┘
       │ (Passed)
       ▼
┌──────────────┐
│  src/agent   │ ──(Routing Logic)
└──────┬───────┘
       ├────────────────────────┐
       ▼                        ▼
┌──────────────┐        ┌──────────────┐
│   src/rag    │        │ Direct LLM   │
│  (ChromaDB)  │        │ Response     │
└──────┬───────┘        └──────┬───────┘
       └───────────┬────────────┘
                   ▼
         ┌──────────────────┐
         │   src/tracing    │
         └─────────┬────────┘
                   ▼
         [ Final Output Response ]




## Quickstart & Local Setup

### Prerequisites
* Python 3.11 installed
* OpenAI API key configured in `.env`

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/health-agent-rag.git](https://github.com/YOUR_USERNAME/health-agent-rag.git)
   cd health-agent-rag

2.** Install dependencies:**
  ```bash
  python -m pip install -r requirements.txt

3.** Run the Evaluation Suites:**
  ```bash
  python -m src.evaluation

4.** Launch the FastAPI Server:**
  ```bash
  python -m uvicorn src.main:app --reload  

   ---

## API Documentation

### POST `/query`
Executes the multi-agent RAG workflow for insurance policy verification.

**Request Body:**
```json
{
  "query": "Does the policy cover room rent charges during hospitalization?"
}


** Response Payload:**
{
  "answer": "Yes, standard hospitalization room charges are covered up to 1% of the Sum Insured per day as specified in Section 3.1.",
  "sources": [
    {
      "document": "policy_terms_v2.pdf",
      "page": 8
    }
  ],
  "guardrail_status": "PASSED"
}

---

## Evaluation & Benchmarking

The automated evaluation pipeline (`src/evaluation.py`) measures system accuracy across three key operational dimensions:

| Metric | Target | Description |
| :--- | :--- | :--- |
| **Context Recall** | > 85% | Measures if the vector retriever fetches all relevant policy clauses |
| **Faithfulness** | > 90% | Validates that the answer is derived strictly from retrieved context (zero hallucination) |
| **Safety Compliance**| 100% | Ensures prompt injection attempts and out-of-scope requests are blocked |

Run benchmarks locally:
```bash
python -m src.evaluation


---

## Engineering Highlights & Design Decisions

* **Deterministic Pre-Retrieval Guardrails:** Implemented input validation and sanitization filters in `src/safety.py` to intercept malicious prompts, prompt injections, and out-of-domain queries before triggering expensive vector database searches or LLM calls.
* **Optimized RAG Chunking:** Configured ChromaDB document ingestion in `src/rag.py` with chunking strategies specifically tuned for dense regulatory and legal text found in health insurance policy clauses.
* **Lightweight Observability & Tracing:** Developed modular execution tracing (`src/tracing.py`) to track step-by-step agent node transitions, tool invocations, and token latencies without heavy external infrastructure dependencies.