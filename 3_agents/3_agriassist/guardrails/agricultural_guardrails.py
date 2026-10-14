
MAX_INPUT_LENGTH = 5000


def validate_user_input(user_input: str) -> tuple[bool, str]:
    """Validate a user's message before sending it to AgriAssist."""

    if not isinstance(user_input, str):
        return False, "Your message must be text."

    cleaned_input = user_input.strip()

    if not cleaned_input:
        return False, "Please enter a question or describe your agricultural problem."

    if len(cleaned_input) > MAX_INPUT_LENGTH:
        return (
            False,
            f"Your message is too long. Please keep it under {MAX_INPUT_LENGTH} characters.",
        )

    return True, cleaned_input
