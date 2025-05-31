"""LangChain agent implementation using custom Gemini LLM with conversation memory."""

from typing import List, Optional
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage, AIMessage
from llm.langchain_adapter import LangChainGeminiAdapter
from tools.langchain_tools import LANGCHAIN_TOOLS
from prompts.agent_prompts import REACT_AGENT_PROMPT


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
        
        # Use centralized prompt from prompts directory
        self.prompt = REACT_AGENT_PROMPT
        
        # Create ReAct agent
        self.agent = create_react_agent(
            llm=self.llm,
            tools=LANGCHAIN_TOOLS,
            prompt=self.prompt
        )
        
        # Create agent executor with memory and better error handling
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=LANGCHAIN_TOOLS,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors="Check your output and make sure it conforms to the expected format. Only provide ONE action per response, never both Action and Final Answer together.",
            max_iterations=2,
            return_intermediate_steps=False
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