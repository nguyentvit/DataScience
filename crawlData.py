import csv
import requests

url = "https://www.udemy.com/api-2.0/structured-data/navigation-lists/?list_ids=ud-main&locale=vi_VN"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()['ud-main']['items']
    for item in data:
        print(item)
else:
    print("Lỗi khi gửi yêu cầu đến API")
