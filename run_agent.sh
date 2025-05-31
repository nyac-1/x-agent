#!/bin/bash

# LangChain Q&A Agent Runner Script
# This script activates the virtual environment and runs the agent

echo "🚀 Starting LangChain Q&A Agent..."
echo "📦 Activating virtual environment..."

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please create one with:"
    echo "   python -m venv venv"
    exit 1
fi

# Activate virtual environment and run the agent
source venv/bin/activate

echo "🔍 Checking dependencies..."
if ! python -c "import langchain, google.generativeai, duckduckgo_search, wikipedia, arxiv, langchain_experimental" 2>/dev/null; then
    echo "📦 Installing missing dependencies..."
    pip install -r requirements.txt
fi

echo "✅ Dependencies ready!"
echo "🦜 Starting agent..."
echo "=================================="

python main.py 