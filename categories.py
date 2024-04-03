import csv
import requests

url = "https://www.udemy.com/api-2.0/structured-data/navigation-lists/?list_ids=ud-main&locale=vi_VN"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()['ud-main']['items']
    fieldNames = [key for key in data[0]['sd_tag'].keys() if key != 'url' and key != 'icon_class']
    fieldNames.insert(0, '_id')
    fileName = 'categories.csv'
    with open(fileName, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldNames)
        writer.writeheader()
        for item in data:
            row = item['sd_tag']
            del row['url']
            del row['icon_class']
            row['_id'] = item['id']
            writer.writerow(row)
else:
    print("Lỗi khi gửi yêu cầu đến API")
