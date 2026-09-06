def wrap(text, cols):
    lines = []
    while len(text) > cols:
        # Find the last space within the first cols+1 characters
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            # No space found: must break the word
            end = cols
        # The line is everything up to (but not including) the space at position end
        line, text = text[:end], text[end:]
        lines.append(line)

    # Append any remaining text (including any leading spaces)
    if text:
        lines.append(text)
    return lines