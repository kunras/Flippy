from blizzardapi2 import BlizzardApi

api_client = BlizzardApi("1da39a413b0943d4ba886681394d419b", "O5cWyf6YBvozdpCQquid2KTmJZ2DolDz")

list_id_realm = [4476,4467,4465,4454,4440,4453,4477,4441,4442,4474,4464,4701,4749,4813,4456,4455,4811,4678,4815,4742,4452,4745,4466,4703,4816]
list_name_realm = ["Gehennas","Firemaw","Golemagg","Mirage Raceway","Everlook","Pyrewood Village", "Venoxis", "Auberdine","Lakeshire","Flamegor","Sulfuron","Mograine","Earthshaker","Mandokir","Nethergarde Keep","Razorfen", "Giantstalker","Hydraxian Waterlords","Thekal","Ashbringer","Chromie","Transcendence","Patchwerk","Amnennar","Jin'do"]


for id_realm,name_realm in zip(list_id_realm,list_name_realm):
    data_AH = api_client.wow.game_data.get_auctions_for_auction_house("eu","fr_FR",id_realm,2)
    with open(f'./data/{name_realm}',"w") as fichier:
        fichier.write(str(data_AH))




