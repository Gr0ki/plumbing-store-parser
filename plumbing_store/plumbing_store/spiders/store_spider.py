import scrapy
from bs4 import BeautifulSoup


class StoreSpiderSpider(scrapy.Spider):
    name = 'store_spider'
    allowed_domains = ['best-dim.com']

    def start_requests(self):
        url = 'https://best-dim.com/ua/g4861238-santehnika'
        yield scrapy.Request(url, self.parse_categories)

    def parse_categories(self, response):
        category_urls = [
            'https://best-dim.com' + e.get() + '?product_items_per_page=48' for e in response.css(
                'a.b-product-groups-gallery__image-link::attr(href)'
            )
        ]

        for category_url in category_urls:
            yield response.follow(category_url, callback=self.parse_category)

    def parse_category(self, response):
        products_urls = [
            item for item in response.css('a.b-centered-image.b-product-line__image-wrapper::attr(href)').getall()
        ]
        for product_url in products_urls:
            yield response.follow(product_url, callback=self.parse)

        next_page = response.css('a.b-pager__link.b-pager__link_pos_last::attr(href)').get()
        if next_page:
            next_page = 'https://best-dim.com' + next_page + '?product_items_per_page=48'
            yield response.follow(next_page, callback=self.parse_category)

    def parse(self, response):
        product_image_url = response.css('img.b-centered-image__img::attr(src)').get()

        try:
            product_code = response.css('span.b-product__sku::text').get()[5:]
        except BaseException:
            product_code = ''

        product_name = response.css('h1.b-title::text').get()

        product_status = response.css('span.b-product__state.b-product__state_type_available::text').get()

        product_prise = response.css('li.b-order-info__item::text').getall()[1].strip().replace('\xa0', '').replace(',', '')

        product_specifications = [
            elem.strip() for elem in response.css('td.b-product-info__cell::text').getall() if elem.strip()
        ]

        product_description = response.css('div.b-content__body.b-user-content').get()
        soup = BeautifulSoup(product_description)
        product_description = [i.get_text() for i in soup.find_all(string=True) if i.get_text()]
        product_description = ' '.join(product_description[:len(product_description) - 1]).replace('\xa0', '').replace('\n', ' ')

        product_info = {
            'product image url': product_image_url,
            'product code': product_code,
            'product name': product_name,
            'product status': product_status,
            'product prise': product_prise,
        }
        for i in range(0, len(product_specifications), 2):
            product_info[product_specifications[i]] = product_specifications[i + 1]

        product_info['product description'] = product_description

        yield product_info
