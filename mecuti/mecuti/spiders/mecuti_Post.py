import scrapy

from mecuti.items import MecutiItem

class MecutiPost(scrapy.Spider):
	name = 'posts'

	def start_requests(self):
		urls = [
			'http://mecuti.vn/',
			# 'http://mecuti.vn/page/10',
			# 'http://mecuti.vn/hai-tran-thanh-minh-nhi-2015-so-do-voi-banh-beo.html'
		]

		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		posts = response.css('div.type-post')

		for post in posts:
			item = MecutiItem()
			item['title'] = post.css('.post-title a::text').extract_first()
			item['url'] = post.css('.post-title a::attr(href)').extract_first()

			yield scrapy.Request(url = item['url'], callback = self.parse_detail, meta={'item': item})

		pagi = response.css('div.pagination a.next.page-numbers::attr(href)').extract_first()

		if pagi:
			arrPagi = pagi.split('/')
			numPage = arrPagi[len(arrPagi)-1]

			# yield scrapy.Request(url = pagi, callback=self.parse)
			if int(numPage) <= 10:
				yield scrapy.Request(url = pagi, callback=self.parse)

	def parse_detail(self, response):
		post = response.css('div.post.single')
		item = response.meta.get('item')
		item['content'] = '\n'.join(post.css('.post-content').extract())
		yield item