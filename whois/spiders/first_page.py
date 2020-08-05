import scrapy


class QuotesSpider(scrapy.Spider):
    name = "a"

    def start_requests(self):
        urls = [
            'http://tmsearch.uspto.gov/bin/gate.exe?f=tess&state=4804:4gxlh5.1.1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'a-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('http://tmsearch.uspto.gov/')
# link = driver.find_element_by_link_text('Basic Word Mark Search (New User)')
# link.click()
# radios = driver.find_elements_by_name('p_s_PARA1')
# radios[1].click()
# search = driver.find_element_by_name('p_s_PARA2')
# search.send_keys(name)
# submit = driver.find_elements_by_name('a_search')[1]
# submit.click()

# try:
#     TSDRs = driver.find_elements_by_link_text('TSDR')
#     TSDRs[0].click()
# except:
#     driver.delete_all_cookies()
#     driver.close()
#     driver.quit()
#     return(f'{name}\nThere\'s no such domain\n--------------------------')