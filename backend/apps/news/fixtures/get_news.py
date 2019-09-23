from newsapi import NewsApiClient
import urllib.request
import json
import os 
import datetime
started = datetime.datetime.now()

from multiprocessing.dummy import Pool as ThreadPool

newsapi = NewsApiClient(api_key='4b52745ff76141fca98215fa4db0f9d0')

categories = [
    ('Политика', 'politic'),
    ('Экономика', 'economic'),
    ('Спорт', 'sport'),
    ('Культура', 'culture'),
    ('Технологии', 'tech'),
    ('Наука', 'science'),
    ('Авто', 'auto')
]

news_id = 1
fixtures_data = []

images = []
print("Fetching breaking news... ", end="")
for category_id, (name, slug) in enumerate(categories, 1):
    fixtures_data.append({
      "model": "news.category",
      "pk": category_id,
      "fields": {
        "name": name,
        "slug": slug
      }
    })

    news = newsapi.get_everything(
            q=name,
            sources='google-news-ru,lenta,rt', 
            language='ru')

    for item in news['articles']:

        if not item['urlToImage']:
            continue
        file_ext = item['urlToImage'].split('.')[-1]
        file_path = 'news_images/{}.{}'.format(news_id, file_ext)
        images.append((item['urlToImage'], os.path.join('/app/static_content/media/', file_path)))
        fixtures_data.append({
            "model": "news.news",
            "pk": news_id,
            "fields": {
                "category_id": category_id,
                "title": item['title'],
                "content": item['description'],
                "datetime": item['publishedAt'],
                "image": file_path
            }
        })

        news_id += 1
    
initial_data_file  = open('initial_data.json', 'w')
initial_data_text = json.dumps(fixtures_data, ensure_ascii=False, indent=4)
initial_data_file.write(initial_data_text)
initial_data_file.close()

pool = ThreadPool(5)
pool.map(lambda args: urllib.request.urlretrieve(*args), images)
pool.close()
pool.join()
print("Done!")
print ((datetime.datetime.now() - started).total_seconds())