import pygame
import random




off_dlina=pygame.image.load("long_tile.png")
on_dlina=pygame.image.load("long_tile_pressed.png")
off_karotka=pygame.image.load("short_tile.png")
on_karotka=pygame.image.load("short_tile_pressed.png")



class Nota:
    def __init__(self,nazvanie,time,nomer):
        self.musik=pygame.mixer.Sound("Sounds/"+nazvanie+".ogg")
        cord_nota=0
        clyc_cislo=random.randint(0, 3)
        self.nomer=nomer
        self.nazvanie=nazvanie
        self.time=time
        self.off_on=0
        if self.time==1:
            self.kartinka=off_karotka
        elif self.time==2:
            self.kartinka=off_dlina
        
        if clyc_cislo==0:
            cord_nota=0
            self.xitbox=pygame.Rect([cord_nota,0],self.kartinka.get_size())

        elif clyc_cislo==1:
            cord_nota=100
            self.xitbox=pygame.Rect([cord_nota,0],self.kartinka.get_size())
         
        elif clyc_cislo==2:
            cord_nota=200
            self.xitbox=pygame.Rect([cord_nota,0],self.kartinka.get_size())
        elif clyc_cislo==3:
            cord_nota=300
            self.xitbox=pygame.Rect([cord_nota,0],self.kartinka.get_size())



        self.skorost=1
        
    def otrisovka(self,okno):
        okno.blit(self.kartinka,self.xitbox)
    def dvig(self):
        self.xitbox.y=self.xitbox.y+self.skorost
    def klik (self):
        
        self.off_on=1


        if self.time==1:
            self.kartinka=on_karotka
        
        else:
            self.kartinka=on_dlina
        kanal=pygame.mixer.find_channel()
        if kanal==None:
            pygame.mixer.stop()
        self.musik.play()
