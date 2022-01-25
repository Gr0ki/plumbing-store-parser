import pandas as pd

df_json = pd.read_json('plumbing_store/store_spider.json')
df_json.to_excel('plumbing_store/store_spider.xlsx')
