import requests
try:
    r = requests.get('https://docs.google.com/document/u/4/export?format=txt&id=1MaetdIy3yDCVHEzmD87SGyHquNavWJo3k-RVU7tYE6Q&token=AC4w5Vg4qq7bqDhwXOwmXKAyzpZr7afLzg%3A1586228079190&includes_info_params=true')
    b = r.text
    with open('birthday', 'w') as f:
        f.write(b)
except Exception as e:
    print('error')
    print(e)

with open('birthday', 'r') as f:
    p = f.read()
    p = p.split('\n')

for i in p:
    name_birthday = i.split(':')[0]
    solar_birthday = i.split(':')[1].replace(' ', '')
    solar_day = int(solar_birthday.split('/')[0])
    solar_month = int(solar_birthday.split('/')[1])
    solar_year = int(solar_birthday.split('/')[2])
    print(name_birthday)