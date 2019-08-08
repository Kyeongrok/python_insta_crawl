from naver_cafe.parser.cafeBoardSearchParser import parse

file = open("./joonggonara_gamgi.html")
pageString = file.read()
list = parse(pageString)