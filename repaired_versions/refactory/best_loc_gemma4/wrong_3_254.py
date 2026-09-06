def remove_extras(lst):
    def helper(remaining, seen):
        if not remaining:
            return []
        first = remaining[0]
        if first in seen:
            return helper(remaining[1:], seen)
        else:
            seen.append(first)
            return [first] + helper(remaining[1:], seen)
    
    return helper(lst, [])