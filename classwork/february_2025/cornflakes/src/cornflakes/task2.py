def swap_and_join(textList:tuple) -> str :
    result = ""
    for i in range (len(textList)-1, -1, -1):
        result += textList[i]+ " "
    return result.strip()