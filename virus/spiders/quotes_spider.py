import scrapy


class QuotesSpider(scrapy.Spider):
    # must be unique
    name = "quotes"

    # 返回可迭代Request对象
    # 会自动爬取生成的URL
    def start_requests(self):
        # urls = [
        #     "http://quotes.toscrape.com/page/" + str(item) + "/"
        #     for item in range(1,20)
        # ]
        #
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)
        #
        for item in range(1, 20):
            yield scrapy.Request(url="http://quotes.toscrape.com/page/" + str(item) + "/", callback=self.parse)

    # 解析Request，可选的返回新的Request以待解析
    # 这样就形成了爬虫链
    def parse(self, response, **kwargs):
        page = response.url.split("/")[-2]
        filename = f"target/example/quotes-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
