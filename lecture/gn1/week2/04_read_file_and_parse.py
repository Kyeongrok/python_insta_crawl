from libs.instagram.parser import parse
file = open("./insta운동스타그램.html", encoding="utf-8")

pageString = file.read()
posts = parse(pageString)
print(posts)
