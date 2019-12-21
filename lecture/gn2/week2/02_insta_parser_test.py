from libs.instaParser import parse

pageString = open("insta.html", encoding="utf-8").read()

links = parse(pageString)
print(links)