# Révision 2e degré

**Mathématiques**

---

## Généralités

Une fonction polynôme du second degré, appelée aussi **trinôme du second degré**, peut s'écrire sous trois formes.

### 1. Forme développée

$$
f(x) = ax^2 + bx + c
$$

où :

- $a$, $b$ et $c$ sont des nombres réels ;
- $a \neq 0$.

En effet, si $a = 0$, l'expression ne contient plus de terme en $x^2$ et la fonction n'est plus une fonction polynôme du second degré. Les coefficients $b$ et $c$ peuvent être nuls. La fonction reste alors un polynôme du second degré tant que $a \neq 0$.

**Utilité**

La forme développée permet :

- de calculer facilement l'image d'un nombre ;
- d'identifier directement les coefficients $a$, $b$ et $c$ ;
- de calculer le discriminant $\Delta = b^2 - 4ac$.

### 2. Forme canonique

$$
f(x) = a(x - \alpha)^2 + \beta
$$

L'extremum de la parabole a pour coordonnées :

$$
S(\alpha \,;\, \beta).
$$

**Utilité**

La forme canonique permet :

- de déterminer rapidement le sommet de la parabole ;
- de dresser le tableau de variations de la fonction ;
- de connaître la valeur minimale ou maximale de la fonction ;
- de tracer plus facilement la courbe représentative.

### 3. Forme factorisée

$$
f(x) = a(x - x_1)(x - x_2)
$$

où $x_1$ et $x_2$ sont les racines de l'équation :

$$
f(x) = 0.
$$

**Utilité**

La forme factorisée permet :

- de résoudre rapidement l'équation $f(x) = 0$ ;
- de déterminer les racines du trinôme ;
- de dresser facilement le tableau de signes de la fonction ;
- de résoudre des inéquations du second degré.

---

## Applications

### App n°1

Dresser le tableau de variations sur $\mathbb{R}$ de la fonction $f$ définie par

$$
f(x) = -3(x + 2)^2 + 3.
$$

### Correction

Dressons le tableau de variations de la fonction $f$.

La fonction est donnée sous forme canonique :

$f(x) = a(x - \alpha)^2 + \beta$

On identifie : $a = -3 \qquad \alpha = -2 \qquad \beta = 3.$

Comme $a = -3 < 0$, la fonction admet donc un maximum égal à $3$, atteint pour $x = -2$. Ainsi :

- $f$ est croissante sur $]-\infty \,;\, -2]$ ;
- $f$ est décroissante sur $[-2 \,;\, +\infty[$.

On obtient donc le tableau de variations suivant :

| $x$ | $-\infty$ | $-2$ | $+\infty$ |
|:---:|:---:|:---:|:---:|
| $f(x)$ | $\nearrow$ | $3$ (maximum) | $\searrow$ |

### App n°2

Dresser le tableau de variations sur $\mathbb{R}$ de la fonction $f$ définie par

$$
f(x) = (x - 10)^2.
$$

### Correction

Dressons le tableau de variations de la fonction $f$.

La fonction est donnée sous forme canonique :

$f(x) = a(x - \alpha)^2 + \beta$

On identifie : $a = 1 \qquad \alpha = 10 \qquad \beta = 0.$

Comme $a = 1 > 0$, la fonction admet donc un minimum égal à $0$, atteint pour $x = 10$. Ainsi :

- $f$ est décroissante sur $]-\infty \,;\, 10]$ ;
- $f$ est croissante sur $[10 \,;\, +\infty[$.

On obtient donc le tableau de variations suivant :

| $x$ | $-\infty$ | $10$ | $+\infty$ |
|:---:|:---:|:---:|:---:|
| $f(x)$ | $\searrow$ | $0$ (minimum) | $\nearrow$ |

### App n°3

Résoudre les équations et inéquations suivantes :

1. $2x^2 - 3x + 1 = 0$
2. $-2x^2 + 5x + 3 \geq 0$

### Correction

**1. Résolvons l'équation $2x^2 - 3x + 1 = 0$.**

Posons $f(x) = 2x^2 - 3x + 1$, avec $a = 2$, $b = -3$ et $c = 1$. Les solutions de l'équation sont les racines du trinôme $f(x)$.

On a :

$$
\Delta = b^2 - 4ac = (-3)^2 - 4 \times 2 \times 1 = 9 - 8 = 1.
$$

Comme $\Delta > 0$, le trinôme admet deux racines distinctes :

$$
x_1 = \frac{-b - \sqrt{\Delta}}{2a} = \frac{3 - 1}{4} = \frac{1}{2}
\qquad \text{et} \qquad
x_2 = \frac{-b + \sqrt{\Delta}}{2a} = \frac{3 + 1}{4} = 1.
$$

Ainsi, l'ensemble des solutions est :

$$
\boxed{S_{\mathbb{R}} = \left\{\frac{1}{2} \,;\, 1\right\}}
$$

**2. Résolvons l'inéquation $-2x^2 + 5x + 3 \geq 0$.**

Posons $g(x) = -2x^2 + 5x + 3$, avec $a = -2$, $b = 5$ et $c = 3$.

On a :

$$
\Delta = b^2 - 4ac = 5^2 - 4 \times (-2) \times 3 = 25 + 24 = 49.
$$

Comme $\Delta > 0$, le trinôme admet deux racines distinctes :

$$
x_1 = \frac{-b - \sqrt{\Delta}}{2a} = \frac{-5 - 7}{-4} = \frac{-12}{-4} = 3
\qquad \text{et} \qquad
x_2 = \frac{-b + \sqrt{\Delta}}{2a} = \frac{-5 + 7}{-4} = \frac{2}{-4} = -\frac{1}{2}.
$$

Comme $a = -2 < 0$, le trinôme est positif **entre** ses racines et négatif en dehors. Ainsi :

$$
g(x) \geq 0 \iff x \in \left[-\frac{1}{2} \,;\, 3\right].
$$

L'ensemble des solutions est donc :

$$
\boxed{S_{\mathbb{R}} = \left[-\frac{1}{2} \,;\, 3\right]}
$$

> **NB :** Si tu veux, tu peux établir le tableau de signes avant d'en déduire l'ensemble des solutions. Si tu penses que ça va te prendre du temps, tu laisses. Il est important de noter que ça t'aide toi-même à vite retrouver l'ensemble des solutions.

---

## Réflexes

1. Pour un tableau de variations $\implies$ il te faut la forme canonique et le signe de $a$.
2. Pour une équation $\implies$ il te faut les racines.
3. Tableau de signes $\implies$ il te faut les racines éventuelles et le signe de $a$.
   - Si tu as déjà la forme factorisée, tant mieux : donne directement le signe de $a$.
   - Si tu as la forme développée, applique la méthode habituelle (calcul de $\Delta$).
   - Si tu as la forme canonique et que $\beta \neq 0$, alors développe pour trouver $a$, $b$ et $c$.
4. Pour une inéquation $\implies$ même principe que le tableau de signes.
5. Souvent, on peut te demander de trouver le signe de la fonction suivante :

$$
f(x) = (x - 2)(-2x^2 + 5x + 3).
$$

Pour résoudre cela, il suffit de remarquer que tu as une expression affine $\times$ un trinôme. On va poser $g(x) = -2x^2 + 5x + 3$ et déterminer les racines de $g(x)$, soit :

$$
x_1 = 3 \quad \text{et} \quad x_2 = -\frac{1}{2}.
$$

On dresse alors le tableau de signes :

| $x$ | $-\infty$ | | $-\frac{1}{2}$ | | $2$ | | $3$ | | $+\infty$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $x - 2$ | | $-$ | $\vert$ | $-$ | $0$ | $+$ | $\vert$ | $+$ | |
| $-2x^2 + 5x + 3$ | | $-$ | $0$ | $+$ | $\vert$ | $+$ | $0$ | $-$ | |
| $f(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | $0$ | $-$ | |

On en déduit le signe de $f$ :

- $f(x) > 0$ sur $\left]-\infty \,;\, -\frac{1}{2}\right[ \cup \left]2 \,;\, 3\right[$ ;
- $f(x) = 0$ pour $x = -\frac{1}{2}$, $x = 2$ et $x = 3$ ;
- $f(x) < 0$ sur $\left]-\frac{1}{2} \,;\, 2\right[ \cup \left]3 \,;\, +\infty\right[$.

> **NB :** N'hésite pas si tu as besoin de comprendre quelque chose vite fait.
