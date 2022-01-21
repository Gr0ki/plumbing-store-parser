# CSS selectors


start_urls = ['https://best-dim.com/ua/g4861238-santehnika']


# Returns generator of 12 links to the categories on that store
#categories = [e for e in response.css('a.b-product-groups-gallery__image-link::attr(href)')]
#category_urls = (
#    'https://best-dim.com' + categories[i].get() + '?product_items_per_page=48' for i in range(len(categories))
#)               # Use next(category_urls) to get link for first page in a next category

category_urls = [
            'https://best-dim.com' + e.get() + '?product_items_per_page=48' for e in response.css(
                'a.b-product-groups-gallery__image-link::attr(href)'
            )
        ]


# Returns a link to the next page(on the category items list), or None if there isn't one
next_page = response.css('a.b-pager__link.b-pager__link_pos_last::attr(href)').get()
next_page = 'https://best-dim.com' + next_page + '?product_items_per_page=48'


# Returns a list of links to each item on the page 
items = response.css('a.b-centered-image.b-product-line__image-wrapper::attr(href)')
items = [items[i].get() for i in range(len(items))]


# Taking data of a particular item
item_image_url = response.css('img.b-centered-image__img::attr(src)').get()

item_code = response.css('span.b-product__sku::text').get()[5:]

item_name = response.css('h1.b-title::text').get()

item_status = response.css('span.b-product__state.b-product__state_type_available::text').get()

item_prise = response.css('li.b-order-info__item::text').getall()[1].strip()
# get rid of \xa0 (non-breaking space character)
# item_prise = item_prise[:2].strip() + item_prise[3:]

item_specifications = [
    elem.strip() for elem in response.css('td.b-product-info__cell::text').getall() if elem.strip()
]

item_description = response.css('div.b-content__body.b-user-content').get()
soup = BeautifulSoup(item_description)
item_description = [i.get_text() for i in soup.find_all(string=True) if i.get_text()]
item_description = item_description[:len(item_description)-1]
item_description = ' '.join(item_description)
print()