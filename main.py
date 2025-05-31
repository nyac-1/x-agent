"""Main CLI interface for the LangChain Q&A Agent with conversation memory."""

import os
from dotenv import load_dotenv
from agent.langchain_agent import LangChainAgent


def print_help():
    """Print available commands."""
    print("\n📋 Available Commands:")
    print("• Ask any question (the agent will remember context)")
    print("• 'help' - Show this help message")
    print("• 'history' - Show conversation history")
    print("• 'clear' - Clear conversation history")
    print("• 'new' - Start a new conversation (clears history)")
    print("• 'quit' or 'exit' - End the session")


def main():
    """Main CLI interface with conversation memory management."""
    print("🦜 LangChain Q&A Agent with Custom Gemini LLM + Memory")
    print("=" * 55)
    
    # Load environment variables
    load_dotenv()
    
    # Get Gemini API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable not set.")
        print("Please set your Gemini API key in a .env file or as an environment variable.")
        return
    
    # Initialize LangChain agent
    try:
        agent = LangChainAgent(api_key)
        print("✅ LangChain Agent initialized successfully!")
        print("\n🛠️ Available tools:")
        print("• 🔍 Web Search (DuckDuckGo)")
        print("• 🧮 Calculator") 
        print("• 📅 Date/Time")
        
        print("\n🦜 LangChain Features:")
        print("• 🤖 ReAct agent pattern")
        print("• 🔧 Tool orchestration")
        print("• 🧠 Custom 3-method Gemini LLM")
        print("• ⚡ Automatic tool selection")
        print("• 💭 Conversation memory")
        
        print("\n💡 Example queries:")
        print("• 'What is the current Bitcoin price?'")
        print("• 'Calculate 15% of that amount' (refers to previous answer)")
        print("• 'What time is it now?'")
        print("• 'Remember that I like Python programming'")
        
        # Initialize conversation
        agent.init_conversation()
        
        print_help()
        print("-" * 55)
        
        # Main interaction loop
        while True:
            try:
                question = input("\n❓ Ask me anything: ").strip()
                
                # Handle special commands
                if question.lower() in ['quit', 'exit', 'q']:
                    agent.end_conversation()
                    print("👋 Goodbye!")
                    break
                
                elif question.lower() in ['help', 'h']:
                    print_help()
                    continue
                
                elif question.lower() in ['history', 'hist']:
                    agent.show_conversation_history()
                    continue
                
                elif question.lower() in ['clear', 'reset']:
                    agent.end_conversation()
                    agent.init_conversation()
                    print("🔄 Conversation history cleared and reinitialized!")
                    continue
                
                elif question.lower() in ['new', 'restart']:
                    agent.end_conversation()
                    agent.init_conversation()
                    print("🆕 New conversation started!")
                    continue
                
                if not question:
                    continue
                
                print("\n🤔 LangChain Agent thinking (with memory)...")
                answer = agent.answer_question(question)
                print(f"\n🤖 Answer: {answer}")
                
            except KeyboardInterrupt:
                print("\n\n🧠 Ending conversation...")
                agent.end_conversation()
                print("👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                
    except Exception as e:
        print(f"❌ Failed to initialize LangChain agent: {str(e)}")


if __name__ == "__main__":
    main() 