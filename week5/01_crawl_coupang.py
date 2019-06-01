from libs.crawler import crawl

url = "https://www.coupang.com/np/search?q=%EC%8D%AC%EA%B8%80%EB%9D%BC%EC%8A%A4&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=72&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken="
pageString = crawl(url)

print(pageString)