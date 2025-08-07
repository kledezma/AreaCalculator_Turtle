import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(name):
  return name.capitalize()

def fire_in_name(name):
  return 'Fire' in name

def concatenate_names(name1, name2):
  return name1 + name2

listRandom = []
# for sufijo in suffixes:
#   listRandom.append(create_fantasy_name(suffixes,prefixes))
  

listacapitalizada = list(map(capitalize_suffix, suffixes))
listafuego = list(filter(fire_in_name,suffixes))
listaReduce = reduce(concatenate_names,suffixes,prefixes)
print(listaReduce)
