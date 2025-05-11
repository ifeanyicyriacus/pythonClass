def circle_arrangement(text1) -> [str]:
    new_arrangements = [text1]
    n = len(text1)

    while n > 0:
        temp = text1[1:] + text1[0]
        new_arrangements.append(temp)
        text1 = temp
        n -= 1
    return new_arrangements


def breakfast(text1: str, text2: str) -> bool:
    if text2 in circle_arrangement(text1):
        return True
    else:
        return False
