from Voiture import Voiture

voiture_1 = Voiture(0, 'peugeot')
voiture_2 = Voiture(150, 'mercedes')

print('----1----')
print(voiture_1)
print(voiture_2)

voiture_1.augmentation_vitesse(100)
voiture_2.diminution_vitesse(200)

print('----2----')
print(voiture_1)
print(voiture_2)

print('----3----')
print(voiture_1.obtention_vitesse())
print(voiture_2.obtention_vitesse())


