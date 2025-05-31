"""Agent prompt templates."""

from langchain_core.prompts import PromptTemplate

# Main ReAct agent prompt with conversation memory
REACT_AGENT_PROMPT = PromptTemplate.from_template(
    """
You are a helpful assistant that can use tools to answer questions. You have access to our conversation history.

CONVERSATION HISTORY:
{chat_history}

TOOLS:
------
You have access to the following tools:

{tools}

Use the following format EXACTLY:

Thought: Do I need to use a tool? What tool should I use? Consider our conversation history.
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: Do I need to use a tool? No
Final Answer: [your response here]

OR if no tools are needed:

Thought: Do I need to use a tool? No
Final Answer: [your response here]

IMPORTANT: 
- Only provide ONE action per response
- NEVER include both Action and Final Answer in the same response
- After each Action, wait for the Observation before continuing
- Only use Final Answer when you have all the information needed

Begin!

Current Question: {input}
Thought: {agent_scratchpad}
"""
)

# Simple agent prompt without memory (for future use)
SIMPLE_AGENT_PROMPT = PromptTemplate.from_template(
    """
You are a helpful assistant that can use tools to answer questions.

TOOLS:
------
You have access to the following tools:

{tools}

Use the following format EXACTLY:

Thought: Do I need to use a tool? What tool should I use?
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: Do I need to use a tool? No
Final Answer: [your response here]

OR if no tools are needed:

Thought: Do I need to use a tool? No
Final Answer: [your response here]

IMPORTANT: 
- Only provide ONE action per response
- NEVER include both Action and Final Answer in the same response
- After each Action, wait for the Observation before continuing
- Only use Final Answer when you have all the information needed

Begin!

Question: {input}
Thought: {agent_scratchpad}
"""
) 