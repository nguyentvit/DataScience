import csv
import requests

fileName = 'courses.csv'
url = 'https://www.udemy.com/api-2.0/discovery-units/all_courses/?page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&label_id=7450&source_page=topic_page&locale=vi_VN&currency=vnd&skip_price=true&sos=pl&fl=lbl'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()['unit']['items']
    print(data)