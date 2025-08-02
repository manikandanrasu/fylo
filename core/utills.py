import re

def refine_text(user_input:str) -> str:
    text = user_input.strip()
    clean_text = re.sub(r"\s+", " ", text)

    base = f"User idea: '{clean_text}'"

    instructions = (
        "You are an AI assistent from this idea, generate the following:\n"
        "1. A catchy project title (5-7 words max).\n"
        "2. Abstract: 2-3 sentences explaining what the project does and who it server.\n"
        "3.Tools and technologies needed (list, beginner-friendly, with brief reason for each).\n"
        "4.Three concrete use cases with one sentence description.\n"
        "Format the output as JSON with keys: title, abstract, tools, use_cases, next_step."
    )

    if len(clean_text.split()) < 5:
        prompt = (
            f"I have a small idea: '{clean_text}'.'{instructions}'"
            "If the idea is ambiguous, expand it into a sensible project."
        )

    else: 
        prompt = f"{base}\n{instructions}"

    return prompt