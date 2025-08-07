songs = {
    'Mago de Oz':'Fiesta Pagana',
    'Warcry':'Quiero',
    'Saratoga':'Halcon'
}

def writesongs(listSons,fileName):
    with open(fileName+".txt",'w') as file:
        for key,value in listSons.items():
            file.write(f"Agrupacion:  {key} |||| Cancion: {value} \n")
    


writesongs(songs,"orale")