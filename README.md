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

## Available Tools

- **Web Search** - DuckDuckGo internet search
- **Calculator** - Mathematical operations
- **Date/Time** - Current date and time information

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
├── llm/
│   ├── custom_gemini.py      # Custom 3-method Gemini LLM
│   ├── langchain_adapter.py  # LangChain LLM adapter
│   ├── schemas.py            # JSON schemas
│   └── __init__.py
├── tools/
│   ├── web_search.py         # DuckDuckGo search tool
│   ├── calculator.py         # Math operations tool
│   ├── datetime_tool.py      # Date/time tool
│   ├── langchain_tools.py    # LangChain tool wrappers
│   └── __init__.py
├── agent/
│   ├── langchain_agent.py    # LangChain agent with ReAct + Memory
│   └── __init__.py
├── main.py                   # CLI interface
├── requirements.txt          # Dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Quick Start

1. **Install dependencies**:
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

4. **Test memory functionality**:
```bash
python test_memory.py
```

## Example Usage

### Context Retention
```
User: "Remember that my name is Sam and I love Python"
Agent: "I'll remember that your name is Sam and you love Python programming!"

User: "What programming language do I love?"
Agent: "Based on our conversation, you love Python programming!"
```

### Sequential Questions
```
User: "What is the current Bitcoin price?"
Agent: "Bitcoin is currently $43,250"

User: "Calculate 15% of that amount"
Agent: "15% of $43,250 (the Bitcoin price from earlier) is $6,487.50"
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
- `google-generativeai>=0.3.0` - Gemini API
- `duckduckgo-search>=4.0.0` - Web search
- `python-dotenv>=1.0.0` - Environment variables
- `pydantic>=2.0.0` - Data validation

## Key Benefits

- **Context Continuity** - Natural conversation flow
- **Reference Resolution** - Handles "that", "it", "the previous result"
- **User Preferences** - Remembers user information
- **Session Management** - Clean conversation boundaries
- **Clean Architecture** - Minimal dependencies, clear module boundaries
- **Rate Limiting** - Built-in API protection
- **Safe Execution** - AST-based calculations, no code execution

## Use Cases

- **Personal Assistant** - Remembers preferences and context
- **Research Sessions** - Maintains research context across queries
- **Learning Sessions** - Builds on previous explanations
- **Data Analysis** - References previous calculations/searches
- **Financial Analysis** - Price lookup with contextual calculations
- **Educational Tool** - Math problems with conversation context 