## Classes divers et varies
import copy
import random

ZZZ = 0
HAUT = 1
BAS = 2
GAUCHE = 3
DROITE = 4


class Table:
    dictionnaireObjet = {}
    
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur


    def ajouter_Objet(self, nomObjet, objet, ligne, colonne): # ATTENTION : 2 objets ne peuvent pas avoir le même nom
        self.dictionnaireObjet[nomObjet] = (objet, ligne, colonne)


    def get_objet(self,nomObjet):
        objet,_,_ = self.dictionnaireObjet[nomObjet]
        return objet
    
    def get_ligne(self,nomObjet):
        _,ligne,_ = self.dictionnaireObjet[nomObjet]
        return ligne
        
    def get_colonne(self,nomObjet):
        _,_,colonne = self.dictionnaireObjet[nomObjet]
        return colonne

        
    def deplace_up(self,objet):
        if self.get_ligne(objet.get_nom()) <= 1: ## si je suis en bord de plateau
            pass
            #print('Impossible de se déplacer vers le haut')
        else:
            nom=objet.get_nom()
            self.dictionnaireObjet[nom]=(self.get_objet(nom),self.get_ligne(nom)-1,self.get_colonne(nom))

    def deplace_down(self,objet):
        if self.get_ligne(objet.get_nom()) >= self.longueur:
            pass
            #print('Impossible de se déplacer vers le bas')
        else:
            nom=objet.get_nom()
            self.dictionnaireObjet[nom]=(self.get_objet(nom),self.get_ligne(nom)+1,self.get_colonne(nom))

    def deplace_left(self,objet):
        if self.get_colonne(objet.get_nom()) <= 1:
            pass
            #print('Impossible de se déplacer vers la gauche')
        else:
            nom=objet.get_nom()
            self.dictionnaireObjet[nom]=(self.get_objet(nom),self.get_ligne(nom),self.get_colonne(nom)-1)

    def deplace_right(self,objet):
        if self.get_colonne(objet.get_nom()) >= self.largeur:
            pass
            #print('Impossible de se déplacer vers la droite')
        else:
            nom=objet.get_nom()
            self.dictionnaireObjet[nom]=(self.get_objet(nom),self.get_ligne(nom),self.get_colonne(nom)+1)

    def __iter__(self):
        return Iter_Table(self, self.dictionnaireObjet)


class Iter_Table:
    def __init__(self, table, dictionnaireObjet):
        self.listeObjet = [table.get_objet(l) for l in dictionnaireObjet]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.listeObjet:
            raise StopIteration
        return self.listeObjet.pop(0)
        

class Objet:
    def __init__(self,table,nom,ligne,colonne):
        self.nomObjet = nom
        self.table = table
        table.dictionnaireObjet[nom]=(self,ligne,colonne)


    def action(self):
        pass


    def deplace_up(self):
        self.table.deplace_up(self)

    def deplace_down(self):
        self.table.deplace_down(self)

    def deplace_right(self):
        self.table.deplace_right(self)

    def deplace_left(self):
        self.table.deplace_left(self)


    def get_nom(self):
        return self.nomObjet


class Maison (Objet):
    listeXebu = (['Xébulon I','Xébulon II','Xébulon III','Xébulon IV','Xébulon V','Xébulon VI','Xébulon VII','Xébulon VIII',
                  'Xébulon IX','Xébulon X','Xébulon XI','Xébulon XII','Xébulon XIII','Xébulon XIV','Xébulon XV','Xébulon XVI',
                  'Xébulon XVII','Xébulon XVIII','Xébulon IXX','Xébulon XX','Xébulon XXI','Xébulon XXII','Xébulon XXIII',
                  'Xébulon XXIV','Xébulon XXV','Xébulon XXVI','Xébulon XXVII','Xébulon XXVIII','Xébulon IXXX','Xébulon XXX',
                  'Xébulon XXXI','Xébulon XXXII','Xébulon XXXIII','Xébulon XXXIV','Xébulon XXXV','Xébulon XXXVI','Super-Xébulon'])
    
    def __init__(self,table,nom,ligne,colonne):
        Objet.__init__(self,table, nom, ligne, colonne)
        self.nourriture = 0
        self.minerai = 0

        
    def action(self):
        ouvriersDansMaison = ([ouvrier for ouvrier in self.table if isinstance(ouvrier, Ouvrier) and
                               self.table.get_ligne(ouvrier.get_nom()) == self.table.get_ligne(self.get_nom()) and
                               self.table.get_colonne(ouvrier.get_nom()) == self.table.get_colonne(self.get_nom())])

                               
        if ouvriersDansMaison:
            for ouvrier in ouvriersDansMaison:
                if ouvrier.minerai != 0:
                    self.minerai = self.minerai + ouvrier.minerai
                    ouvrier.minerai = 0 ## Créer une classe interaction pour éviter de modifier directement les attributs d'une autres classe

                if ouvrier.nourriture != 0:
                    self.nourriture = self.nourriture + ouvrier.nourriture
                    ouvrier.nourriture = 0

            
            for ouvrier in ouvriersDansMaison:
                if ouvrier.dernierRepas > 5 and self.nourriture > 0: ## Définir une limite de tour ou l'ouvrier aura faim (ici 5)
                    ouvrier.dernierRepas = 0
                    self.nourriture = self.nourriture - 1


        if self.minerai >= 8:
            try:
                self.minerai = self.minerai - 8
                return Ouvrier(self.table, self.listeXebu[len([ouvrier for ouvrier in self.table if isinstance(ouvrier, Ouvrier)])],
                               self.table.get_ligne(self.nomObjet), self.table.get_colonne(self.nomObjet))

            except IndexError:
                print("Super-Xébulon est arrivé plus aucune naissance de possible")

    def get_minerai(self):
        return self.minerai

    def get_nourriture(self):
        return self.nourriture
            


class Ouvrier (Objet):
    def __init__(self,table,nom,ligne,colonne):
        Objet.__init__(self,table,nom,ligne,colonne)
        self.minerai = 0
        self.nourriture = 0
        self.dernierRepas = 0
        self.chemin = []
        self.selectionne = False


    def action(self):
        if not self.chemin:
            i = random.randint(1,100)

            if i < 40:
                return ZZZ

            elif i < 55:
                self.deplace_up()
                return HAUT

            elif i < 70:
                self.deplace_down()
                return BAS

            elif i < 85:
                self.deplace_right()
                return DROITE

            else:
                self.deplace_left ()
                return GAUCHE

    



class Mine (Objet):
    def __init__(self,table,nom,ligne,colonne):
        Objet.__init__(self,table,nom,ligne,colonne)


    def action(self):
        ouvriersDansMine = ([ouvrier for ouvrier in self.table if isinstance(ouvrier, Ouvrier) and
                               self.table.get_ligne(ouvrier.get_nom()) == self.table.get_ligne(self.get_nom()) and
                               self.table.get_colonne(ouvrier.get_nom()) == self.table.get_colonne(self.get_nom())])
        
        if ouvriersDansMine:
            for ouvrier in ouvriersDansMine:
                if ouvrier.minerai + ouvrier.nourriture <= 3:
                    ouvrier.minerai = ouvrier.minerai + 1 ## Ajouter des méthodes dans Ouvrier
                #elif ouvrier.minerai + ouvrier.nourriture == 9:
                 #   ouvrier.minerai = ouvrier.minerai + 1   



class Champ (Objet):
    def __init__(self,table,nom,ligne,colonne):
        Objet.__init__(self,table,nom,ligne,colonne)


    def action(self):
        ouvriersDansChamp = ([ouvrier for ouvrier in self.table if isinstance(ouvrier, Ouvrier) and
                               self.table.get_ligne(ouvrier.get_nom()) == self.table.get_ligne(self.get_nom()) and
                               self.table.get_colonne(ouvrier.get_nom()) == self.table.get_colonne(self.get_nom())])
        
        if ouvriersDansChamp:
            for ouvrier in ouvriersDansChamp:
                if ouvrier.minerai + ouvrier.nourriture <= 3:
                    ouvrier.nourriture = ouvrier.nourriture + 1 ## Ajouter des méthodes dans Ouvrier
                #elif ouvrier.minerai + ouvrier.nourriture == 9:
                 #   ouvrier.nourriture = ouvrier.nourriture + 1
    





