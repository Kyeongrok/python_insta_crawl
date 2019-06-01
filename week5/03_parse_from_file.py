from libs.coupang.subpageParser import parse

# 파일 읽기
file = open("./pages/0.html", encoding="utf-8")
pageString = file.read()
file.close()

print(pageString)

productInfo = parse(pageString)
print(productInfo)
