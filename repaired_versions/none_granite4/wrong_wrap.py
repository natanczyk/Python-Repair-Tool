def wrap(text, cols):
    lines = []
    while len(text) > cols:
        # Find the last space within the first cols+1 characters
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            # No space found, must break the word
            end = cols
        line, text = text[:end], text[end:]
        lines.append(line)

    # Append any remaining text (could be empty)
    if text:
        lines.append(text)

    return lines