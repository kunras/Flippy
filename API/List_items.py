from blizzardapi2 import BlizzardApi
import mysql.connector
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_client = BlizzardApi(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
mydb = mysql.connector.connect(
    host=os.getenv('HOST_DB'),
    user=os.getenv('USER_DB'),
    password=os.getenv('PASSWORD_DB'),
    database=os.getenv('DATABASE_DB')
)
cursor = mydb.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    id_item INT PRIMARY KEY,
    name_item VARCHAR(100),
    url_img VARCHAR(300)
)
''')

i=2749

while i < 9999999:
    try:
        name_search = api_client.wow.game_data.get_item("eu","fr_FR",i,True)
        print(f'item trouvé avec l\'id {i}')
        try:
            img_search = api_client.wow.game_data.get_item_media("eu","fr_FR",i,True)
            if 'assets' in img_search : 
                print(f'image trouvé avec l\'id {i}')
                cursor.execute(f'''
                INSERT INTO items (id_item, name_item, url_img)
                VALUES (%s, %s, %s)''',
                (i, name_search["name"],img_search["assets"][0]["value"]))
            else:
                print(f'URL OK mais pas d\'image avec l\'id {i}')
        except requests.exceptions.HTTPError:
            if e.response.status_code == 404:
                print(f'Pas d\'image avec l\'id {i}')
            else:
                print("Autre prob")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f'Pas d\'item avec l\'id {i}')
        else:
            print("Autre prob")
    i+=1







mydb.commit()
cursor.close()
mydb.close()