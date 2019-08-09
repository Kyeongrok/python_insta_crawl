from naver_cafe.parser.cafeBoardSearchParser import parse

file = open("./gamgiLast.html")
pageString = file.read()
list = parse(pageString)