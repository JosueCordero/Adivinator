

database = [
    {"name":"Avicci", "Banda":False, "Solista":True, "Duo": False,"USA":False,
    "UK":False,"Electronica":True,"Vivo":False}, #

    {"name":"Martin Garrix", "Banda":False, "Solista":True,  "Duo": False,"USA":False,
    "UK":False,"Electronica":True,"Vivo":True}, #

    {"name":"The chainsmokers", "Banda":False, "Solista":False,  "Duo": True,"USA":True,
    "UK":False,"Electronica":True}, #

    {"name":"Eminem", "Banda":False, "Solista":True,  "Duo": False ,"USA":True,
    "UK":False,"Electronica":False}, #
    
    {"name":"Calle 13", "Banda":True, "Solista":False,  "Duo": False ,"USA":False,
    "UK":False,"Electronica":False,"Rock":False,"PR":True}, #

    {"name":"Santana", "Banda":True, "Solista":False,  "Duo": False ,"USA":False,
    "UK":False,"Electronica":False,"Rock":True,"PR":False,"J":True}, #

    {"name":"AC/DC", "Banda":True, "Solista":False, "Duo": False,"USA":False,
    "UK":True,"Electronica":False,"Rock":True, "PR":False,"J":False}, #

    {"name":"Queen", "Banda":True, "Solista":False,  "Duo": False,"USA":False,
    "UK":True,"Electronica":False,"Rock":True,"PR":False,"J":False}, #


    {"name":"Black eye peas", "Banda":True, "Solista":False,  "Duo": False,"USA":True,
    "UK":False,"Electronica":False,"Rock":False,"HH":True}, #

    {"name":"Disturbed", "Banda":True, "Solista":False,  "Duo": False,"USA":True,
    "UK":False,"Electronica":False,"Rock":False,"HH":False,"HM":True}, #

    {"name":"Metallica", "Banda":True, "Solista":False,  "Duo": False,"USA":True,
    "UK":False,"Electronica":False,"Rock":False,"HH":False,"HM":False, "RM":False}, #

    {"name":"Rage Against the Machine", "Banda":True, "Solista":False,  "Duo": False,"USA":True,
    "UK":False,"Electronica":False,"Rock":False,"HH":False,"HM":False, "RM":True}, #

    {"name":"Imagine Dragons", "Banda":True, "Solista":False,  "Duo": False ,"USA":True,
    "UK":False,"Electronica":False,"Rock":True,"RP":True},#

    {"name":"Foo Figthers", "Banda":True, "Solista":False,  "Duo": False,"USA":True,
    "UK":False,"Electronica":False,"Rock":True,"RP":False,"kurt":False,"Foo":True}, #

    {"name":"Nirvana", "Banda":True, "Solista":False, "Duo": False,"USA":True,
    "UK":False,"Electronica":False,"Rock":True,"RP":False,"kurt":True}, #

    {"name":"Red Hot Chilli Peppers", "Banda":True, "Solista":False,  "Duo":False ,"USA":True,
    "UK":False,"Electronica":False,"Rock":True,"RP":False,"kurt":False,"Foo":False},#

   

]

def take_chance(answer, property):
    if answer == "y":
        ans = True
    else:
        ans = False

    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("Pensabas en: "+database[0]["name"])
        quit()

    return ans


ans = input("Estas pensando en un banda musical?(y,n)")
if(take_chance(ans, "Banda")):
    ans = input("Es tu banda de los estados unidos?(y,n)")
    if(take_chance(ans,"USA")):
        ans = input("Tu banda toca rock?(y,n)")
        if(take_chance(ans,"Rock")):
            ans = input("Tu banda toca rockpop?(y,n)")
            take_chance(ans,"RP")
            ans = input("El vocalista de tu banda termino con su vida(y,n)")
            take_chance(ans,"kurt")
            ans = input("El vocalista de tu banda fue baterista de nirvana(y,n)")
            take_chance(ans,"Foo")

        ans = input("Tu banda toca Hip Hop(y,n)")
        if(not take_chance(ans,"HH")):
            ans = input("Tu banda toca Heavy Metal?(y,n)")
            take_chance(ans,"HM")
            ans = input("Tu banda toca Rap Metal?(y,n)")
            take_chance(ans,"RM")


    ans = input("Tu banda es de Puerto Rico(y,n)")
    if(not take_chance(ans,"PR")):
        ans = input("Tu banda tiene un integrante de Jalisco?(y,n)")
        if (not take_chance(ans,"J")):
            ans = input("Tu banda toca rock y es de Reino Unido(y,n)")
            take_chance(ans,"UK")
                

ans = input("Estabas pensando en un solista?(y,n)")
if(take_chance(ans, "Solista")):

    ans = input("Es tu solista de los estados unidos?(y,n)")
    if(take_chance(ans,"USA")):

        ans = input("Tu solista hace musica electronica?(y,n)")
        if(take_chance(ans,"Electronica")):

            ans = input("Tu DJ vive?(y,n)")
            take_chance(ans,"Vivo")
                

ans = input("Estas pensando en un duo?(y,n)")
if(take_chance(ans,"Duo")):
    pass



