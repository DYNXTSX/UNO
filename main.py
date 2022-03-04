from enum import Enum
import random


class Couleurs(Enum):
    BLEU = 1
    ROUGE = 2
    JAUNE = 3
    VERT = 4


class Chiffres(Enum):
    UN = 1
    DEUX = 2
    TROIS = 3
    QUATRE = 4
    CINQ = 5
    SIX = 6
    SEPT = 7
    HUITE = 8
    NEUF = 9


class Carte:
    def __init__(self, color, number):
        self.couleur = color
        self.chiffre = number

    def __str__(self):
        return f' {self.chiffre} de couleur {self.couleur}'

    # Question 2
    def equalsCards(self, card2):
        return (self.couleur == card2.couleur) or (self.chiffre == card2.chiffre)


class Deck:
    def __init__(self, nbCartes=80):
        self.cartes = []
        i = 0
        while i < nbCartes:
            for c in Couleurs:
                for n in Chiffres:
                    self.cartes.append(Carte(c.name, n.name))
                    i += 1
                    if i >= nbCartes:
                        random.shuffle(self.cartes)
                        return  # return pour stoper toutes les boucles

    def get_deck(self):
        return self.cartes

    def get_colorPresent(self):
        listeColors = []
        for c in Couleurs:
            listeColors.append(0)

        for carte in self.cartes:
            



class Player:
    def __init__(self, pseudo):
        self.name = pseudo
        self.main = []

    def piocher(self, carte):
        self.main.append(carte)

    def get_main(self):
        return self.main


class Partie:
    def __init__(self, nbCartes, nbJoueurs, cartesParJoueurs):
        self.joueurs = []
        self.cpj = cartesParJoueurs
        self.pioche = Deck(nbCartes).get_deck()
        for i in range(nbJoueurs):
            self.joueurs.append(Player("Joueur"+str(i)))

    def get_pioche(self):
        return self.pioche

    # Question 3
    def distribuerCartes(self):
        for i in range(self.cpj):
            for j in self.joueurs:
                j.piocher(self.pioche[0])
                self.pioche.remove(self.pioche[0])

    def afficherMains(self):
        for p in self.joueurs:
            print(p.name)
            for c in p.main:
                print(c.__str__())


if __name__ == '__main__':
    # Question 1
    partie = Partie(80, 2, 7)
    pioche = partie.pioche

    #for c in pioche:
    #    print(str(pioche.index(c)) + " " + c.__str__())
    #print("Il y a une pioche de " + str(len(pioche)) + " cartes !")

    # Question 2
    #carte1 = Carte("BLEU", "SEPT")
    #carte2 = Carte("BLEU", "SIX")
    #print(carte1.equalsCards(carte2))

    # Question 3
    partie.distribuerCartes()
    partie.afficherMains()

    print("Il y a une pioche de " + str(len(pioche)) + " cartes !")

    # Question 4
