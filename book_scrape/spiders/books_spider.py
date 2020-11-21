# install scrapy with conda than pip in the spiders folder
# pip install twisted[tls]
# this should be if import prob

# to make html file type (scrapy crawl books)

# scrapy shell <url>
# response
# response.css(*"a")
# response.css("a")[0]
# len(response.css("a"))
# response.css("article")
# response.css("article.product_pod")
# response.css("article.product_pod h3")
# response.css("article.product_pod h3 a") find product_pod class in article element and find child h3 which has child a
# response.css("article.product_pod h3 a::text")
# response.css("article.product_pod h3 a::text").get()
# response.css("article.product_pod h3 a::text").getall()
# response.css("article.product_pod h3 a::attr(href)"").get()
# response.css("article.product_pod h3 a::attr(title)").getall()

# scrapy crawl books -o books.json
import scrapy

print(scrapy.__version__)
print(dir(scrapy)) # shows all classes available

class BooksSpider(scrapy.Spider):
    # if I have start_urls class attribute and parse method no need of start_requests instance method
    name = "books"
    start_urls = [
        "http://books.toscrape.com"
    ]

    # def start_requests(self):
    #     return [
    #         scrapy.Request(url = "http://books.toscrape.com", callback = self.parse)
    #     ]

    def parse(self, response):
       for entry in response.css("article.product_pod"):
           title = entry.css("h3 a::attr(title)").get()
           price = entry.css("p.price_color::text").get()
           yield {"title": title, "price": price}

       next_page = response.css("li.next a::attr(href)").get()

       if next_page is not None:
           next_page_url = response.urljoin(next_page) 
           yield scrapy.Request(url = next_page_url, callback = self.parse)


        # titles = response.css("article.product_pod h3 a::attr(title)").getall()
        # prices = response.css("article.product_pod p.price_color::text").getall()
        # for title in titles:
        #     # yield for buffering not to load everything once
        #     yield {
        #         "title": title
        #     }

        # b means the file format coming is binary so we want to write it
        # with open("books.html", "wb") as file:
        #     file.write(response.body)




