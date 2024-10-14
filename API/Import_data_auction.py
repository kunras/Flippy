from blizzardapi2 import BlizzardApi
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()
api_client = BlizzardApi(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
list_id_realm = [4476,4467,4465,4454,4440,4453,4477,4441,4442,4474,4464,4701,4749,4813,4456,4455,4811,4678,4815,4742,4452,4745,4466,4703,4816]
list_name_realm = ["Gehennas","Firemaw","Golemagg","Mirage_Raceway","Everlook","Pyrewood_Village", "Venoxis", "Auberdine","Lakeshire","Flamegor","Sulfuron","Mograine","Earthshaker","Mandokir","Nethergarde_Keep","Razorfen", "Giantstalker","Hydraxian_Waterlords","Thekal","Ashbringer","Chromie","Transcendence","Patchwerk","Amnennar","Jin'do"]

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


for serveur in list_name_realm:
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS `{serveur}` (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        item_id INT,
        bid BIGINT,
        buyout BIGINT,
        quantity INT,
        time_left VARCHAR(50),
        date DATE,
        heure TIME,
        FOREIGN KEY (item_id) REFERENCES items(id)
    )
    ''')




for id_realm, name_realm in zip(list_id_realm, list_name_realm):
    data_AH = api_client.wow.game_data.get_auctions_for_auction_house("eu", "fr_FR", id_realm, 2)
    print(name_realm)
    
    if 'auctions' in data_AH:
        # Insertion des données dans la base de données
        for auction in data_AH['auctions']:
            item = auction['item']
            cursor.execute(f'''
            INSERT INTO {name_realm} (item_id, bid, buyout, quantity, time_left,date,heure)
            VALUES (%s, %s, %s, %s, %s,CURDATE(),CURTIME())''',
            (item['id'], auction['bid'], auction['buyout'], auction['quantity'], auction['time_left']))
    else:
        print(f"Aucune enchère trouvée pour le royaume {name_realm}.")

mydb.commit()
cursor.close()
mydb.close()

