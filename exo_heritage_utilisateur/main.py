from Utilisateur import Senior, Junior
from projets import projets


paul = Junior("Paul", "Durand")
arthur = Senior("Jean", "Marleau")

print(arthur)
print(paul)

print('---------------')

print('Projets accessible à paul :')
paul.afficher_projets()
print('Projets accessible à arthur :')
arthur.afficher_projets()
