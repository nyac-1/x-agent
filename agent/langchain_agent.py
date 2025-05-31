"""LangChain agent implementation using custom Gemini LLM with conversation memory."""

from typing import List, Optional
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage, AIMessage
from llm.langchain_adapter import LangChainGeminiAdapter
from tools.langchain_tools import LANGCHAIN_TOOLS


class LangChainAgent:
    """Q&A agent using LangChain with custom Gemini LLM and conversation memory."""
    
    def __init__(self, gemini_api_key: str):
        """Initialize the LangChain agent with conversation memory."""
        # Create custom LLM adapter
        self.llm = LangChainGeminiAdapter(api_key=gemini_api_key)
        
        # Initialize conversation memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="output"
        )
        
        # Create agent prompt template with memory
        self.prompt = PromptTemplate.from_template(
            """
You are a helpful assistant that can use tools to answer questions. You have access to our conversation history.

CONVERSATION HISTORY:
{chat_history}

TOOLS:
------
You have access to the following tools:

{tools}

To use a tool, please use the following format:

```
Thought: Do I need to use a tool? What tool should I use? Consider our conversation history.
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```

Begin!

Current Question: {input}
Thought: {agent_scratchpad}
"""
        )
        
        # Create ReAct agent
        self.agent = create_react_agent(
            llm=self.llm,
            tools=LANGCHAIN_TOOLS,
            prompt=self.prompt
        )
        
        # Create agent executor with memory
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=LANGCHAIN_TOOLS,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3
        )
    
    def init_conversation(self) -> None:
        """Initialize a new conversation by clearing memory."""
        self.memory.clear()
        print("🧠 Conversation history initialized (memory cleared)")
    
    def end_conversation(self) -> None:
        """End the conversation by clearing memory."""
        self.memory.clear()
        print("🧠 Conversation history cleared")
    
    def get_conversation_history(self) -> List[str]:
        """Get the current conversation history as a list of strings."""
        messages = self.memory.chat_memory.messages
        history = []
        for message in messages:
            if isinstance(message, HumanMessage):
                history.append(f"Human: {message.content}")
            elif isinstance(message, AIMessage):
                history.append(f"Assistant: {message.content}")
        return history
    
    def show_conversation_history(self) -> None:
        """Display the current conversation history."""
        history = self.get_conversation_history()
        if not history:
            print("📝 No conversation history yet")
            return
        
        print("📝 Conversation History:")
        print("-" * 40)
        for entry in history:
            print(f"  {entry}")
        print("-" * 40)
    
    def answer_question(self, question: str) -> str:
        """Answer a question using the LangChain agent with memory."""
        try:
            response = self.agent_executor.invoke({"input": question})
            return response["output"]
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}" 