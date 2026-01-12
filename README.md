# 🧠 Context Engineering Agent: Tri-Tier Persistent Memory

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-orange.svg)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-green.svg)
![Framework](https://img.shields.io/badge/SDK-Google%20GenAI-blue.svg)

An advanced AI agent implementation demonstrating **Context Engineering** patterns. This project moves beyond simple prompting by implementing a managed, tri-tier memory system that ensures high-signal reasoning, low latency, and persistent recall across long-duration conversations.

---

## 🚀 The Problem: Token Bloat & Reasoning Fatigue
Even with massive context windows (1M+ tokens), throwing unorganized data at an LLM leads to:
1. **Reasoning Saturation:** The model misses the "signal" in the "noise."
2. **Economic Inefficiency:** Processing unnecessary tokens increases operational costs.
3. **Latency:** Large prompts significantly increase Time to First Token (TTFT).

## 🛠️ The Solution: Tri-Tier Memory Architecture
This agent implements a managed context lifecycle:
1. **System Instructions:** Fixed core behavior logic.
2. **Working Memory (Short-Term):** A sliding window of the most recent interactions managed by a `ContextManager`.
3. **Persistent Archive (Long-Term):** Semantic retrieval of past interactions using **ChromaDB**, injected only when relevant to the current query.

---

## 🏗️ Project Structure

```text
context_agent/
├── agent.py             # Main orchestrator & Google GenAI client
├── context_manager.py   # Sliding window & token pruning logic
├── vector_store.py      # ChromaDB interface for semantic memory
└── .env                 # API Credentials (Not tracked)
```

## 🔧 Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/ShivekMaharaj/context-engineering-agent.git
cd context-engineering-agent
```

2. **Install dependencies:**
```bash
pip install google-genai chromadb python-dotenv
```

