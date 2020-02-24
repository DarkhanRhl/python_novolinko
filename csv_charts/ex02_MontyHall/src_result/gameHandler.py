
# Pour utiliser la fonction randint, qui génère des nombres
# entiers de façon aléatoire:
from random import randint, seed
from strat import Strategie

seed()

class GameHandler:

    def play(self, strategie, nb_tours):
            return [1 if self.playGame(strategie) else 0 for i in range(nb_tours)]

    def playGame(self, strategie):
            portes = [0, 1, 2]
            bonne_porte = randint(0,2)
            premier_choix = randint(0,2)
            portes.remove(premier_choix)
            
            # Le présentateur élimine une porte
            if premier_choix == bonne_porte:
                portes.remove(portes[randint(0,1)])
            else:
                portes = [bonne_porte]
            
            # Le deuxieme choix depend de la strategie
            if strategie == Strategie.CHANGER:
                deuxieme_choix = portes[0]
            elif strategie == Strategie.GARDER:
                deuxieme_choix = premier_choix
            else:
                raise ValueError("Stratégie non reconnue!")
            return deuxieme_choix == bonne_porte
            #TODO ajoutez les graphiques (voir openClassroom)



        