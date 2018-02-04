from interfaceGraphique import *
import pygame
from pygame.locals import *


class Event:

    def __init__(self, graphique):
        self.graph = graphique


    def gestion_event(self):
        for event in pygame.event.get():
            self.event_pause(event)
            self.event_souris(event)
            self.event_fin(event)
        


    def event_fin(self,event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.graph.fin()
        
        if event.type == QUIT:
            self.graph.fin()
        
            
    def event_pause(self,event):
        if event.type == KEYDOWN and event.key == K_SPACE:
                self.graph.pause()
                pauseEnCours = 1
                while pauseEnCours:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN and event.key == K_SPACE:
                            pauseEnCours = 0
                    self.event_fin(event)
                    
    def event_souris(self,event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            for nomStructureBox in self.graph.dictionnaireBoxStructure:
                (xMin, xMax, yMin, yMax) = self.graph.dictionnaireBoxStructure[nomStructureBox]
                
                if (event.pos[0] > xMin and event.pos[0] < xMax and
                            event.pos[1] > yMin and event.pos[1] < yMax):
                    self.graph.structure_select_on(nomStructureBox)
                    return

            self.graph.structure_select_off()
            return

                
            
