#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:34:27 2020

@author: Abdoulaye BA
"""
import matplotlib.pyplot as plt
from scipy import array
#***************************************************
# 1- Enregistrement des données sur un format adapté
#***************************************************
xi= array([18, 7, 14, 31, 21, 5, 11, 16, 26, 29])

yi= array([55, 17, 36, 85, 62, 18, 33, 41, 63, 87])

#*******************************************
# 2- Representation de yi en fonction de xi
#*******************************************
plt.scatter(xi, yi)
#Oui nous pouvons dire du'il existe un soupçon de liaison linéaire entre ces
#deux variables

#**************************************
# 3- Calcul de la moyenne de X et de Y
#**************************************
moyenneX = xi.mean()
moyenneY = yi.mean()

#***********************************
#Calcul de la variance de X et de Y
#***********************************
varX = xi.var()
varY = yi.var()

#************************************
#Calcul de l'ecart type de X et de Y
#************************************
ecarTypeX=xi.std()
ecarTypeY=yi.std()

#***************************
#Calcul de la covariance XY
#***************************
def cov(xi, yi):
       sum = 0
       for i in range(0, len(xi)):
           sum += (xi[i] - moyenneX) * (yi[i] - moyenneY)
       return sum/(len(xi))

CovXY = cov(xi, yi)

#************************************
#Détermination du coef de corrélation
#************************************
r = CovXY / (ecarTypeX * ecarTypeY)

#******************
#Détermination de a
#******************
a = CovXY / varX

#*******************
#Détermination de b
#*******************
b = moyenneY - a * moyenneX

#******************************************************
# 4- Détermination des nouvelles valeurs estimées de Y
#******************************************************    
for k in range(0, len(xi)):
        valY=(a * xi[k]) + b  
        print(valY)
# Valeurs de yi estimées
# 50.2469512195122
# 20.164634146341466
# 39.3079268292683
# 85.79878048780489
# 58.451219512195124
# 14.695121951219514
# 31.103658536585368
# 44.77743902439025
# 72.125
# 80.32926829268294
        
#****************************
# 5- Répresentation graphique
#****************************
dY= (a * xi) + b 
Axes = plt.axes()
plt.xlabel("Abscisses") # nom de l'axe x
plt.ylabel("Ordonnées") # nom de l'axe y
Axes.grid() # Grille de dessin
plt.plot(xi, dY, linewidth=3, color='blue', label = "Données")#Représentation
plt.legend()# Legende du graphe
plt.title("Regression Lineaire") # Titre du graphe
plt.show() 

#***************************************
# 6- Estimation plausible de Y à xi = 21
#***************************************
y21 = a * 21 + b

#*****************************
# 7- Détermination de l'écart
#*****************************
ecart = yi[4] - y21
#la différence entre les points issus des données et la droite
#obtenue par la régression linéaire est appelée Résidus

#***************
# 8- Conclusion
#***************
# oui la droite de regression passe par le point de coordonnée (moyenneX, moyenneY)
