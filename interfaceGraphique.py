import pygame
from classes import *
from pygame.locals import *
import random

class Graphique:
      
    def __init__(self,table):
        pygame.init()
        
        self.table = table
        
        self.fenetre = pygame.display.set_mode((1920,1080))##,FULLSCREEN
        self.imgHerbe1 = pygame.image.load("texture\medievalTile_57.png").convert()
        self.imgHerbe2 = pygame.image.load("texture\medievalTile_58.png").convert()
        self.imgMine = pygame.image.load("texture\mine.png").convert_alpha()
        self.imgMaison = pygame.image.load("texture\maison.png").convert_alpha()
        self.imgChamp = pygame.image.load("texture\champ.png").convert_alpha()
        self.imgForet = pygame.image.load("texture\medievalTile_48.png").convert()

        self.OuvrierHaut1 = pygame.image.load("texture\ouvrier_haut_1.png").convert_alpha()
        self.OuvrierHaut2 = pygame.image.load("texture\ouvrier_haut_2.png").convert_alpha()
        self.OuvrierHaut3 = pygame.image.load("texture\ouvrier_haut_3.png").convert_alpha()
        self.OuvrierBas1 = pygame.image.load("texture\ouvrier_bas_1.png").convert_alpha()
        self.OuvrierBas2 = pygame.image.load("texture\ouvrier_bas_2.png").convert_alpha()
        self.OuvrierBas3 = pygame.image.load("texture\ouvrier_bas_3.png").convert_alpha()
        self.OuvrierDroite1 = pygame.image.load("texture\ouvrier_droite_1.png").convert_alpha()
        self.OuvrierDroite2 = pygame.image.load("texture\ouvrier_droite_2.png").convert_alpha()
        self.OuvrierDroite3 = pygame.image.load("texture\ouvrier_droite_3.png").convert_alpha()
        self.OuvrierGauche1 = pygame.image.load("texture\ouvrier_gauche_1.png").convert_alpha()
        self.OuvrierGauche2 = pygame.image.load("texture\ouvrier_gauche_2.png").convert_alpha()
        self.OuvrierGauche3 = pygame.image.load("texture\ouvrier_gauche_3.png").convert_alpha()

        self.imgBox = pygame.image.load("texture\\box.png").convert()
        self.imgInfoObj = pygame.image.load("texture\info_objet.png").convert_alpha()
        self.imgTxtStruct = pygame.image.load("texture\\txt_structure.png").convert_alpha()

        self.imgInfoObjMaison = pygame.image.load("texture\info_objet_maison.png").convert_alpha()
        self.imgInfoObjMine = pygame.image.load("texture\info_objet_Mine.png").convert_alpha()
        self.imgInfoObjChamp = pygame.image.load("texture\info_objet_Champ.png").convert_alpha()

        self.imgInfoObjMaisonMinerai0 = pygame.image.load("texture\info_objet_maison_minerais_0.png").convert_alpha()
        self.imgInfoObjMaisonMinerai1 = pygame.image.load("texture\info_objet_maison_minerais_1.png").convert_alpha()
        self.imgInfoObjMaisonMinerai2 = pygame.image.load("texture\info_objet_maison_minerais_2.png").convert_alpha()
        self.imgInfoObjMaisonMinerai3 = pygame.image.load("texture\info_objet_maison_minerais_3.png").convert_alpha()
        self.imgInfoObjMaisonMinerai4 = pygame.image.load("texture\info_objet_maison_minerais_4.png").convert_alpha()
        self.imgInfoObjMaisonMinerai5 = pygame.image.load("texture\info_objet_maison_minerais_5.png").convert_alpha()
        self.imgInfoObjMaisonMinerai6 = pygame.image.load("texture\info_objet_maison_minerais_6.png").convert_alpha()
        self.imgInfoObjMaisonMinerai7 = pygame.image.load("texture\info_objet_maison_minerais_7.png").convert_alpha()
        self.imgInfoObjMaisonMinerai8 = pygame.image.load("texture\info_objet_maison_minerais_8.png").convert_alpha()
        self.imgInfoObjMaisonMinerai9 = pygame.image.load("texture\info_objet_maison_minerais_9.png").convert_alpha()
        self.imgInfoObjMaisonMinerai10 = pygame.image.load("texture\info_objet_maison_minerais_10.png").convert_alpha()
        self.imgInfoObjMaisonMinerai10p = pygame.image.load("texture\info_objet_maison_minerais_10plus.png").convert_alpha()

        self.imgInfoObjMaisonNourriture0 = pygame.image.load("texture\info_objet_maison_nourriture_0.png").convert_alpha()
        self.imgInfoObjMaisonNourriture1_9 = pygame.image.load("texture\info_objet_maison_nourriture_1_9.png").convert_alpha()
        self.imgInfoObjMaisonNourriture10_30 = pygame.image.load("texture\info_objet_maison_nourriture_10_30.png").convert_alpha()
        self.imgInfoObjMaisonNourriture30p = pygame.image.load("texture\info_objet_maison_nourriture_30plus.png").convert_alpha()


        self.imgBoxMaison = pygame.image.load("texture\\box_objet_maison.png").convert_alpha()
        self.imgBoxMine = pygame.image.load("texture\\box_objet_mine.png").convert_alpha()
        self.imgBoxChamp = pygame.image.load("texture\\box_objet_champ.png").convert_alpha()

        self.imgMaisonSelect = pygame.image.load("texture\maison_select.png").convert_alpha()
        self.imgMineSelect = pygame.image.load("texture\mine_select.png").convert_alpha()
        self.imgChampSelect = pygame.image.load("texture\champ_select.png").convert_alpha()
        
        self.imgPause = pygame.image.load("texture\pause.png").convert_alpha()
        
        
        self.listeCase = []
        for i in range(0,13):
            for j in range(0,8):
                self.listeCase.append((i,j,random.randint(1,2)))

        self.dictionnaireBoxStructure = {}
        self.nomStructureSelect = None

        

    def afficher(self,dicoOuvrierTemp={},temps=0):
        
        self.afficher_fond()
        
        self.afficher_box_structure()

        for nomObjetDico in self.table.dictionnaireObjet:
            (objet,_,_) = self.table.dictionnaireObjet[nomObjetDico]
            if isinstance(objet, (Mine,Maison,Champ)):
                self.afficher_structure(nomObjetDico)

        self.afficher_structure_select()

        for nomObjetDico in self.table.dictionnaireObjet:
            (objet,_,_) = self.table.dictionnaireObjet[nomObjetDico]       
            if isinstance(objet, Ouvrier):
                self.afficher_ouvrier(nomObjetDico,dicoOuvrierTemp,temps)
                            
        self.maj_ecran()



    def afficher_fond(self):
        for i in range(0,26): # rendre ce code plus propre
            self.fenetre.blit(self.imgForet,(64*i,-36))
            self.fenetre.blit(self.imgForet,(64*i,1052))
                                             
        for (i,j,rand) in self.listeCase:
            if rand == 1:
                self.fenetre.blit(self.imgHerbe1,(128*i,128*j+28))
            else:
                self.fenetre.blit(self.imgHerbe2,(128*i,128*j+28))

        self.fenetre.blit(self.imgBox,(1664,0))
        self.fenetre.blit(self.imgInfoObj,(1664,827))
        self.fenetre.blit(self.imgTxtStruct,(1664+48,27))


    ##/!\ attention onglet et scroll /!\
    def afficher_box_structure(self):
        i = 0
        for nomObjetDico in self.table.dictionnaireObjet:
            (objet,_,_) = self.table.dictionnaireObjet[nomObjetDico]
            if isinstance(objet, Mine):
                self.fenetre.blit(self.imgBoxMine,(1686+(105*(i%2)),70+(105*(i//2))))
                self.dictionnaireBoxStructure[nomObjetDico] = ( 1686+(105*(i%2)) + 10, 1686+(105*(i%2)) + 95,
                                                                70+(105*(i//2)) + 10, 70+(105*(i//2)) + 95 )

            if isinstance(objet, Maison):
                self.fenetre.blit(self.imgBoxMaison,(1686+(105*(i%2)),70+(105*(i//2))))
                self.dictionnaireBoxStructure[nomObjetDico] = ( 1686+(105*(i%2)) + 10, 1686+(105*(i%2)) + 95,
                                                                70+(105*(i//2)) + 10, 70+(105*(i//2)) + 95 )

            if isinstance(objet, Champ):
                self.fenetre.blit(self.imgBoxChamp,(1686+(105*(i%2)),70+(105*(i//2))))
                self.dictionnaireBoxStructure[nomObjetDico] = ( 1686+(105*(i%2)) + 10, 1686+(105*(i%2)) + 95,
                                                                70+(105*(i//2)) + 10, 70+(105*(i//2)) + 95 )
                
            if isinstance(objet, (Mine,Maison,Champ)):
                i = i + 1
                


        
    def afficher_structure(self,nomObjetDico):
        
        (objet,ligne,colonne) = self.table.dictionnaireObjet[nomObjetDico]
            
        if isinstance(objet, Mine):
            self.fenetre.blit(self.imgMine,(128*(colonne-1),128*(ligne-1)+28))
                
        elif isinstance(objet, Maison):
            self.fenetre.blit(self.imgMaison,(128*(colonne-1),128*(ligne-1)+28))
                
        elif isinstance(objet, Champ):
            self.fenetre.blit(self.imgChamp,(128*(colonne-1),128*(ligne-1)+28))


    def afficher_ouvrier(self,nomObjetDico,dicoOuvrierTemp,temps):
        if not dicoOuvrierTemp or not nomObjetDico in dicoOuvrierTemp:
            (objet,ligne,colonne) = self.table.dictionnaireObjet[nomObjetDico]
            self.fenetre.blit(self.OuvrierBas1,(128*(colonne-1),128*(ligne-1)+28))

        else:
            (objet,ligne,colonne,direction) = dicoOuvrierTemp[nomObjetDico]

            if direction == ZZZ:
                self.fenetre.blit(self.OuvrierBas1,(128*(colonne-1),128*(ligne-1)+28))
                
            elif direction == HAUT:
                if temps <= 8:
                    self.fenetre.blit(self.OuvrierHaut2,(128*(colonne-1),128*(ligne-1) - (8*temps)+28))
                else:
                    self.fenetre.blit(self.OuvrierHaut3,(128*(colonne-1),128*(ligne-1) - (8*temps)+28))

            elif direction == BAS:
                if temps <= 8:
                    self.fenetre.blit(self.OuvrierBas2,(128*(colonne-1),128*(ligne-1) + (8*temps)+28))
                else:
                    self.fenetre.blit(self.OuvrierBas3,(128*(colonne-1),128*(ligne-1) + (8*temps)+28))

            elif direction == DROITE:
                if temps <= 8:
                    self.fenetre.blit(self.OuvrierDroite2,(128*(colonne-1) + (8*temps),128*(ligne-1)+28))
                else:
                    self.fenetre.blit(self.OuvrierDroite3,(128*(colonne-1) + (8*temps),128*(ligne-1)+28))

            elif direction == GAUCHE:
                if temps <= 8:
                    self.fenetre.blit(self.OuvrierGauche2,(128*(colonne-1) - (8*temps) ,128*(ligne-1)+28))
                else:
                    self.fenetre.blit(self.OuvrierGauche3,(128*(colonne-1) - (8*temps),128*(ligne-1)+28))


    def afficher_structure_select(self):
        if self.nomStructureSelect:
            (objet,ligne,colonne) = self.table.dictionnaireObjet[self.nomStructureSelect]
            if isinstance(objet, Mine):
                self.fenetre.blit(self.imgMineSelect,(128*(colonne-1),128*(ligne-1)+28))
                self.fenetre.blit(self.imgInfoObjMine,(1664,827))                
                    
            elif isinstance(objet, Maison):
                self.fenetre.blit(self.imgMaisonSelect,(128*(colonne-1),128*(ligne-1)+28))
                self.fenetre.blit(self.imgInfoObjMaison,(1664,827))
                
                if objet.get_minerai() == 0:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai0,(1664,827))
                    
                elif objet.get_minerai() == 1:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai1,(1664,827))

                elif objet.get_minerai() == 2:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai2,(1664,827))

                elif objet.get_minerai() == 3:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai3,(1664,827))
                    
                elif objet.get_minerai() == 4:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai4,(1664,827))

                elif objet.get_minerai() == 5:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai5,(1664,827))

                elif objet.get_minerai() == 6:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai6,(1664,827))

                elif objet.get_minerai() == 7:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai7,(1664,827))

                elif objet.get_minerai() == 8:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai8,(1664,827))

                elif objet.get_minerai() == 9:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai9,(1664,827))

                elif objet.get_minerai() == 10:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai10,(1664,827))

                else:
                    self.fenetre.blit(self.imgInfoObjMaisonMinerai10p,(1664,827))

                if objet.get_nourriture() == 0:
                    self.fenetre.blit(self.imgInfoObjMaisonNourriture0,(1664,827))

                elif objet.get_nourriture() < 10:
                    self.fenetre.blit(self.imgInfoObjMaisonNourriture1_9,(1664,827))

                elif objet.get_nourriture() < 31:
                    self.fenetre.blit(self.imgInfoObjMaisonNourriture10_30,(1664,827))

                else:
                    self.fenetre.blit(self.imgInfoObjMaisonNourriture30p,(1664,827))
                    
            elif isinstance(objet, Champ):
                self.fenetre.blit(self.imgChampSelect,(128*(colonne-1),128*(ligne-1)+28))
                self.fenetre.blit(self.imgInfoObjChamp,(1664,827))

        
        
    def maj_ecran(self):
        pygame.display.flip()

    def fin(self):
        pygame.display.quit()

    def pause(self):
        self.fenetre.blit(self.imgPause,(0,0))
        pygame.display.flip()

    def structure_select_on(self,nomStructure):
        self.nomStructureSelect = nomStructure

    def structure_select_off(self):
        self.nomStructureSelect = None
