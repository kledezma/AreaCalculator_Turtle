#class Person:
   # def __init__(self, name, position,number,yards_gained,touchdowns):
    #  self.name = name
    #  self.age = age



players = [
  {
    "name" : "Patrick ",
    "position" : "Quarterback",
    "number" : 10,
    'yards_gained': 150,
    'touchdowns': 300
  },
  {
    "name" : "Travis  ",
    "position" : "Hight End",
    "number" : 10,
    'yards_gained': 530,
    'touchdowns': 13
  },  
  {
    "name" : "Tyreek  ",
    "position" : "Wide Receiver",
    "number" : 5,
    'yards_gained': 10,
    'touchdowns': 6
  },
]
totalTouchdowns = 0
totalYards_gained = 0
avrgTouchdowns = 0
avrgYards_gained = 0

players[1]["yards_gained"] = 600
for i in range(len(players)):
  totalTouchdowns += players[i]["touchdowns"]
  totalYards_gained += players[i]["yards_gained"]
  print(players[i]["position"])
  print(players[i]["yards_gained"])

avrgTouchdowns = totalTouchdowns / len(players)
avrgYards_gained = totalYards_gained / len(players)

average_yards = sum(player["yards_gained"] for player in players) / len(players)
average_touchdowns = sum(player["touchdowns"] for player in players) / len(players)

print(avrgTouchdowns)
print(avrgYards_gained)
