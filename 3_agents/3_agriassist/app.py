
from pathlib import Path

import gradio as gr

from agents import Runner, set_default_openai_key
from config import OPENAI_API_KEY
from agent_modules.orchestrator import agriassist_agent
from guardrails.agricultural_guardrails import validate_user_input


set_default_openai_key(OPENAI_API_KEY)

# Load the stylesheet from the static folder.
PROJECT_DIR = Path(__file__).resolve().parent
CSS_FILE = PROJECT_DIR / "static" / "style.css"

with open(CSS_FILE, encoding="utf-8") as file:
    AGRIASSIST_CSS = file.read()


async def chat(message, history):
    is_valid, validation_result = validate_user_input(message)

    if not is_valid:
        return validation_result

    conversation = [
        {
            "role": item["role"],
            "content": item["content"],
        }
        for item in history
        if item.get("role") in ("user", "assistant")
        and isinstance(item.get("content"), str)
    ]

    conversation.append({
        "role": "user",
        "content": validation_result,
    })

    try:
        result = await Runner.run(
            agriassist_agent,
            conversation,
        )
        return result.final_output

    except Exception:
        print("AgriAssist encountered an error.")
        return (
            "Sorry, AgriAssist couldn't process your request. "
            "Please try again."
        )



with gr.Blocks() as demo:
    gr.Markdown(
        """
        # AgriAssist
        ### Practical agricultural support, powered by AI

        Get help with crop production, crop health, livestock,
        farm business and agricultural support.
        """
    )

    gr.ChatInterface(
        fn=chat,
        chatbot=gr.Chatbot(height=460),
        textbox=gr.Textbox(
            placeholder="Ask AgriAssist about your farm...",
            lines=2,
        ),
        examples=[
            "How should I prepare my land for maize planting?",
            "My maize leaves are turning yellow. What could be wrong?",
            "My chickens are weak and eating less. What should I do?",
            "Help me estimate a fertilizer budget for my farm.",
            "My poultry feed delivery has been delayed. What should I do?",
        ],
    )


if __name__ == "__main__":
    demo.launch(css=AGRIASSIST_CSS)
