from libs.patternMatchedTextGetter import getMatchedText

# 파일에서 text 불러오기
file = open("cell.txt")
text = file.read()

result = getMatchedText("셀트리온.{1}", text)
print(result)
print(len(result))
