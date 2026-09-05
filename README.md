# Agentic RAG Chatbot with LangGraph
<hr>

A conversational Retrieval-Augmented Generation (RAG) application built using LangGraph. This chatbot goes beyond simple question-answering by utilizing stateful memory, tool-calling (web search, RAG as a tool, getting stack price and user defined tool for calculations), and local vector search to provide grounded, real-time responses with low perceived latency via streaming.
<br><hr>
## Features

*   **Graph-Based Orchestration (LangGraph):** Complex agent workflows, routing, and tool execution are handled via LangGraph's state graph architecture.
*   **Persistent Memory:** Chat histories are stored locally using SQLite3. Users can pause, exit, and resume past conversations seamlessly using unique session IDs.
*   **Vector Search (FAISS):** Local, in-memory vector database integration for fast retrieval of ingested document embeddings.
*   **Tool Calling:** <br>
1.Integrated with LangChain's DuckDuckGo search tool to allow the agent to fetch real-time information from the web when local knowledge context falls short.<br>
2.Uses RAG as a tool for providing contextual answers.<br>
3.Tool to get the current stock price of a company.<br>
4.User defined tool for calculations.<br>
*   **Response Streaming:** Token-by-token output streaming to the frontend for a responsive, ChatGPT-like user experience.

<br><hr>
## Tech Stack

*   **Framework:** LangChain & LangGraph
*   **Vector Database:** FAISS (faiss-cpu)
*   **Database (Memory):** SQLite3
*   **Search Integration:** DuckDuckGo API (`langchain-duckduckgo`), latest stock price of company through URL
*   **Embeddings & LLM:** [Grok / Gemini / Open Model(Hugging Face)]

<br><hr>
## Installation

1. Clone the repository:
```bash
git clone https://github.com/Anurag-Rawat-07/ChatBot.git
cd ChatBot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables. Create a `.env` file in the root directory:
```env
# Example .env file
GROQ_API_KEY=your_api_key_here
# Add any other required API keys for your specific LLM/Embeddings
```

<br><hr>
## Usage

```bash
streamlit run frontend.py
```

<br><hr>
### Resuming Conversations
To resume a past chat, just click on any chat in the past conversation section. The SQLite3 backend will automatically load the past message graph and inject it into the LangGraph state.

<br><hr>
## Project Structure

```text
├── rag_backend.py          # LangGraph state, nodes, and edges setup
├── memory.py               # SQLite3 database connection and checkpointer
├── tools.py                # DuckDuckGo search and FAISS retrieval tools
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```
<br>
<hr>
<h2>Images</h2>
<img width="1910" height="851" alt="Screenshot 2026-09-06 012712" src="https://github.com/user-attachments/assets/1d119678-7830-4ed5-b4a4-e5d419c591d7" />
<br>
<hr>
<br>
<img width="1908" height="860" alt="Screenshot 2026-09-06 014731" src="https://github.com/user-attachments/assets/3c7076e6-6fe6-48d5-91cd-193f14029fc2" />

