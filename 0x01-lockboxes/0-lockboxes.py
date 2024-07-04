#!/usr/bin/python3
'''
lockboxe
'''

def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key < n and not opened[new_key]:
                opened[new_key] = True
                keys.append(new_key)
    
    return all(opened)

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
