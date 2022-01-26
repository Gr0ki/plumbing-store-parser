# About this project:
This is my training project for parsing data from web-sites.
This project was build to parse a specific web-site: "https://best-dim.com/ua/g4861238-santehnika".

The scraper moves through all subcategories and all the pages to take info about each product in the site tree from starting point.

# Parser commands (from ../plumbing_store/):
"scrapy runspider spiders/store_spider.py" - to run parser and output result to a console

"scrapy crawl store_spider -O store_spider.json" - to run parser and output result to a new json file
(If such a file already exists, it will be overwritten. Use "-o" to append.)

You can also replace ".json" with ".csv" in the command above to write to csv file.

# Create xlsx file (by using .json file):
After writing parsed data from the store to json file run "python convert_json_to_xlsx.py" to create .xlsx file.

