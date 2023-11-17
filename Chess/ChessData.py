import requests

class ChessData:
    def __init__(self, username):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.theURL = f"https://api.chess.com/pub/player/{username}"
        self.player = requests.get(f"{self.theURL}/stats", headers=self.headers)
        self.playerData = requests.get(f"{self.theURL}", headers=self.headers)
    def getChessData(self):
        allGames = dict(self.player.json())
        playerData = dict(self.playerData.json())
        print(allGames)

        self.game={}
        # self.game['is_online'] = playerData['title']

        try:
            self.game['Profile']= playerData['avatar']
        except:
            self.game['Profile'] = "\static\images\profile_pic.jpg"
        try:
            self.game['Name'] = playerData['name']
        except:
            self.game['Name'] = "N/A"
        self.game['Username'] = playerData['username']
        try:
            self.game['followers'] = playerData['followers']
        except:
            self.game['followers'] = 0
        try:
            self.game['League'] = playerData['league']
        except:
            self.game['League'] = "Bronze"
        try:
            self.game["Rapid"] = allGames["chess_rapid"]
        except:
            self.game["Rapid"] = {'last': {'rating': 0, 'date': 0, 'rd': 0},
                              'best': {'rating': 0, 'date': 0, 'game': "N/A"},
                              'record': {'win': 0, 'loss': 0, 'draw': 0}}
        try:
            self.game["Bullet"] = allGames["chess_bullet"]
        except:
            self.game["Bullet"] = {'last': {'rating': 0, 'date': 0, 'rd': 0},
                              'best': {'rating': 0, 'date': 0, 'game': "N/A"},
                              'record': {'win': 0, 'loss': 0, 'draw': 0}}
        
        try:
            self.game["Blitz"] = allGames["chess_blitz"]
        except:
            self.game["Blitz"] = {'last': {'rating': 0, 'date': 0, 'rd': 0},
                              'best': {'rating': 0, 'date': 0, 'game': "N/A"},
                              'record': {'win': 0, 'loss': 0, 'draw': 0}}
        return self.game


x = ChessData("spunkysukh")
result = x.getChessData()

for i, j in result.items():
    print(i)
    print(j)
    print("\n")