import requests
from config import etsy_key
import pandas as pd
from pandas import Timestamp
import json
import datetime

df = pd.read_csv ('shop_ids.csv')
df = df.reset_index()
df_new = pd.DataFrame(columns=['date_time', 'shop_name','sold_count','favorites','review_score','review_count','listing_active_count'])

for i in range(len(df)):
    url = "https://openapi.etsy.com/v3/application/shops/" + df.iloc[i, 2].astype(str)

    payload={}
    headers = {
      'x-api-key': etsy_key,
      'Cookie': 'user_prefs=Iw7P9NQSWBGDNHpeBc4ftvqNldpjZACCJK1d_DA6Oq80J0eHPCKWAQA.'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    json_data = response.json()

    favorites = json_data['num_favorers']
    sold_count = json_data['transaction_sold_count']
    review_score = json_data['review_average']
    review_count = json_data['review_count']
    shop_name = json_data['shop_name']
    listing_active_count = json_data['listing_active_count']
    date_time = Timestamp.today()
    
    data = {
    'date_time': [date_time],
    'shop_name': [shop_name], 
    'sold_count': [sold_count],
    'favorites': [favorites],
    'review_score': [review_score],
    'review_count': [review_count],
    'listing_active_count': [listing_active_count]
    }
    df_merge = pd.DataFrame(data=data)
    df_new = pd.concat([df_new, df_merge])
    
df_new.to_csv('comp_data.csv', mode='a', index=False, header=False)