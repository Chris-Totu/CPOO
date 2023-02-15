from Division import Division

calcul_1 = Division(4, 2)           # Crétation d'un objet Division
calcul_1.affichage_fraction()       # Affiche la fraction en console
print(calcul_1.result_division())   # Affiche le résultat de la division

calcul_2 = Division(79, 4)
calcul_2.affichage_fraction()
print(calcul_2.result_division())

calcul_3 = Division(567, 6)
calcul_3.affichage_fraction()
print(calcul_3.result_division())


calcul_3.all_results()              # Affiche tout les calculs qu'il y'a eu dans une liste