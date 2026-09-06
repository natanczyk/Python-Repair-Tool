def hanoi(height, start=1, end=3):
    steps = []
    if height > 0:
        # Calculate the helper peg by subtracting start and end from the set of all pegs
        helper = ({1, 2, 3} - {start, end}).pop()
        
        # Step 1: Move height-1 disks from start to helper
        steps.extend(hanoi(height - 1, start, helper))
        
        # Step 2: Move the largest disk from start to end
        # The test cases expect lists [start, end] instead of tuples (start, end)
        steps.append([start, end])
        
        # Step 3: Move height-1 disks from helper to end
        steps.extend(hanoi(height - 1, helper, end))

    return steps