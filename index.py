import pygame, sys #importer viktige bibloteker
import random

#funksjon for retning, fart og posisjon for ballen
def ball_animasjon():
    global ball_fart_x, ball_fart_y #gjør det mulig å bruke variablene i dette scopet
    #ballfart
    ball.x += ball_fart_x #endrer x kordinaten, dette blir gjort for hver frame som at ballen beveger seg gradvis.
    ball.y += ball_fart_y #samme med y kordinaten
    if ball.top <= 0 or ball.bottom >= skjerm_høyde: #gjør slik at ballen ikke beveger seg ut av bildet.
        ball_fart_y *= -1 #gjør farten til ballen invers
    if ball.left <= 0 or ball.right >= skjerm_bredde: #setter ballen i midten hvis den treffer høyre eller venstre side 
        ball_restart() #kaller restart funksjonen
        
    if ball.colliderect(spiller1) or ball.colliderect(spiller2): 
        ball_fart_x *= -1 #endrer farten slik at den bytter vei, x-kordinater

#funksjon som endrer farten til spiller 1
def spiller1_animasjon(): 
    spiller1.y += spiller1_fart #endrer y kordinaten til spiller 1
    if spiller1.top <= 0: #passer på at spiller 1 ikke kan bevege seg ut av bildet 
        spiller1.top = 0
    if spiller1.bottom >= skjerm_høyde:
        spiller1.bottom = skjerm_høyde

#funskjonen styrer spiller2 automatisk
def spiller2AI():
    if spiller2.top < ball.y: #sjekker y kordinaten opp mat ballen 
        spiller2.top += spiller2_fart #endrer deretter
    if spiller2.bottom > ball.y: #samme her bare i negativ retning
        spiller2.bottom -= spiller2_fart
    if spiller2.top <= 0: # passer på at spiller 2 ikke beveger seg ut at bildet 
        spiller2.top = 0
    if spiller2.bottom >= skjerm_høyde:
        spiller2.bottom = skjerm_høyde

def ball_restart(): # funksjon som kan restarte ballen
    global ball_fart_x, ball_fart_y
    ball.center = (skjerm_bredde/2,skjerm_høyde/2) #plaserer den i sentrum
    ball_fart_y *= random.choice((1,-1)) #gjør retningen den starter i tilfeldig
    ball_fart_x *= random.choice((1,-1))
#setup
#gjør klart slik at pygame kan kjøre
pygame.init()
klokke = pygame.time.Clock() #variabel for tid

#sette opp spillvinduet
skjerm_bredde = 1100 #bredde i px
skjerm_høyde = 670 #høyde i px
#koden som kjører vinduet, tar inn variablene
skjerm = pygame.display.set_mode((skjerm_bredde,skjerm_høyde))
pygame.display.set_caption('Pong')

#farger
bakgrunn_farge = pygame.Color("grey12")
grå = (200,200,200)

#ting i spillet bruker rect for rektangeler
ball = pygame.Rect(skjerm_bredde/2 - 15,skjerm_høyde/2 - 15,30,30)
spiller1 = pygame.Rect(skjerm_bredde-20,skjerm_høyde/2 - 70,10,140)
spiller2 = pygame.Rect(10,skjerm_høyde/2 - 70,10,140)

#animasjoner/fart per gang spille blir oppdatert 
ball_fart_x = 7 * random.choice((1,-1)) #gjør farten tilfeldig nå spillet starter
ball_fart_y = 7
spiller1_fart = 0
spiller2_fart = 7

while True: #loop for å holde vinduet åpent 
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT: #avslutter spillet
            pygame.quit()
            sys.exit()
        if hendelse.type == pygame.KEYDOWN: #sjekker hvis nedoverpil er manipulert
            if hendelse.key == pygame.K_DOWN: #hvis det er pil ned 
                spiller1_fart += 7 #øk farten
            if hendelse.key == pygame.K_UP: #hvis blir tatt opp senk farten
                spiller1_fart -= 7
        if hendelse.type == pygame.KEYUP: #sjekker hvis
            if hendelse.key == pygame.K_DOWN:
                spiller1_fart -= 7
            if hendelse.key == pygame.K_UP:
                spiller1_fart += 7
                     
    ball_animasjon() # kaller funksjonene oppe 
    spiller1_animasjon()
    spiller2AI()
 
    
    #visuelt
    skjerm.fill(bakgrunn_farge) #lager bakgrunnen grå
    pygame.draw.rect(skjerm,grå,spiller1) #spiller1
    pygame.draw.rect(skjerm,grå,spiller2) #spiller2
    pygame.draw.ellipse(skjerm,grå,ball) #ball, selv om den egt er en firkant blir den rund
    pygame.draw.aaline(skjerm,grå,(skjerm_bredde/2,0),(skjerm_bredde/2,skjerm_høyde)) #linje som deler midten
    
    #oppdaterer vinduet
    pygame.display.flip() #gjør om slik at man kan se figurene
    klokke.tick(60) # setter til 60 frames per second
    
    