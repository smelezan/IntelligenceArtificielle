# -*- coding: utf-8 -*-

import time
import Tictactoe 
from random import randint,choice

nbNoeuds =0
nbNoeudsAmelio = 0

def RandomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles'''
    return choice(b.legal_moves())

def deroulementRandom(b):
    '''Effectue un déroulement aléatoire du jeu de morpion.'''
    print("----------")
    print(b)
    if b.is_game_over():
        res = getresult(b)
        if res == 1:
            print("Victoire de X")
        elif res == -1:
            print("Victoire de O")
        else:
            print("Egalité")
        return
    b.push(RandomMove(b))
    deroulementRandom(b)
    b.pop()


def getresult(b):
    '''Fonction qui évalue la victoire (ou non) en tant que X. Renvoie 1 pour victoire, 0 pour 
       égalité et -1 pour défaite. '''
    if b.result() == b._X:
        return 1
    elif b.result() == b._O:
        return -1
    else:
        return 0

def toutesLesParties(b):
    global nbNoeuds
    nbNoeuds+=1
    if (b.is_game_over()):
        return 
    for move in b.legal_moves():
        b.push(move)
        toutesLesParties(b)
        b.pop()

#niveau ami = 0
#niveau ennemi = 1

def MinEtMax(niveau,result):
    if(result == -1 or result == 0):
        return False
    elif(result == 1):
        return True
    return 



def rechercheStrategieGagnante(b,niveau):
    global nbNoeuds
    nbNoeuds +=1
    if (niveau ==0):
        res=True
    else:
        res= False

    if (b.is_game_over()):
        return getresult(b)

    for move in b.legal_moves():
        b.push(move)
        
        if(niveau == 0 ):
            tmp=rechercheStrategieGagnante(b,1-niveau) 
            if(tmp== -1 or tmp ==0 ):
                res = False

        elif( niveau ==1):
            tmp = rechercheStrategieGagnante(b,1-niveau)
            if(tmp == 1):
                res= res or True
            if(tmp == -1 or tmp == 0):
                res = res or False
        
        b.pop()
    return res
    

def rechercheStrategieGagnanteAmelioree(b,niveau):
    global nbNoeudsAmelio
    nbNoeudsAmelio +=1

    if (niveau ==0):
        res=True
    else:
        res= False

    if (b.is_game_over()):
        return getresult(b)

    for move in b.legal_moves():
        b.push(move)
        
        if(niveau == 0 ):
            tmp=rechercheStrategieGagnanteAmelioree(b,1-niveau) 
            if(tmp== -1 or tmp ==0 ):
                res =False
                break
            
        elif( niveau ==1):
            tmp = rechercheStrategieGagnanteAmelioree(b,1-niveau)
            if(tmp == 1):
                break
            if(tmp == -1 or tmp == 0):
                res = res or False
        
        b.pop()
    return res




board = Tictactoe.Board()
# print(board)

### Deroulement d'une partie aléatoire
# deroulementRandom(board)



# print("Apres le match, chaque coup est défait (grâce aux pop()): on retrouve le plateau de départ :")
# print(board)

print(rechercheStrategieGagnante(board,0))

print(nbNoeuds)



