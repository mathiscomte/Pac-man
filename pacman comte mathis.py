"""
Programme réalisé par comte, mathis, 1G4
"""
import pygame

#variables du niveau
NB_TILES = 30   #nombre de tiles a chager (ici de 00.png à 26.png) 27 au total !!
TITLE_SIZE=32   #definition du dessin (carré)
largeur=28       #hauteur du niveau 28
hauteur=28       #largeur du niveau 32
tiles=[]       #liste d'images tiles

#variables de gestion du pacman
pacX=13          #position x y du pacman dans le niveau
pacY=22
compteurBilles=0

#variables de gestion du fantome
FRAMERATE_FANTOME= 10      #vitesse du fantome chiffre elevé = vitesse lente
NB_DEPLACEMENT_FANTOME = 89   #le fantome se deplace sur 9 cases
positionFantome=1
frameRateCounterFantome=5
posfX=13     #position initiale du fantome
posfY=10

#definition du niveau

niveau=[[1,5,5,5,5,5,5,5,5,5,5,5,5,10,10,5,5,5,5,5,5,5,5,5,5,5,5,2],
     [6,12,12,12,12,12,12,12,12,12,12,12,12,6,6,12,12,12,12,12,12,12,12,12,12,12,12,6],
     [6,12,1,5,5,2,12,1,5,5,5,2,12,6,6,12,1,5,5,5,2,12,1,5,5,2,12,6],
     [6,12,3,5,5,4,12,3,5,5,5,4,12,3,4,12,3,5,5,5,4,12,3,5,5,4,12,6],
     [6,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,6],
     [6,12,1,5,5,2,12,1,2,12,1,5,5,5,5,5,5,2,12,1,2,12,1,5,5,2,12,6],
     [6,12,3,5,5,4,12,6,6,12,3,5,5,2,1,5,5,4,12,6,6,12,3,5,5,4,12,6],
     [6,12,12,12,12,12,12,6,6,12,12,12,12,6,6,12,12,12,12,6,6,12,12,12,12,12,12,6],
     [3,5,5,5,5,2,12,6,3,5,5,2,0,6,6,0,1,5,5,4,6,12,1,5,5,5,5,4],
     [0,0,0,0,0,6,12,6,1,5,5,4,0,3,4,0,3,5,5,2,6,12,6,0,0,0,0,0],
     [0,0,0,0,0,6,12,6,6,0,0,0,0,0,0,0,0,0,0,6,6,12,6,0,0,0,0,0],
     [0,0,0,0,0,6,12,6,6,0,1,5,5,24,23,5,5,2,0,6,6,12,6,0,0,0,0,0],
     [5,5,5,5,5,4,12,3,4,0,6,0,0,0,0,0,0,6,0,3,4,12,3,5,5,5,5,5],
     [0,0,0,0,0,0,12,0,0,0,6,0,0,0,0,0,0,6,0,0,0,12,0,0,0,0,0,0],
     [5,5,5,5,5,2,12,1,2,0,6,0,0,0,0,0,0,6,0,1,2,12,1,5,5,5,5,5],
     [0,0,0,0,0,6,12,6,6,0,3,5,5,5,5,5,5,4,0,6,6,12,6,0,0,0,0,0],
     [0,0,0,0,0,6,12,6,6,0,0,0,0,0,0,0,0,0,0,6,6,12,6,0,0,0,0,0],
     [0,0,0,0,0,6,12,6,3,5,5,2,0,1,2,0,1,5,5,4,6,12,6,0,0,0,0,0],
     [1,5,5,5,5,4,12,6,1,5,5,4,0,6,6,0,3,5,5,2,6,12,3,5,5,5,5,2],
     [6,12,12,12,12,12,12,6,6,12,12,12,12,6,6,12,12,12,12,6,6,12,12,12,12,12,12,6],
     [6,12,1,5,5,2,12,6,6,12,1,5,5,4,3,5,5,2,12,6,6,12,1,5,5,2,12,6],
     [6,12,3,5,5,4,12,3,4,12,3,5,5,5,5,5,5,4,12,3,4,12,3,5,5,4,12,6],
     [6,12,12,12,12,12,12,12,12,12,12,12,12,0,0,12,12,12,12,12,12,12,12,12,12,12,12,6],
     [6,12,1,5,5,2,12,1,5,5,5,2,12,1,2,12,1,5,5,5,2,12,1,5,5,2,12,6],
     [6,12,3,5,5,4,12,3,5,5,5,4,12,6,6,12,3,5,5,5,4,12,3,5,5,4,12,6],
     [6,12,12,12,12,12,12,12,12,12,12,12,12,6,6,12,12,12,12,12,12,12,12,12,12,12,12,6],
     [7,5,5,5,5,5,5,5,5,5,5,5,5,8,8,5,5,5,5,5,5,5,5,5,5,5,5,9],
     [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6]]




fantome=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,67,68,69,70,71,72,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,66,0,0,0,0,0,74,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,65,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,64,0,0,79,78,77,76,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,63,0,0,80,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,62,0,0,81,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,61,0,0,82,83,84,85,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,60,0,0,0,0,0,86,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,59,0,0,0,0,0,87,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,58,0,0,0,0,0,88,1,2,3,4,5,6,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,57,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,56,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,55,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,54,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,53,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,52,0,0,0,0,0,0,0,0,15,14,13,12,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,51,0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,17,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,44,45,46,47,48,49,0,0,0,0,0,0,0,0,18,19,20,21,0,0,0,0,0,0,0,0,0],
     [0,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,22,0,0,0,0,0,0,0,0,0],
     [0,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,23,0,0,0,0,0,0,0,0,0],
     [0,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur)*TITLE_SIZE))
pygame.display.set_caption("Pac-Man")
font = pygame.font.Font('freesansbold.ttf', 20)

def chargetiles(tiles):
    """
    fonction permettant de charger les images tiles dans une liste tiles[]
    """
    for n in range(0,NB_TILES):
        #print('data/'+str(n)+'.png')
        tiles.append(pygame.image.load('data/'+str(n)+'.png')) #attention au chemin


def afficheNiveau(niveau):
    """
    affiche le niveau a partir de la liste a deux dimensions niveau[][]
    """
    for y in range(hauteur):
        for x in range(largeur):
            fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))


def affichePac(numero):
    """
    affiche le pacman en position pacX et pacY
    """
    fenetre.blit(tiles[numero],(pacX * TITLE_SIZE,pacY * TITLE_SIZE))

def afficheScore(score):
    """
    affiche le score
    """
    scoreAafficher = font.render("score : "+str(score), True, (0, 255, 0))
    fenetre.blit(scoreAafficher,(120,865))


def calculScore():
    nbBalles=0
    for i in range(len(niveau)):
        for y in range(len(niveau[i])):
            if niveau[i][y]==12:
                nbBalles+=1
    remainAfficher = font.render("billes restantes : "+str(nbBalles), True, (0, 255, 0))
    fenetre.blit(remainAfficher,(240,865))
    if nbBalles==0:win='o'
    else:win='n'
    return win

def afficheVies(vies):
    if vies>=1:
        fenetre.blit(tiles[14],(24* TITLE_SIZE,27 * TITLE_SIZE))
    if vies>=2:
        fenetre.blit(tiles[14],(25* TITLE_SIZE,27 * TITLE_SIZE))
    if vies>=3:
        fenetre.blit(tiles[14],(26* TITLE_SIZE,27 * TITLE_SIZE))




def rechercheFantome(fantome,position): #recherche les coord du fantome dans la liste fantome
    """
    recherche les coordonnées du fantome en fonction du numéro de sa postion dans le parcours
    """
    global pacX
    global pacY
    global vies
    global imgpac
    print(position)                     #la position doit etre dans la liste fantome sinon plantage
    for y in range(hauteur):
        for x in range(largeur):
            if fantome[y][x]==position:
                coodFantome=x,y
    if coodFantome[0]==pacX:
        if coodFantome[1]==pacY:
            vies-=1
            pacX=13
            pacY=22
            imgpac=14


    return coodFantome          #les coord du fantome x et y sont dans un tuple coodFantome

def deplaceFantome(fantome):
    """
    Incrémente automatiquement le déplacement du fantome, gère sa vitesse et son affichage
    """
    global frameRateCounterFantome
    global positionFantome
    global posfX,posfY
    global vies
    global pacX
    global pacY
    if frameRateCounterFantome==FRAMERATE_FANTOME:      #ralentit la viteese du fantome
        posfX,posfY=rechercheFantome(fantome,positionFantome)   #deballage du tuple coordonnées du fantome
        positionFantome+=1
        if positionFantome==NB_DEPLACEMENT_FANTOME:     #un tour est fait donc on passe à la 1ere position
            positionFantome=1
        frameRateCounterFantome=0                       #compteur de vitesse à zero
    fenetre.blit(tiles[15],(posfX * TITLE_SIZE,posfY * TITLE_SIZE)) #affichage du fantome
    frameRateCounterFantome+=1                        #incrémentation du compteur de vitesse

def initialise():
    global pacX
    global pacY




winAfficher=font.render("You win the game !", True, (255, 255, 0))
loseAfficher=font.render("Game Over", True, (255,0, 0))
playAfficher=font.render("Play again?", True, (0, 255, 0))



chargetiles(tiles)  #chargement des images
imgpac=14

vies=3
numeroTile=0

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
            elif event.key == pygame.K_UP:    #est-ce la touche UP
                posY = pacY - 1             #on deplace le pacman vituellement
                posX = pacX
                numeroTile = niveau[posY][posX]       #on regarde le numéro du tile
                print("up",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 13):   #si le tile est une bille ou un fond noir alors le déplacement est possible
                    pacY -= 1                               #on monte donc il faut décrémenter pacY
                    print("deplacement possible",pacX,pacY)
                    imgpac=29
                else:
                    print("deplacement impossible")

            elif event.key == pygame.K_DOWN:  #est-ce la touche DOWN
                posY = pacY + 1
                posX = pacX
                numeroTile = niveau[posY][posX]
                print("down",numeroTile,end=':')
                if (numeroTile == 12 or numeroTile == 0 or numeroTile == 13):
                    pacY += 1
                    print("deplacement possible",pacX,pacY)
                    imgpac=27
                else:
                    print("deplacement impossible")

            elif event.key == pygame.K_RIGHT:  #est-ce la touche RIGHT
                if pacX==27:
                    imgpac=14
                    pacX=0
                else:
                    pass
                    posX = pacX + 1
                    posY = pacY
                    numeroTile = niveau[posY][posX]
                    print("down",numeroTile,end=':')
                    if (numeroTile == 12 or numeroTile == 0 or numeroTile == 13):
                        pacX += 1
                        print("deplacement possible",pacX,pacY)
                        imgpac=14


            elif event.key == pygame.K_LEFT:  #est-ce la touche LEFT
                if pacX==0:
                    imgpac=28
                    pacX=27
                else:
                    pass
                    posX = pacX - 1
                    posY = pacY
                    numeroTile = niveau[posY][posX]
                    print("up",numeroTile,end=':')
                    if (numeroTile == 12 or numeroTile == 0 or numeroTile == 13):
                        pacX -= 1
                        print("deplacement possible",pacX,pacY)
                        imgpac=28
                    else:
                        print("deplacement impossible")


            if (numeroTile==12):  #si le numero du tile est 12 c'est que l'on est sur une nouvelle bille
                compteurBilles+=1   #alors on incrémente le score
                niveau[posY][posX]=0    #et on efface la bille dans le niveau
                print("nouvelle bille")
            else:
                print("fond noir")
            print(pacX,pacY)






    fenetre.fill((0,0,0))   #efface la fenetre
    afficheNiveau(niveau)   #affiche le niveau
    affichePac(imgpac)          #affiche la pacman et le score
    deplaceFantome(fantome) #mettre un commentaire pour desactiver le déplacement du fantome
    afficheScore(compteurBilles)
    afficheVies(vies)
    calculScore()
    if calculScore()=='o' or vies==0:
        if calculScore()=='o':
            fenetre.blit(winAfficher,(360,410))
        else:
            fenetre.blit(loseAfficher,(390,400))
        fenetre.blit(playAfficher,(390,440))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:  #lecture du clavier
                if event.unicode =='o':
                    niveau=[[1,5,5,5,5,5,5,5,5,5,5,5,5,10,10,5,5,5,5,5,5,5,5,5,5,5,5,2],
                        [6,12,12,12,12,12,12,12,12,12,12,12,12,6,6,12,12,12,12,12,12,12,12,12,12,12,12,6],
                        [6,12,1,5,5,2,12,1,5,5,5,2,12,6,6,12,1,5,5,5,2,12,1,5,5,2,12,6],
                        [6,12,3,5,5,4,12,3,5,5,5,4,12,3,4,12,3,5,5,5,4,12,3,5,5,4,12,6],
                        [6,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,6],
                        [6,12,1,5,5,2,12,1,2,12,1,5,5,5,5,5,5,2,12,1,2,12,1,5,5,2,12,6],
                        [6,12,3,5,5,4,12,6,6,12,3,5,5,2,1,5,5,4,12,6,6,12,3,5,5,4,12,6],
                        [6,12,12,12,12,12,12,6,6,12,12,12,12,6,6,12,12,12,12,6,6,12,12,12,12,12,12,6],
                        [3,5,5,5,5,2,12,6,3,5,5,2,0,6,6,0,1,5,5,4,6,12,1,5,5,5,5,4],
                        [0,0,0,0,0,6,12,6,1,5,5,4,0,3,4,0,3,5,5,2,6,12,6,0,0,0,0,0],
                        [0,0,0,0,0,6,12,6,6,0,0,0,0,0,0,0,0,0,0,6,6,12,6,0,0,0,0,0],
                        [0,0,0,0,0,6,12,6,6,0,1,5,5,24,23,5,5,2,0,6,6,12,6,0,0,0,0,0],
                        [5,5,5,5,5,4,12,3,4,0,6,0,0,0,0,0,0,6,0,3,4,12,3,5,5,5,5,5],
                        [0,0,0,0,0,0,12,0,0,0,6,0,0,0,0,0,0,6,0,0,0,12,0,0,0,0,0,0],
                        [5,5,5,5,5,2,12,1,2,0,6,0,0,0,0,0,0,6,0,1,2,12,1,5,5,5,5,5],
                        [0,0,0,0,0,6,12,6,6,0,3,5,5,5,5,5,5,4,0,6,6,12,6,0,0,0,0,0],
                        [0,0,0,0,0,6,12,6,6,0,0,0,0,0,0,0,0,0,0,6,6,12,6,0,0,0,0,0],
                        [0,0,0,0,0,6,12,6,3,5,5,2,0,1,2,0,1,5,5,4,6,12,6,0,0,0,0,0],
                        [1,5,5,5,5,4,12,6,1,5,5,4,0,6,6,0,3,5,5,2,6,12,3,5,5,5,5,2],
                        [6,12,12,12,12,12,12,6,6,12,12,12,12,6,6,12,12,12,12,6,6,12,12,12,12,12,12,6],
                        [6,12,1,5,5,2,12,6,6,12,1,5,5,4,3,5,5,2,12,6,6,12,1,5,5,2,12,6],
                        [6,12,3,5,5,4,12,3,4,12,3,5,5,5,5,5,5,4,12,3,4,12,3,5,5,4,12,6],
                        [6,12,12,12,12,12,12,12,12,12,12,12,12,0,0,12,12,12,12,12,12,12,12,12,12,12,12,6],
                        [6,12,1,5,5,2,12,1,5,5,5,2,12,1,2,12,1,5,5,5,2,12,1,5,5,2,12,6],
                        [6,12,3,5,5,4,12,3,5,5,5,4,12,6,6,12,3,5,5,5,4,12,3,5,5,4,12,6],
                        [6,12,12,12,12,12,12,12,12,12,12,12,12,6,6,12,12,12,12,12,12,12,12,12,12,12,12,6],
                        [7,5,5,5,5,5,5,5,5,5,5,5,5,8,8,5,5,5,5,5,5,5,5,5,5,5,5,9],
                        [6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6]]
                    afficheNiveau(niveau)
                    pacX=13
                    pacY=22
                    compteurBilles=0
                    vies=3
                    imgpac=14
                    positionFantome=1
                elif event.unicode =='n':
                    loop=False
                elif event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                    loop = False
                else:print("La réponse doit être 'o' ou 'n'")

    pygame.display.update() #met à jour la fentre graphique

pygame.quit()