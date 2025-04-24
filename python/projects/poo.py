from datetime import datetime


# class Agent:
#     def __init__(self, nom):
#         self.nom = nom
#         self.experience = 0

#     def parler(self):
#         print(f'Bonjour, je suis {self.nom}')

#     def apprendre(self, xp):
#         self.experience += xp
#         print(f'{self.nom} a appris {xp} points. Total : {self.experience}')

# moi = Agent('Jules')
# moi.parler()
# moi.apprendre(10)
# moi.apprendre(30) # Sans self = moi.apprendre(moi, 30) /// self est présent mais invisible



# --------------------------------------------



# class Monstre:
#     def __init__(self, name, pv, damage):
#         self.name = name
#         self.pv = pv
#         self.xp = 1
#         self.damage = damage
    
#     def infos(self):
#         if self.pv <=0:
#             print(f'{self.name} est mort !!!')
#         else:
#             print(f'{self.name} -> Niveau : {self.xp} -> Pv : {self.pv} -> Dégat : {self.damage}')

#     def fight(self, target, count):
#         self.infos()
#         target.infos()
#         print('Début du combat !')
#         for i in range(count):
#             self.pv -= target.damage
#             target.pv -= self.damage

#             if self.pv <= 0 or target.pv <= 0:
#                 break
            
#         print(f'Fin du combat ! Nombre de tour : {i+1}')
#         self.infos()    
#         target.infos()


# orc = Monstre('Orc', 150, 60)
# elfe = Monstre('Elfe', 70, 110)
# dragon = Monstre('Dragon', 780, 430)

# loser = Monstre('Thomas', 50, 10)
# winner = Monstre('Jules', 100, 55)

# loser.fight(winner, 3)



# --------------------------------------------


        