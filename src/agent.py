# Google ADK Agent — Google Search Example

This uses [Google’s Agent Development Kit (ADK)](https://google.github.io/adk-docs/get-started/quickstart/) to create a basic Python agent that responds to user queries with Google Search results.

## 1. Install ADK

```bash
pip install google-adk
```

## 2. Python Example: Question-Answering Agent with Google Search

```python
from adk.agent import Agent
from adk.actions import WebSearch

class GoogleSearchAgent(Agent):
    def __init__(self):
        super().__init__(name="Google Search Agent")

        # Add a search action, e.g., via Google or Bing
        self.add_action(WebSearch(engine="google"))

    def handle(self, message):
        # Simple echo if not a question
        if not message.endswith("?"):
            return "Ask me a question and I'll Google it for you!"

        # Use web search to answer the question
        results = self.act("web_search", query=message)
        if results and "items" in results:
            top_result = results["items"][0]
            return f"Top Google result for '{message}':\n{top_result['title']}\n{top_result['link']}"
        return "Sorry, I couldn't find any results."

if __name__ == "__main__":
    agent = GoogleSearchAgent()
    while True:
        user_input = input("Ask me anything: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        print(agent.handle(user_input))
```

## 3. Usage
1. Run the script.
2. Type in a question, e.g. “What is the tallest mountain?”.
3. The agent replies with the top Google Search result.

---

**References:**
- [Google ADK Quickstart](https://google.github.io/adk-docs/get-started/quickstart/)
- [Official ADK Python API](https://google.github.io/adk-docs/get-started/python/)

**Note:**  
Check ADK documentation for more advanced usage, authentication, or API key requirements for the WebSearch action.
