

import pygame
import random
import os 

pygame.init() 

import threading
import time

#----------------------------------------------------#
#------------- Initiation des variables -------------# 
#----------------------------------------------------#

gameOn = False 

countGame = 0               ## Compteur de manches
countScore = 0              ## Compteur du score
highScore = 0               ## Meilleur score

affichageFont = 'comicsans'   ## Police d'affichage
affichageSize = 30            ## Taille des affichages
SpeedType = pygame.font.SysFont(affichageFont, affichageSize - 10)    ## Caractéristiques de l'affichage de la vitesse (police et taille)
ScoreType = pygame.font.SysFont(affichageFont, affichageSize)         ## Caractéristiques de l'affichage du score (police et taille)
HighScoreType = pygame.font.SysFont(affichageFont, affichageSize)     ## Caractéristiques de l'affichage du high score (police et taille)
gameOnType = pygame.font.SysFont(affichageFont, affichageSize + 10)   ## Caractéristiques de l'affichage du message de lancement du jeu (police et taille)


largeur = 800             
hauteur = 600 #souvenir oiseau < hauteur et oisueur > hauteur = meurt car sort de la fenêtre
alignBottom = 350           
alignLeft = 20  

blanc = (255, 255, 255)    
noir = (0, 0, 0)            

isJumping = False           ## Pour vérifier si l'image est en train de sauter
jumpUp = 7.5                 ## Vitesse verticale initiale
jumpGravity = 0        
jumpVelocity = 0            ## Vitesse verticale 

compteur = 0

linuxWidth = 100             ## Largeur du dino
linuxHeight = 125            ## Hauteur du dino
linuxRefY = hauteur-alignBottom-linuxHeight

tuyaudownwidth = 60
tuyaudownheight = 90
tuyautopwidth = tuyaudownwidth
tuyautopheight = tuyaudownheight 

#------------------------------------------------#
#------------- Paramètre des images -------------# 
#------------------------------------------------#


#--- Linux ---#
linuxImage = pygame.image.load(os.path.join('images', 'birdlinux.png'))
## Charge l'image
## La stocke dans une variable pour pouvoir y faire appel plus tard 
linux = pygame.transform.scale(linuxImage, (linuxWidth, linuxHeight))
## Redimensionne l'image aux dimensions définies
## Ecrase l'image originelle par celle redimensionnée
linuxRect = pygame.Rect(alignLeft, linuxRefY, linuxWidth, linuxHeight)
## Crée un rectanlge au dessus de l'image du dino pour gérer les intéractions

#--- Background ---#

backgroundX = 0  
backgroundSpeed = 2


fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Le jeu Flappy Bird")


backgroundImage = pygame.image.load(os.path.join('images', 'Background2.png'))   
background = pygame.transform.scale(backgroundImage, (largeur, hauteur))       

#--- tuyaux ---#
tuyauDX = 400
tuyauDY = 250
tuyauTX = tuyauDX 
tuyauTY = -25

tuyauDWidht = 3000
tuyauDHeight = 5000
tuyauTWidht = tuyauDWidht
tuyauTHeight = tuyauDHeight


tuyaudownimg = pygame.image.load(os.path.join('images', 'ice_pillardown.png'))
tuyaudown = pygame.transform.scale(tuyaudownimg, (tuyauDWidht, tuyauDHeight)) 

tuyautopimg = pygame.image.load(os.path.join('images', 'ice_pillartop.png'))
tuyautop = pygame.transform.scale(tuyautopimg, (tuyauTWidht, tuyauTHeight)) 



#---------------------------------------------#
#------------- Boucle principale -------------# 
#---------------------------------------------#

running = True
## Variable booléenne qui régit l'exécution de la boucle
## La boucle permet de répéter des lignes de code autant de fois que nécessaire
## La boucle est exécutée tant que "running" a la valeur logique True

while running :
    #--------------------------------------------------#
    #------------- Gestion des événements -------------#
    #--------------------------------------------------#

    # Evenement = action / occurence générée par le système / l'utilisateur
    # à laquelle le programme peut réagir
    for event in pygame.event.get() :
        ## pygame.event.get() retourne une liste de tous les événements en attente 
        ### que l’utilisateur a effectués depuis le dernier appel  
        ## for est une boucle qui parcourt chaque événement de cette liste
        if event.type == pygame.QUIT :
            ## Si le type d'événement actuel est "pygame.QUIT"
            ## pygame.QUIT est l'événement quand l’utilisateur 
            ### clique sur le bouton de fermeture de la fenêtre
            running = False
            ## Fait passer la variable booléenne à Faux pour sortir de la boucle de jeu
        if event.type == pygame.KEYDOWN and not(gameOn) :

                    # Lance le jeu avec la barre d'espace
                    if event.key == pygame.K_SPACE :
                                
                        #--- Lance la partie ---#
                        gameOn = True  # Le jeu commence ou reprend  
                        jumpGravity = 0.5   
                        #--- réinitialise les paramètres de début de partie ---#
                        # Vitesse
                    #  obstacleSpeed = initialSpeed

                        # Scores
                        countScore = 0                

                        # Repositionnement de linux à chaque début de partie
                   # linuxRefY = linuxRefY
                   # if linuxRefY < hauteur :
                    #     gameOn = False
                    #elif linuxRefY > hauteur :
                        # gameon = False     
                        # Repositionne les obstacles en début de partie
                        # for i in range(obstacleNombre) : ## Boucle effectuée pour chaque obstacle de la liste
                            # Les éléments obstacles sont de type "Rect". Il possède certains attributs :
                            # obstacle.x = abscisse du coin gauche -/- obstacle.y = ordonnée du coin supérieur
                            # obstacle.right = coordonnée x du côté droit du bloc -/- idem : left, bottom, top
                        # obstaclesRect[i].x = largeur + obstacleSpace * i    ## répartition uniforme des obstacles
                        # obstaclesRect[i].y = obstacleRefY     ## sur la ligne de base


            


    #-------------------------------------------#
    #------------- Gestion du Fond -------------#
    #-------------------------------------------#

    # Mise à jour de l'affichage
    fenetre.fill(blanc)

    # Déplacer le fond vers la gauche
    backgroundX -= backgroundSpeed

    # Réinitialiser la position du fond lorsque la première image disparaît
    if backgroundX <= -largeur :
        backgroundX = 0

    # Dessiner deux images de fond pour créer l'effet de défilement
    ## blit : Affichage (objet, (positionX, positionY))
    fenetre.blit(background, (backgroundX, 0))  # Affichage de l'image de fond principale
    fenetre.blit(background, (backgroundX + largeur, 0))  # Affichage de la deuxième image de fond 
  
  
    #--------------------------------------------#
    #------------- Gestion de linux -------------#
    #--------------------------------------------#
    # Affichage de l'image 'dino'

    fenetre.blit(linux, (linuxRect.x, linuxRect.y))

    # Liste des touches enfoncées
    keys_pressed = pygame.key.get_pressed()
    # Si la touche espace est enfoncée et qu'on est pas déjà pendant un saut
    if keys_pressed[pygame.K_SPACE] and not(isJumping) :
        isJumping = True        ## Indique que le saut commence
        jumpVelocity = -jumpUp  ## Affecte la vitesse verticale de saut

    # Logique de Saut
    jumpVelocity += jumpGravity 
    linuxRect.y += jumpVelocity 
    if isJumping :
        isJumping = False       ## Finir le saut
        

    #----------------------------------------------#
    #------------- Gestion des tuyaux -------------#
    #----------------------------------------------#
    # Affichage des tuyaux
    fenetre.blit(tuyaudownimg, (tuyauDX,tuyauDY ))
    fenetre.blit(tuyautopimg, (tuyauTX,tuyauTY ))


#---------------------------------------------#
#------------- Ecran de contrôle -------------#
#---------------------------------------------#

# Ecran d'attente
    if gameOn == False :     ## Si le jeu n'est pas en cours 
        gamePlay = gameOnType.render("Appuyez sur la barre d'espace", True, noir)   ## Texte de l'écran d'attente
        fenetre.blit(gamePlay, (largeur // 2 - gamePlay.get_width()//2, 150))       ## Affichage du texte de relance
        jumpGravity = 0    
        ## Ecran de relance (s'additionne à l'écran d'attente)
        if countGame >= 1 : ## Dans le cas où au moins une partie a été jouée
            DisplayBravo = gameOnType.render(f"Félicitations !", 1, noir)             ## Texte de l'écran d'attente
            DisplayScore = gameOnType.render(f"Score : {countScore}", 1, noir)           ## Texte de l'affichage du score sur l'écran d'attente
            DisplayHihgScore = HighScoreType.render(f"High Score : {highScore}", 1, noir)   ## Texte de l'affichage du high score sur l'écran d'attente
            fenetre.blit(DisplayBravo, (largeur // 2 - DisplayBravo.get_width()//2, 200))   ## Affichage du texte de félicitations sur l'écran d'attente
            fenetre.blit(DisplayScore, (largeur // 2 - DisplayScore.get_width()//2, 270))   ## Affichage du texte de score sur l'écran d'attente
            fenetre.blit(DisplayHihgScore, (largeur // 2 - DisplayHihgScore.get_width()//2, 320))   ## Affichage du texte de high scoresur l'écran d'attente
      
        
    #----------------------------------------------------------#
    #------------- Rafraichissement de la fenêtre -------------#
    #----------------------------------------------------------#
    # Mise à jour de l'intégralité de la surface d'affichage
    pygame.display.flip()

    # Contrôle de la vitesse de la boucle (FPS)
    pygame.time.Clock().tick(60)

# Quitter Pygame proprement
pygame.quit()