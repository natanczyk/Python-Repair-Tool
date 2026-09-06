def wrap(text, cols):
    lines = []
    while len(text) > cols:
        # Find the last space within the allowed range
        end = text.rfind(' ', 0, cols + 1)
        if end == -1:
            # No space found, break at column limit
            end = cols
        else:
            # Ensure we don't break at exactly the column limit if it would create a line longer than cols
            if end >= len(text):
                end = len(text)
        
        # Extract the line and remaining text
        line = text[:end]
        remaining = text[end:]
        
        # Handle whitespace properly
        lines.append(line)
        text = remaining
        
        # If we're at the end and there's no more text, break
        if not text:
            break
    
    # Add the remaining text as the last line
    if text:
        lines.append(text)
    
    return lines