from blizzardapi2 import BlizzardApi
import mysql.connector
import requests

# Connexion à l'API Blizzard
api_client = BlizzardApi("1da39a413b0943d4ba886681394d419b", "O5cWyf6YBvozdpCQquid2KTmJZ2DolDz")

# Connexion à la base de données MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="data_cata"
)
cursor = mydb.cursor()

# Création de la table items si elle n'existe pas
cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    id_item INT PRIMARY KEY,
    name_item VARCHAR(100),
    url_img VARCHAR(300)
)
''')

# Exécution de la requête pour récupérer les IDs des items
cursor.execute('''
SELECT item_id FROM Gehennas
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Firemaw
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Golemagg
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Mirage_Raceway
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Everlook
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Pyrewood_Village
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Venoxis
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Auberdine
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Lakeshire
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Flamegor
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Sulfuron
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Mograine
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Earthshaker
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Mandokir
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Nethergarde_Keep
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Razorfen
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Giantstalker
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Hydraxian_Waterlords
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Thekal
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Ashbringer
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Chromie
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Transcendence
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Patchwerk
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM Amnennar
WHERE item_id NOT IN (SELECT id_item FROM items)
UNION
SELECT item_id FROM `Jin'do`
WHERE item_id NOT IN (SELECT id_item FROM items)
ORDER BY item_id ASC;
''') 

# Récupérer les résultats
data_id = cursor.fetchall()

# Préparer les données à insérer avec executemany
data_to_insert = []
for row in data_id:
    id = row[0]
    print(id)
    # Récupération des données de l'API pour chaque item
    try:
        name_search = api_client.wow.game_data.get_item("eu", "fr_FR", id, True)
        try:
            img_search = api_client.wow.game_data.get_item_media("eu", "fr_FR", id, True)
            # Ajouter les données à insérer dans la liste
            data_to_insert.append((
                id, 
                name_search["name"], 
                img_search["assets"][0]["value"]
            ))
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f'image non trouvé pour l\'id : {id}')
                data_to_insert.append((
                id, 
                name_search["name"], 
                "null"
            ))
            else:
                print(f'Autre prob avec l\'id : {id}')
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f'nom non trouvé pour l\'id : {id}')
        else:
            print(f'Autre prob avec l\'id : {id}')

        

# Insertion des données en une seule fois
cursor.executemany('''
    INSERT INTO items (id_item, name_item, url_img)
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE name_item=%s, url_img=%s
''', [(id, name, url, name, url) for id, name, url in data_to_insert])

# Commit des changements
mydb.commit()

# Fermeture du curseur et de la connexion à la base de données
cursor.close()
mydb.close()
