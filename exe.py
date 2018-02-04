import time

from classes import *
from interfaceGraphique import *
from events import *

                    
t = Table(8,13)
ma1 = Maison(t, 'maison', 5,5)
ma2 = Maison(t, 'maison2', 2,10)
mi1 = Mine(t, 'mine1', 1,7)
mi2 = Mine(t, 'mine2', 3,4)
mi3 = Mine(t, 'mine3', 4,12)
ch1 = Champ(t,'champ1',6,2)
ch2 = Champ(t,'champ2',8,11)
o1 = Ouvrier(t,'Xébulon I',1,2)
o2 = Ouvrier(t,'Xébulon II',2,7)
o3 = Ouvrier(t,'Xébulon III',7,9)
graph = Graphique(t)
event = Event(graph)


while 1:
    dicoTemp = {}
    
    for objet in t:
        if isinstance(objet, Ouvrier):
            dicoTemp[objet.get_nom()] = t.dictionnaireObjet[objet.get_nom()]
        direction = objet.action()
        if isinstance(objet, Ouvrier):
            dicoTemp[objet.get_nom()] = dicoTemp[objet.get_nom()] + (direction,)

    for temps in range(1,17):        
        time.sleep(1/30)
        graph.afficher(dicoTemp,temps)
        event.gestion_event()
         



    
