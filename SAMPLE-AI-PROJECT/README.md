# AI Chat Application with RAG

An intelligent chat application powered by LangChain, OpenAI/Anthropic, and vector databases.

## Features

- **Conversational AI**: GPT-4 and Claude 3 integration
- **RAG Pipeline**: Retrieval-Augmented Generation for context-aware responses
- **Vector Search**: Pinecone, ChromaDB, and Weaviate support
- **Real-time Chat**: Next.js frontend with Supabase backend
- **Multi-Agent System**: LangChain agents for complex workflows

## Tech Stack

### Frontend
- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Supabase Client**: Real-time subscriptions

### Backend
- **FastAPI**: High-performance Python API
- **LangChain**: LLM orchestration framework
- **Vector Databases**: Pinecone, ChromaDB, Weaviate
- **Supabase**: PostgreSQL with real-time capabilities

### AI/ML
- **OpenAI GPT-4**: Primary language model
- **Anthropic Claude 3**: Alternative LLM
- **Embeddings**: text-embedding-ada-002
- **Prompt Engineering**: Structured prompt templates

## Project Structure

```
├── app/                    # Next.js app directory
│   ├── api/               # API routes
│   ├── chat/              # Chat interface
│   └── components/        # React components
├── backend/               # FastAPI backend
│   ├── agents/           # LangChain agents
│   ├── chains/           # LangChain chains
│   ├── embeddings/       # Vector embeddings
│   └── prompts/          # Prompt templates
├── supabase/             # Database migrations
└── tests/                # Test suite
```

## Development

```bash
# Install dependencies
npm install
pip install -r requirements.txt

# Run development servers
npm run dev              # Frontend (port 3000)
uvicorn main:app --reload  # Backend (port 8000)
```

## Architecture

This is a fullstack AI application with:
- Frontend chat interface built with Next.js
- Backend API with FastAPI handling LLM requests
- Vector database for semantic search
- Supabase for user data and chat history
- LangChain for complex AI workflows


