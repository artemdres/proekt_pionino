import pygame
import pygame.freetype
import seting
class Menu:
    def __init__(self,game):
        self.nomer_pesni=1
        self.cvet1=[255,255,255]
        self.cvet2=[0,0,0]
        self.cvet3=[0,0,0]
        self.game=game
        self.fon_menu=pygame.image.load("menu.png")
        self.text=pygame.freetype.Font("ofont.ru_Nunito.ttf", 25)
    def otrisovka(self):
        self.game.okno.blit(self.fon_menu, [0,0])
        self.text.render_to(self.game.okno,[30,100], "в лесу родилась ёлочка",self.cvet1)
        self.text.render_to(self.game.okno,[100,300], "берёзка",self.cvet2)
        self.text.render_to(self.game.okno,[150,500], "утро",self.cvet3)














        pygame.display.update()




    def logika(self):
        pass



    def sobitia(self): 
        spisok_sobitia=pygame.event.get()
        for sobitie in spisok_sobitia:
            if sobitie.type==pygame.QUIT:
                
                self.game.q=1
            elif sobitie.type==pygame.KEYDOWN:
                if sobitie.key==pygame.K_DOWN:
                    if self.nomer_pesni==1:
                        self.nomer_pesni=2
                        self.cvet1=[0,0,0]
                        self.cvet2=[255,255,255]
                    elif self.nomer_pesni==2:
                        self.nomer_pesni=3
                        self.cvet2=[0,0,0]
                        self.cvet3=[255,255,255]
                    elif self.nomer_pesni==3:
                        self.nomer_pesni=1
                        self.cvet3=[0,0,0]
                        self.cvet1=[255,255,255]
                if sobitie.key==pygame.K_UP:
                    if self.nomer_pesni==1:
                        self.nomer_pesni=3
                        self.cvet1=[0,0,0]
                        self.cvet3=[255,255,255]
                    elif self.nomer_pesni==3:
                        self.nomer_pesni=2
                        self.cvet3=[0,0,0]
                        self.cvet2=[255,255,255]
                    elif self.nomer_pesni==2:
                        self.nomer_pesni=1
                        self.cvet2=[0,0,0]
                        self.cvet1=[255,255,255]
                if sobitie.key==pygame.K_RETURN:
                    if  self.nomer_pesni==1:
                        self.game.pesna_nota=seting.CHRISTMAS_TREE_NOTES
                        self.game.pesna_time=seting.BIRCH_DURATION
                    elif  self.nomer_pesni==2:
                        self.game.pesna_nota=seting.BIRCH_NOTES
                        self.game.pesna_time=seting.BIRCH_DURATION
                    elif self.nomer_pesni==3:
                        self.game.pesna_nota=seting.MORNING_NOTES
                        self.game.pesna_time=seting.MORNING_DURATION


                    self.game.game_menu=1
                    self.game.win_game_over=0
                    self.game.time=0
                    self.game.time_game_over=0
                    self.game.clavis_propysk=0
                    self.game.nota_cliknyta=0
                    self.game.cislo_musik=0
                    self.game.notes=[]
                    self.game.nota_scet=len(self.game.pesna_nota)