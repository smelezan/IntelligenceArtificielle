# -*- coding: utf-8 -*-

import time
import Reversi
from random import randint
from playerInterface import *
from sys import maxsize



class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None
        self._personalboard= []
        for x in range (10):
            self._personalboard.append([1]*10)
        

    def getPlayerName(self):
        return "Random Player"

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1,-1)
        moves = self.IaAlphaBeta(5)
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

    def alphaBeta(self, depth, alpha, beta, maximizingPlayer,move):
        [player,x,y]= move
        if(depth == 0):
            return self._board.heuristique_Amelioree(self)
        if maximizingPlayer:
            value = -maxsize
            for m in self._board.legal_moves():
                self._board.push(m)
                value = max(value, self.alphaBeta(depth-1, alpha, beta, False,m))
                self._board.pop()
                alpha = max(alpha, value)
                if (alpha >= beta):
                    break
            return value
        else:
            value = maxsize
            for m in self._board.legal_moves():
                self._board.push(m)
                value = min(value, self.alphaBeta(depth-1, alpha, beta, True,m))
                self._board.pop()
                beta = min(value, beta)
                if (alpha >= beta):
                    break
            return value


    def IaAlphaBeta(self, profondeur):

        meilleur = -maxsize
        meilleurCoup = None
        listMoveEgaux = []

        for move in self._board.legal_moves():
            self._board.push(move)
            v = self.alphaBeta(profondeur, -maxsize, maxsize, True,move)
            if v > meilleur or meilleurCoup == None:
                meilleur = v
                meilleurCoup = move
                listMoveEgaux = [move]
            elif v == meilleur:
                listMoveEgaux.append(move)
            self._board.pop()
        return listMoveEgaux

    def evaluate_pos(self,x,y):
        # #avant Coins à éviter
        # if (x == 1 and y == 1) or (x == 8 and y == 8) or (x == 1 and y == 8) or (x == 8 and y == 1):
        #     return -100
        # #Coins très important
        # if (x == 0 and y == 0) or (x == 9 and y == 0) or (x == 0 and y == 9) or (x == 9 and y == 9):
        #     return 100
        # if y==0 or y==9 or x==0 or x==9:
        #     return 20
        
        # return 5
        pass

    def evaluate_board(self):
        res=0
        for i in range(10):
            for j in range(10):
                if self._board[i][j]==self._mycolor:
                    res+=self._personalboard[i][j]
                elif self._board[i][j]!= 0:
                    res -= self._personalboard[i][j]
        return res
        

    def updatePersonalBoard(self):
        #pour le moment le board aura toujours la même valeur
        #les coins:
        self._personalboard[0][0]=5
        self._personalboard[0][9]=5
        self._personalboard[9][0]=5
        self._personalboard[9][9]=5

        #les bords
        for i in range (1,9):
            self._personalboard[i][0]=3
            self._personalboard[0][i]=3
            self._personalboard[i][9]=3
            self._personalboard[9][i]=3
        