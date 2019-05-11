import re

def getMatchedText(pattern, text):
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        result.append(match)
    return result
