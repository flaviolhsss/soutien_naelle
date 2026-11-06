# Exercices de programmation en Python

**NSI**

---

## Généralités

Pour bien entamer les exercices, il est important de revoir les notions suivantes :

- **Les types et les structures de données :** `int`, `str`, `float`, `list`, `dict`, `set`, `tuple`
- **Les comparaisons :** `==`, `<`, `<=`, `>`, `>=`, `not`, `or`, `and`
- **Les conditions :** `if`, `else`, `elif`
- **Les boucles :** `for`, `while`
- **Les fonctions** et **les classes**

---

## Énoncés

### Exercice n°1 : Table de multiplication

On veut réaliser la table de multiplication de 0 à 10 d'un nombre. Écrire un programme qui demande à l'utilisateur un nombre et affiche sa table de multiplication.

**Exemple d'exécution :**

```text
Saisir un nombre : 8
Table de multiplication de 8 :
8 x 0 = 0
8 x 1 = 8
...
8 x 10 = 80
```

---

### Exercice n°2 : Pair ou impair ?

Écrire une fonction Python nommée `est_pair(n)` qui prend en paramètre un nombre entier `n` (positif ou négatif) et renvoie `True` si le nombre est pair, et `False` s'il est impair.

Tester cette fonction avec un script qui demande un nombre à l'utilisateur.

---

### Exercice n°3 : Recherche du maximum

Écrire une fonction qui prend en paramètre une liste de nombres entiers et qui renvoie la valeur maximale présente dans cette liste, **sans utiliser** la fonction native `max()` de Python.

---

### Exercice n°4 : Tri

Écrire une fonction qui prend en paramètre une liste de nombres et qui renvoie une liste ordonnée, **sans utiliser** les fonctions natives `sort()` et `sorted()` de Python.

---

### Exercice n°5 : Équation du premier degré $ax + b = 0$

Écrire une fonction Python nommée `resoudre_premier_degre(a, b)` qui prend en paramètres deux nombres réels `a` et `b` et qui renvoie la solution de l'équation $ax + b = 0$.

**Exemple d'exécution :**

```text
>>> resoudre_premier_degre(2, -4)
'La solution est x = 2.0'
>>> resoudre_premier_degre(0, 3)
"Aucune solution"
>>> resoudre_premier_degre(0, 0)
"Une infinité de solutions"
```

---

### Exercice n°6 : Équation du second degré $ax^2 + bx + c = 0$

Écrire une fonction Python nommée `resoudre_second_degre(a, b, c)` qui prend en paramètres trois nombres réels `a`, `b` et `c` (avec $a \neq 0$) et qui renvoie les solutions réelles de l'équation $ax^2 + bx + c = 0$.

On rappelle que le discriminant est donné par :

$$
\Delta = b^2 - 4ac
$$

**Exemple d'exécution :**

```text
>>> resoudre_second_degre(1, -3, 2)
'Deux solutions : x1 = 1.0 et x2 = 2.0'
>>> resoudre_second_degre(1, -2, 1)
'Une solution double : x0 = 1.0'
>>> resoudre_second_degre(1, 0, 1)
"Aucune solution réelle"
```
