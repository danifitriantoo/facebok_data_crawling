import json, datetime,pandas as pd
from facebook_scraper import get_posts
from facebook_scraper import get_profile

timestamp = datetime.datetime.now();

def getData() :
    latest_post = []

    # facebook scrapper logic
    profile = get_profile('zuck')
    for post in get_posts('meta', pages=6):
        latest_post.append(post)

    # memanggil method untuk export ke CSV
    createCSV()

    # memanggil method untuk export ke json
    createJson(profile=profile,latest_post=latest_post)

def createJson(profile,latest_post):
    # membuat dictionary untuk meta json
    meta = {'purpose': 'Crawling Data Menggunakan Facebook',
            'source_data':'facebook_scrapper','schema': 'application/json'}

    # membuat dictionary untuk data utama
    data = {'founder_detail': profile, 'latest_post':latest_post}
    list_data = [data];

    # membuat dictionary entire json
    json_result = {'meta': meta,'data':list_data ,'created_at': timestamp,'updated_at':timestamp}  

    # serialize json
    json_object = json.dumps(json_result, indent=4, default=str)

    # export json kedalam bentuk file
    with open("company_profile.json", "w") as outfile:
        outfile.write(json_object)


def createCSV() :
    df = pd.read_json('hasil_facebook.json')
    df.to_csv('companies_post.csv')

getData()
