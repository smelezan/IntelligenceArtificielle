# -*- coding: utf-8 -*-

import time
import Reversi
from random import randint
from playerInterface import *
def evaluateBoard(b):
    for x in range(10):
        for y in range (10):
            liste =testAndBuild_ValidMove(self, player, xstart, ystart)
            if(liste):
                
    for move in 
def maxMin(b,profondeur,Ennemi):
    global nbNoeuds
    nbNoeuds+=1
    pire= 800

    if(profondeur==0):
        evaluate = evaluateBoard(b)
        if( Ennemi):
            return evaluate
        else:
            return -evaluate
        
    for move in b.generate_legal_moves():
        b.push(move)
        v = maxMin(b,profondeur-1,Ennemi)
        if v < pire:
            pire = v
        b.pop()

    return pire

def minMax(b,profondeur,Ami):
    global nbNoeuds
    nbNoeuds+=1
    meilleur= -800
    pire= 800

    if(profondeur==0):
        evaluate = evaluateBoard(b)
        if( Ami):
            return evaluate
        else:
            return -evaluate
        
    for move in b.generate_legal_moves():
        b.push(move)
        if(Ami):
            v = minMax(b,profondeur-1,not Ami)
            if v > meilleur:
                meilleur = v
            b.pop()
        else:
            v = maxMin(b,profondeur-1,not Ami)
            if v < pire:
                pire = v
            b.pop()
    if(Ami):
        return meilleur
    else:
        return pire
    

def IaMinMax(b,profondeur,Ami):
    global nbNoeuds
    nbNoeuds+=1
    meilleur=-800
    meilleurCoup=None
    listMoveEgaux=[]
    for move in b.generate_legal_moves():
        b.push(move)
        if(Ami):
            v=minMax(b,profondeur-1,not Ami)
            if v > meilleur or meilleurCoup ==None:
                meilleur= v
                meilleurCoup= move
                listMoveEgaux = [move]
            elif v==meilleur:
                listMoveEgaux.append(move)
        b.pop()
    return listMoveEgaux




class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None

    def getPlayerName(self):
        return "Random Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1,-1)
        moves = [m for m in self._board.legal_moves()]
        move = moves[randint(0,len(moves)-1)]
        self._board.push(move)
        print("I am playing ", move)
        (c,x,y) = move
        assert(c==self._mycolor)
        print("My current board :")
        print(self._board)
        return (x,y) 

    def playOpponentMove(self, x,y):
        assert(self._board.is_valid_move(self._opponent, x, y))
        print("Opponent played ", (x,y))
        self._board.push([self._opponent, x, y])

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")


 
