# LangChain Q&A Agent with Custom Gemini LLM

A question-answer agent built with LangChain framework using a custom Gemini LLM wrapper with exactly 3 methods. Features proper LangChain agent orchestration with ReAct pattern and conversation memory management.

## Features

- **LangChain Framework** - Agent orchestration using AgentExecutor
- **Custom 3-Method Gemini LLM** with constrained interface:
  - `text_to_text()` - Basic text completion
  - `text_to_json()` - Structured JSON responses  
  - `text_to_function_call()` - Function calling capabilities
- **ReAct Agent Pattern** - Reasoning and acting with tools
- **Conversation Memory** - Context retention across interactions
- **Dynamic Tool Selection** - Automatic tool orchestration
- **Centralized Prompts** - All prompts, schemas, and function definitions in one place
- **Hybrid Tool Suite** - Custom tools + native LangChain tools

## Available Tools

### Custom Tools
- **Web Search** - DuckDuckGo internet search
- **Calculator** - Mathematical operations  
- **Date/Time** - Current date and time information

### Native LangChain Tools
- **Wikipedia** - Encyclopedic information lookup
- **ArXiv** - Academic papers and research search
- **Python REPL** - Safe Python code execution

## Conversation Memory

### Memory Features
- Context retention throughout conversation
- Memory initialization for fresh conversations
- Memory cleanup when needed
- Conversation history viewing

### Memory Commands
```
help        Show available commands
history     Display conversation history
clear       Clear conversation memory
new         Start new conversation (clears memory)
quit        End session (auto-clears memory)
```

### Memory API
```python
agent = LangChainAgent(api_key)

agent.init_conversation()         # Initialize new conversation
agent.end_conversation()          # Clear memory and end
agent.show_conversation_history() # Display history
agent.get_conversation_history()  # Get history as list
```

## Project Structure

```
langchain_gemini_agent/
├── prompts/
│   ├── agent_prompts.py      # Agent prompt templates
│   ├── schemas.py            # JSON response schemas
│   ├── function_definitions.py # Tool function definitions
│   └── __init__.py
├── llm/
│   ├── custom_gemini.py      # Custom 3-method Gemini LLM
│   ├── langchain_adapter.py  # LangChain LLM adapter
│   └── __init__.py
├── tools/
│   ├── web_search.py         # DuckDuckGo search tool
│   ├── calculator.py         # Math operations tool
│   ├── datetime_tool.py      # Date/time tool
│   ├── langchain_tools.py    # LangChain tool wrappers
│   └── __init__.py
├── agent/
│   ├── langchain_agent.py    # LangChain agent with ReAct + Memory
│   ├── README.md            # Agent architecture deep dive
│   └── __init__.py
├── venv/                     # Virtual environment (recommended)
├── main.py                   # CLI interface
├── run_agent.sh             # Venv runner script
├── requirements.txt          # Dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Quick Start

### Option 1: Using Virtual Environment (Recommended)

1. **Create and activate virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set your Gemini API key**:
```bash
echo "GEMINI_API_KEY=your_actual_gemini_api_key" > .env
```

4. **Run the agent**:
```bash
python main.py
# OR use the convenience script:
./run_agent.sh
```

### Option 2: Global Installation

1. **Install dependencies globally**:
```bash
pip install -r requirements.txt
```

2. **Set your Gemini API key**:
```bash
echo "GEMINI_API_KEY=your_actual_gemini_api_key" > .env
```

3. **Run the agent**:
```bash
python main.py
```

## Example Usage

### Context Retention
```
User: "Remember that my name is Sam and I love Python"
Agent: "I'll remember that your name is Sam and you love Python programming!"

User: "What programming language do I love?"
Agent: "Based on our conversation, you love Python programming!"
```

### Sequential Questions with Tools
```
User: "What is the current Bitcoin price?"
Agent: [uses web_search] → "Bitcoin is currently $43,250"

User: "Calculate 15% of that amount"
Agent: [uses calculator with context] → "15% of $43,250 is $6,487.50"

User: "Find a Wikipedia article about cryptocurrency"
Agent: [uses wikipedia] → "Cryptocurrency is a digital currency..."
```

### Advanced Tool Usage
```
User: "Search for recent papers about transformer models"
Agent: [uses arxiv] → "Found recent papers on transformer architectures..."

User: "Create a Python script to calculate the fibonacci sequence"
Agent: [uses python_repl] → "def fibonacci(n): ..."
```

## Custom LLM Architecture

### 3-Method Constraint
```python
class CustomGeminiLLM:
    def text_to_text(self, prompt: str) -> str:
        """Basic text completion with 1-second rate limiting"""
        
    def text_to_json(self, prompt: str, schema: dict) -> dict:
        """Structured JSON response with schema validation"""
        
    def text_to_function_call(self, prompt: str, functions: List[dict]) -> dict:
        """Function calling in Vertex AI style"""
```

### LangChain Integration
```python
class LangChainGeminiAdapter(LLM):
    def _call(self, prompt: str, **kwargs) -> str:
        return self.custom_llm.text_to_text(prompt)
```

### Memory Implementation
```python
self.memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="output"
)
```

## Centralized Prompts Architecture

### Prompts Directory Structure
- **agent_prompts.py** - ReAct agent templates with memory support
- **schemas.py** - JSON schemas for structured responses
- **function_definitions.py** - Tool function definitions for LLM

### Benefits of Centralization
- Single source of truth for all prompts
- Easy prompt modification and testing
- Clear separation from business logic
- Simplified prompt version control

## Agent Behavior

### ReAct Pattern with Memory
1. **Thought** - Analyze what needs to be done considering conversation history
2. **Action** - Select appropriate tool
3. **Observation** - Process tool results
4. **Final Answer** - Provide response using memory context

### Memory-Aware Tool Selection
- References previous conversations for context
- Maintains conversation continuity
- Proper pronoun resolution ("that", "it", "the previous result")

## Technical Details

### Virtual Environment Benefits
- Isolated dependencies
- Reproducible setup
- No conflicts with system packages
- Easy cleanup and management

### Memory Implementation
- LangChain ConversationBufferMemory stores full conversation
- Human/AI message distinction
- Memory key integrated into prompt template
- Auto-cleanup on session end

### Rate Limiting
- 1-second sleep between Gemini API calls
- Prevents API quota exhaustion

### Error Handling
- Graceful tool failure handling
- Parse error recovery in LangChain
- Memory persistence during errors

## Dependencies

- `langchain>=0.1.0` - Main framework (includes memory)
- `langchain-core>=0.1.0` - Core LangChain components
- `langchain-community>=0.0.10` - Community tools
- `langchain-experimental>=0.0.50` - Experimental tools (Python REPL)
- `google-generativeai>=0.3.0` - Gemini API
- `duckduckgo-search>=4.0.0` - Web search
- `python-dotenv>=1.0.0` - Environment variables
- `pydantic>=2.0.0` - Data validation
- `wikipedia>=1.4.0` - Wikipedia API
- `arxiv>=2.1.0` - ArXiv API

## Key Benefits

- **Context Continuity** - Natural conversation flow
- **Reference Resolution** - Handles "that", "it", "the previous result"
- **User Preferences** - Remembers user information
- **Session Management** - Clean conversation boundaries
- **Clean Architecture** - Minimal dependencies, clear module boundaries
- **Centralized Prompts** - All prompts and schemas in one place
- **Hybrid Tools** - Best of custom and native LangChain tools
- **Virtual Environment** - Isolated, reproducible setup
- **Rate Limiting** - Built-in API protection
- **Safe Execution** - AST-based calculations, sandboxed Python execution

## Use Cases

- **Personal Assistant** - Remembers preferences and context
- **Research Sessions** - Wikipedia + ArXiv + web search with memory
- **Learning Sessions** - Builds on previous explanations
- **Data Analysis** - Python execution + calculations with context
- **Financial Analysis** - Price lookup with contextual calculations
- **Educational Tool** - Math + programming + research with conversation context
- **Academic Research** - ArXiv search + Wikipedia + Python analysis

## Architecture Deep Dive

For detailed information about the LangChain agent implementation, see [`agent/README.md`](agent/README.md) which covers:
- ReAct pattern implementation
- LangChain vs custom agent differences
- Component breakdown and execution flow
- Tool architecture and selection logic
- Memory management strategies
- Error handling and debugging
- Extension points and best practices 