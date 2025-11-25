import re

invite_regex = re.compile(r"(https?://t\.me/\S+)")

def extract_invite_link(text: str):
    match = invite_regex.search(text)
    return match.group(1) if match else None