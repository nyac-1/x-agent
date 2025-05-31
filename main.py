"""Main CLI interface for the LangChain Q&A Agent."""

import os
from dotenv import load_dotenv
from agent.langchain_agent import LangChainAgent


def main():
    """Main CLI interface."""
    print("🦜 LangChain Q&A Agent with Custom Gemini LLM")
    print("=" * 50)
    
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
        
        print("\n💡 Example queries:")
        print("• 'What is the current Bitcoin price?'")
        print("• 'Calculate 15% of 50000'")
        print("• 'What time is it now?'")
        print("• 'Current Bitcoin price and what's 10% of that amount'")
        
        print("\nType 'quit' or 'exit' to stop the agent.")
        print("-" * 50)
        
        # Main interaction loop
        while True:
            try:
                question = input("\n❓ Ask me anything: ").strip()
                
                if question.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if not question:
                    continue
                
                print("\n🤔 LangChain Agent thinking...")
                answer = agent.answer_question(question)
                print(f"\n🤖 Answer: {answer}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                
    except Exception as e:
        print(f"❌ Failed to initialize LangChain agent: {str(e)}")


if __name__ == "__main__":
    main() 