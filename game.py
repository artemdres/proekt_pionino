import pygame
import seting
import sprait
import random
import pygame.freetype
import  menu

pygame.init()






class Game:
    def __init__ (self):
        self.pesna_nota=seting.BIRCH_NOTES
        self.pesna_time=seting.BIRCH_DURATION
        self.time=0
        self.time_game_over=0
        self.menu=menu.Menu(self)
        self.game_menu=0
        self.win_game_over=0
        self.clavis_propysk=0
        self.text=pygame.freetype.Font("ofont.ru_Nunito.ttf", 40)
        self.nota_cliknyta=0
        self.nota_scet=len(self.pesna_nota)
        
        self.cislo_musik=0
        self.okno=pygame.display.set_mode(seting.SIZE,)
        self.q=0
        self.notes=[]
        self.time_notees=pygame.USEREVENT
        pygame.time.set_timer(self.time_notees, 700)
        
    def otrisovka (self):
        self.okno.fill([255,255,255])
        stolbik=seting.SIR_STOLB
        cislo=0
        while seting.STOLB>cislo:
            pygame.draw.line(self.okno, [0,0,0],[stolbik,0],[stolbik,600])
            stolbik=stolbik+seting.SIR_STOLB
            cislo=cislo+1
        pygame.draw.line(self.okno, [255,0,0],[0,500],[600,500])
        if self.win_game_over==0:
            for nota in self.notes:
                nota.otrisovka(self.okno)
        
        self.text.render_to(self.okno,[0,0], str(self.nota_scet))
        if self.nota_cliknyta==len(self.pesna_nota):
            
            self.text.render_to(self.okno,[300,200], "win",[255,0,0])

        elif self.cislo_musik==len(self.pesna_nota) and self.notes[-1].xitbox.y>500:

            
            self.text.render_to(self.okno,[100,200],"game over",[255,0,0])
        elif self.win_game_over==1:
            self.text.render_to(self.okno,[100,200],"game over",[255,0,0])
        pygame.display.update()
        
    def logika (self):
        for dfig_nots in self.notes:
            dfig_nots.dvig()
        for notes in self.notes:
            if notes.xitbox.y>500 and notes.off_on==0:
                self.clavis_propysk=self.clavis_propysk+1
                self.notes.remove(notes)
                if self.clavis_propysk>2  and self.win_game_over==0:
                    self.time_game_over=pygame.time.get_ticks()
                    self.win_game_over=1

                    
        self.time=pygame.time.get_ticks()
        if self.time-self.time_game_over>2000 and self.win_game_over==1:
            self.game_menu=0
        elif self.time-self.time_game_over>2000 and self.win_game_over==2:
            self.game_menu=0
    
    
            
    def sobitia (self):
        
        spisok_sobitia=pygame.event.get()
        for sobitie in spisok_sobitia:
            if sobitie.type==pygame.QUIT:
                self.q=1
            elif sobitie.type==self.time_notees and self.cislo_musik<len(self.pesna_nota):
                nota=sprait.Nota(self.pesna_nota[self.cislo_musik],self.pesna_time[self.cislo_musik],self.cislo_musik)
                self.notes.append(nota)
                self.cislo_musik=self.cislo_musik+1
            elif sobitie.type==pygame.MOUSEBUTTONDOWN:
                for note in self.notes:
                    if note.xitbox.collidepoint(sobitie.pos)==True and note.off_on==0 :
                        if self.notes.index(note)==self.nota_cliknyta:
                            note.klik()
                            self.nota_scet=self.nota_scet-1
                            self.nota_cliknyta=self.nota_cliknyta+1
                            if self.nota_cliknyta==len(self.pesna_nota):
                                self.win_game_over=2
                                self.time_game_over=pygame.time.get_ticks()
                                
                        else:
                            self.win_game_over=1
                            self.time_game_over=pygame.time.get_ticks()
                            


    def play (self):
        self.q=0
        
        while 0==self.q:
            if self.game_menu==1:
            
            
                self.otrisovka()
                self.logika()
                self.sobitia()

            else:
                self.menu.otrisovka()
                self.menu.logika()
                self.menu.sobitia()
game_pionino=Game()
game_pionino.play()
