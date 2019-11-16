import time
import chess
from random import randint, choice

nbNoeuds=0
niveau =0
def randomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles. Pour avoir un choix au hasard, il faut
    construire explicitement tous les mouvements. Or, generate_legal_moves() nous donne un itérateur.'''
    return choice([m for m in b.generate_legal_moves()])

def deroulementRandom(b):
    '''Déroulement d'une partie d'échecs au hasard des coups possibles. Cela va donner presque exclusivement
    des parties très longues et sans gagnant. Cela illustre cependant comment on peut jouer avec la librairie
    très simplement.'''
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(randomMove(b))
    deroulementRandom(b)
    b.pop()

t= time.time()
board = chess.Board()

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


def rechercheEnProfondeurAvecTemps(b,profondeur):
    global nbNoeuds
    nbNoeuds+=1

    if b.is_game_over():
        return profondeur

    if time.time()-t >= 30:
        return profondeur

    for move in b.generate_legal_moves():
        b.push(move)
        rechercheEnProfondeurAvecTemps(b,profondeur+1)
        b.pop()


def rechercheEnProfondeurAvecMax(b,niveau,max):
    global nbNoeuds
    nbNoeuds+=1

    if b.is_game_over() or niveau >=max :
        return 
        
    for move in b.generate_legal_moves():
        b.push(move)
        rechercheEnProfondeurAvecMax(b,niveau+1,max)
        b.pop()

# rechercheEnProfondeurAvecMax(board,0,5)
print(nbNoeuds)


def deroulementMatch(b,blancJoue):
    print("\n")
    print(b)
    
    if(b.is_game_over()):
        print("Resultat: ",b.result())
        return
    if(not blancJoue):
        moves= IaMinMax(b,1, True)
        b.push(choice([m for m in moves]))
        deroulementMatch(b,not blancJoue)
        b.pop()
        else:
            moves= IaMinMax(b,2, True)
            b.push(choice([m for m in moves]))
            deroulementMatch(b,not blancJoue)
            b.pop()

def evaluateBoard(b):
    dic = { 'k':200 , 'q':9, 'r':5 , 'b':3 ,'n':3, 'p':1}
    result =0
    for key,pieces in b.piece_map().items():
            if(str(pieces) in dic.keys()):
                result+= dic[str(pieces)]

            elif(str(pieces).lower() in dic.keys()):
                result -=dic[str(pieces).lower()]
    return result


print(evaluateBoard(board))
deroulementMatch(board,True)

