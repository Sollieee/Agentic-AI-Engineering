
from agents import Agent, ToolCallItem
from guardrails.agricultural_guardrails import validate_user_input

def get_called_tools(run_items):
    """Return the names of tools called during an agent run."""
    return [
        item.tool_name
        for item in run_items
        if isinstance(item, ToolCallItem) and item.tool_name is not None
    ]


def test_get_called_tools_identifies_farming_advisor():
    test_agent = Agent(
        name="Test Agent",
        instructions="This agent is only used for testing.",
    )

    simulated_run_items = [
        ToolCallItem(
            agent=test_agent,
            raw_item={
                "name": "farming_advisor",
                "call_id": "test-call-1",
                "type": "function_call",
                "arguments": "{}",
            },
        )
    ]

    called_tools = get_called_tools(simulated_run_items)

    assert called_tools == ["farming_advisor"]


def test_get_called_tools_ignores_non_tool_items():
    test_agent = Agent(
        name="Test Agent",
        instructions="This agent is only used for testing.",
    )

    simulated_run_items = [
        ToolCallItem(
            agent=test_agent,
            raw_item={
                "name": "farming_advisor",
                "call_id": "test-call-1",
                "type": "function_call",
                "arguments": "{}",
            },
        ),
        "This is an ordinary message, not a tool call.",
    ]

    called_tools = get_called_tools(simulated_run_items)

    assert called_tools == ["farming_advisor"]






def test_rejects_empty_input():
    is_valid, message = validate_user_input("")

    assert is_valid is False
    assert "enter a question" in message.lower()


def test_rejects_whitespace_input():
    is_valid, message = validate_user_input("   ")

    assert is_valid is False


def test_rejects_oversized_input():
    long_message = "a" * 5001

    is_valid, message = validate_user_input(long_message)

    assert is_valid is False
    assert "too long" in message.lower()


def test_accepts_valid_input():
    user_message = "How do I improve maize production?"

    is_valid, cleaned_message = validate_user_input(user_message)

    assert is_valid is True
    assert cleaned_message == user_message


def test_strips_extra_whitespace():
    is_valid, cleaned_message = validate_user_input(
        "  How do I care for poultry?  "
    )

    assert is_valid is True
    assert cleaned_message == "How do I care for poultry?"
