"""LangChain agent implementation using custom Gemini LLM."""

from typing import List
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from llm.langchain_adapter import LangChainGeminiAdapter
from tools.langchain_tools import LANGCHAIN_TOOLS


class LangChainAgent:
    """Q&A agent using LangChain with custom Gemini LLM."""
    
    def __init__(self, gemini_api_key: str):
        """Initialize the LangChain agent."""
        # Create custom LLM adapter
        self.llm = LangChainGeminiAdapter(api_key=gemini_api_key)
        
        # Create agent prompt template
        self.prompt = PromptTemplate.from_template(
            """
You are a helpful assistant that can use tools to answer questions.

TOOLS:
------
You have access to the following tools:

{tools}

To use a tool, please use the following format:

```
Thought: Do I need to use a tool? What tool should I use?
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

Question: {input}
Thought: {agent_scratchpad}
"""
        )
        
        # Create ReAct agent
        self.agent = create_react_agent(
            llm=self.llm,
            tools=LANGCHAIN_TOOLS,
            prompt=self.prompt
        )
        
        # Create agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=LANGCHAIN_TOOLS,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3
        )
    
    def answer_question(self, question: str) -> str:
        """Answer a question using the LangChain agent."""
        try:
            response = self.agent_executor.invoke({"input": question})
            return response["output"]
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}" 