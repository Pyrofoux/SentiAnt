from Sentiant.Model.Point import Point

class MoveManager:

    def __init__(self):
        pass


    @staticmethod
    def checkPauli(positions, other): #Vérifie si les fourmis respectent le principe d'exclusion de Pauli, et renvoient l'index de celles qui ne le font pas
        checkedPoints = []
        checkedIndex = []
        collidingIndex = []

        for index in range(0,len(positions)) :
            if not(positions[index] in other):
                if not (positions[index] in checkedPoints): #S'il n'y a personne sur la case cible
                    checkedPoints.append(positions[index])
                    checkedIndex.append(index)

                else : #S'il y a quelqu'un dans la case cible

                    collidingIndex.append(index) #Rajoute l'index des fourmis/positions actuelemment considérés

                    #Rajoute l'index de la première fourmi à être sur cette case, si pas déjà rajouté
                    i = checkedPoints.index(positions[index])
                    firstIndex = checkedIndex[i]



                    if not (firstIndex in collidingIndex):
                        collidingIndex.append(firstIndex)

            else :
                collidingIndex.append(index)

        return collidingIndex


    @staticmethod
    def calculatePunished(pos,dest, other): #Renvoie les fourmis autorisées à effectuer leur déplacement

        nextTry = dest
        colliding = MoveManager.checkPauli(nextTry, other)

        punished = []
        iter = 0

        while len(colliding) > 0 and iter<100: #Peut-être faire un nombre d'itération max pour éviter que des petits bugs deviennt gros

            #Ajouter la liste des fourmis qui se cognent dans celles à PUNIR
            for i in colliding:
                if not (i in punished):
                    punished.append(i)

            #Nouvelle tentative, en annulant le déplacement de celles  qui se cognent

            nextTry = []

            for index in range(0,len(dest)):
                if index in colliding:
                    nextTry.append(pos[index])
                else:
                    nextTry.append(dest[index])
            colliding = MoveManager.checkPauli(nextTry, other)

            iter=iter+1

        return punished




if __name__ == '__main__':

    _pos =  [Point(0,0), Point(0,1), Point(1,1)]
    _dest = [Point(0,1), Point(0,0), Point(1,0)]
    #(MoveManager.calculateAntsMove(_pos,_dest))print