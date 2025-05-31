# 🦜 LangChain Q&A Agent with Custom Gemini LLM

A clean question-answer agent built with **LangChain framework** using a custom Gemini LLM wrapper that has exactly 3 methods. This implementation uses proper LangChain agent orchestration with ReAct pattern for dynamic tool selection.

## ✨ Features

- **🦜 LangChain Framework** - Proper agent orchestration using AgentExecutor
- **🧠 Custom 3-Method Gemini LLM** with exactly these operations:
  - `text_to_text()` - Basic text completion
  - `text_to_json()` - Structured JSON responses  
  - `text_to_function_call()` - Function calling capabilities
- **🤖 ReAct Agent Pattern** - Reasoning and acting with tools
- **⚡ Dynamic Tool Selection** - Automatic tool orchestration
- **🔧 LangChain Tools** - Properly integrated tools

## 🛠️ Tools Available

- 🔍 **Web Search** - DuckDuckGo internet search
- 🧮 **Calculator** - Mathematical operations
- 📅 **Date/Time** - Current date and time information

## 🏗️ Clean Project Structure

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
│   ├── langchain_agent.py    # LangChain agent with ReAct
│   └── __init__.py
├── main.py                   # CLI interface
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

## 🚀 Quick Start

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Set your Gemini API key**:
```bash
# Create a .env file
echo "GEMINI_API_KEY=your_actual_gemini_api_key" > .env
```

3. **Run the LangChain agent**:
```bash
python main.py
```

## 💡 Example Interactions

### **Simple Questions**
```
❓ User: "What is 2 + 2?"
🤖 Agent: Uses calculator tool → "Result: 4"
```

### **Web Search**
```
❓ User: "What is the current Bitcoin price?"
🤖 Agent: Uses web search → Current price information
```

### **Complex Multi-Tool**
```
❓ User: "Current Bitcoin price and what's 10% of that amount"
🤖 Agent: 
  1. Searches for Bitcoin price
  2. Extracts the price value
  3. Calculates 10% using calculator
  4. Provides comprehensive answer
```

## 🧠 Custom LLM Architecture

### **3-Method Constraint**
The `CustomGeminiLLM` wrapper implements exactly these methods:

```python
class CustomGeminiLLM:
    def text_to_text(self, prompt: str) -> str:
        """Basic text completion with 1-second rate limiting"""
        
    def text_to_json(self, prompt: str, schema: dict) -> dict:
        """Structured JSON response with schema validation"""
        
    def text_to_function_call(self, prompt: str, functions: List[dict]) -> dict:
        """Function calling in Vertex AI style"""
```

### **LangChain Integration**
The `LangChainGeminiAdapter` wraps the custom LLM to work with LangChain:

```python
class LangChainGeminiAdapter(LLM):
    def _call(self, prompt: str, **kwargs) -> str:
        """LangChain-compatible interface"""
        return self.custom_llm.text_to_text(prompt)
```

## 🤖 Agent Behavior

### **ReAct Pattern**
The agent follows the Reasoning-Acting pattern:

1. **Thought** - Analyze what needs to be done
2. **Action** - Select appropriate tool
3. **Observation** - Process tool results
4. **Final Answer** - Provide comprehensive response

### **Tool Selection Logic**
- Automatic tool selection based on question analysis
- Proper error handling and fallback
- Context preservation between tool calls

## 🔧 Technical Details

### **Rate Limiting**
- 1-second sleep between Gemini API calls
- Prevents API quota exhaustion

### **Error Handling**
- Graceful tool failure handling
- Parse error recovery in LangChain
- User-friendly error messages

### **Tool Integration**
- LangChain-compatible tool wrappers
- Proper input validation with Pydantic
- Structured tool responses

## 📋 Dependencies

- `langchain>=0.1.0` - Main framework
- `langchain-core>=0.1.0` - Core LangChain components
- `langchain-community>=0.0.10` - Community tools
- `google-generativeai>=0.3.0` - Gemini API
- `duckduckgo-search>=4.0.0` - Web search
- `python-dotenv>=1.0.0` - Environment variables
- `pydantic>=2.0.0` - Data validation

## 🎯 Key Advantages

### **Clean Architecture**
- ✅ **Minimal Dependencies** - Only essential files
- ✅ **Separation of Concerns** - Clear module boundaries
- ✅ **Maintainable Code** - Simple, focused components
- ✅ **Easy Testing** - Modular design

### **LangChain Benefits**
- ✅ **Proper Agent Orchestration** - Built-in agent patterns
- ✅ **Tool Management** - Standardized tool interface
- ✅ **Error Handling** - Robust error recovery
- ✅ **Extensibility** - Easy to add new tools

### **Custom LLM Benefits**
- ✅ **Rate Limiting** - Built-in API protection
- ✅ **3-Method Constraint** - Simplified interface
- ✅ **Structured Outputs** - Reliable JSON responses
- ✅ **Function Calling** - Tool parameter extraction

## 🔒 Security

- **Safe Calculations** - AST-based expression evaluation
- **Input Validation** - Pydantic schema validation
- **API Protection** - Rate limiting and error handling
- **No Code Execution** - Safe tool implementations

## 🎪 Use Cases

- **Research Assistant** - Web search + calculations
- **Financial Analysis** - Price lookup + percentage calculations  
- **General Q&A** - Mixed tool usage based on question type
- **Educational Tool** - Math problems with current data

## 🧹 Clean Implementation

This project has been thoroughly cleaned to include only:
- **Essential files** for the LangChain agent
- **Custom 3-method Gemini LLM** implementation
- **Core tools** (web search, calculator, datetime)
- **No legacy code** or unused components

The result is a minimal, maintainable codebase focused on the core functionality. 