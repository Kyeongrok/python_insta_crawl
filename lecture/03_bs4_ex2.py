pageString = '''

<html>
    <head>
        <title>hello python</title>
    </head>
    <body>
        <div>nice to meet you</div>
        <div class="message">Dear god, I need your help</div>
        
        <ul class="post_list">
            <li class="post_type1">yesterday, i fixed my iphone.</li>
            <li class="post_type1">today, i suffered hard from python.</li>
        </ul>
    </body>
</html>
'''

from bs4 import BeautifulSoup
def parse(pageString):
    bsobj = BeautifulSoup(pageString, "html.parser")
    message = bsobj.find("div", {"class":"message"})
    print(message.text)

    lis = bsobj.findAll("li")
    for li in lis:
        print(li.text)

    # 두개 동시에 뽑기 yesterday, today


parse(pageString)