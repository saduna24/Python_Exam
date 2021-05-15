# 1
# import requests
# resp = requests.get("https://btu.edu.ge")
# print(resp.status_code)
# print(resp.headers)
# print(resp.headers['Content-Type'])


# 2 & 3
# import json
# import sqlite3
# import requests
#
# api_key: str = 'b7ac53435df9ab14f67fa7c0ee471aed'
# choose = input("ევროს ეკვივალენტი (USD,GEL...): ")
# currency = choose
# url = f'http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols={currency}'
# r = requests.get(url)
# result_json = r.text
# res = json.loads(result_json)
# res_structured = json.dumps(res, indent=4)
# print(res_structured)
# time = res['date']
# price = res['rates']
#
# print(f' დრო: {time} ეკვივალენტი: {price}')


'''ვცადე ავტომატურად შეეტანა წინა მოქმედებებიდან მონაცემები მაგრამ ვერ გადავიყვანე შესაფერის ტიპში მონაცემები'''
# conn = sqlite3.connect("currency.sqlite")
# cursor = conn.cursor()
# # cursor.execute('''CREATE TABLE History
# #               (id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                dro ,
# #                fasi );''')
#
# change = (time, price)
#
# cursor.execute('INSERT INTO History (dro, fasi) VALUES (?, ? )', change)


# conn.commit()
