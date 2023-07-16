def hide(text: str, public_len: int = 5, cover: str = '*') -> str:
    if not isinstance(text, str):
        raise TypeError("Text must be of str type")

    text_len = len(text)
    cover_len = text_len - public_len

    if cover_len > 0:
        return text[:public_len] + cover * cover_len

    return text
