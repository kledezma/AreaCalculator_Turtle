from functools import reduce

playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)] 

def longer_than_five_minutes(song):
    return song > 5.00

def minutes_to_seconds(song):
    duration = song[1]
    minutes = int(duration)
    seconds = (duration - minutes) * 100
    return minutes * 60 + round(seconds)

def add_durations(x,y):
    return x+y

listsons = filter(longer_than_five_minutes,[song[1] for song in playlist])
listsons2 = map(minutes_to_seconds,[song for song in playlist])
listsons3 = reduce(add_durations,[song[1] for song in playlist])

print(
listsons3
)

