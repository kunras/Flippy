from blizzardapi2 import BlizzardApi

api_client = BlizzardApi("1da39a413b0943d4ba886681394d419b", "O5cWyf6YBvozdpCQquid2KTmJZ2DolDz")
data_AH = api_client.wow.game_data.get_auctions_for_auction_house("eu","fr_FR",4440,2)

with open("./data/Data_auberdine.json","w") as fichier:
    fichier.write(str(data_AH))