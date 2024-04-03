import csv
import requests

sub_categories_path = 'sub_categories.csv'
list_id_sub_categories = []
with open(sub_categories_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        list_id_sub_categories.append(row['id'])
url_demo = 'https://www.udemy.com/api-2.0/course-subcategories/8/labels/?page_size=9&locale=vi_VN&navigation_locale=vi_VN'
response_demo = requests.get(url_demo)
if (response_demo.status_code == 200):
    data = response_demo.json()['results'][0]
    fileName = 'course_categories.csv'
    fieldNames = [key for key in data.keys() if key != 'topic_channel_url' and key != 'url']
    fieldNames.insert(0, 'id_sub')
    print(fieldNames)
    with open(fileName, 'w', newline='', encoding='utf-8') as file:
        write = csv.DictWriter(file, fieldnames=fieldNames)
        write.writeheader()
        for sub_id in list_id_sub_categories:
            url = f'https://www.udemy.com/api-2.0/course-subcategories/{sub_id}/labels/?page_size=9&locale=vi_VN&navigation_locale=vi_VN'
            response = requests.get(url)
            if (response.status_code == 200):
                data = response.json()['results']
                for course in data[1:]:
                    del course['topic_channel_url']
                    del course['url']
                    course['id_sub'] = sub_id
                    write.writerow(course)

    # with open(fileName, newline='', encoding='utf-8') as file:
    #     writer = csv.DictWriter(file, fieldnames=fieldNames)
    #     writer.writeheader()
        # for sub_id in list_id_sub_categories:
        #     url = f'https://www.udemy.com/api-2.0/course-subcategories/{sub_id}/labels/?page_size=9&locale=vi_VN&navigation_locale=vi_VN'
        #     response = requests.get(url)
        #     if response.status_code == 200:
        #         data = response.json()['results']
        #
        #         print(data)