# El cuerpo de los números complejos 

El cuerpo de los números complejos es un conjunto que _en cierto modo_ contiene a los reales, y con unas operaciones que _en cierto modo_ generalizan las conocidas en los reales. 

En los números reales podemos distinguir dos conjuntos por como se comportan con respecto al producto. Por una parte están los números positivos, es decir, aquellos mayores que cero, cuyo producto es también un número positivo. Y por otra parte están los números negativos, que cumplen que su producto no devuelve un número negativo si no uno positivo. 

DIBUJO

La consecuencia es que el cuadrado de un número real nunca será un número negativo y por lo tanto la ecuación $x^2 + 1 = 0$, donde "$1$", "$0$" y "$x$" representan a números reales, no admite ninguna solución. 

Cuando la ecuación $x^2 = k$ tiene solución, es decir, cuando $k$ no es negativo, solemos denotar por $\sqrt{k}$ a la solución positiva de dicha ecuación. A dicho número lo llamamos la raíz cuadrada de $k$ y diríamos que la ecuación anterior tiene dos soluciones $\sqrt{k}$ y $-\sqrt{k}$.

Por ello, una forma de resumir la imposibilidad de resolver la ecuación $x^2 + 1 = 0$ en los reales es decir que no existen las raíces cuadradas de números negativos.

Esto no debería de resultar sorprendente, pues no es la primera vez que ocurre algo similar. La ecuación $n + 3 = 2$ donde "$n$", "$3$" y "$2$" representan números naturales tampoco admite ninguna solución. Sería como preguntarse *¿Cuantas manzanas debería tener un árbol, de manera que si le añado $3$ manzanas acabe teniendo $2$ manzanas?* Dicho problema no tiene solución. Un problema diferente sería *¿En qué piso me tengo que encontrar, si tras subir $3$ pisos acabo en el segundo piso?*. La respuesta es que tengo que estar en el sótano, es decir, en el piso $-1$. De ese modo, la ecuación $p+3=2$ donde "$p$", "$3$" y "$2$", representan números enteros, sí que tiene solución. Es decir, el hecho de que una ecuación tenga solución o no va a depender de si los símbolos que aparecen en ella representan números naturales o enteros. 

Del mismo modo, en esta sección vamos a construir *otro* conjunto numérico, al que llamaremos el [cuerpo](#cuerpo) de los números complejos el cual contendrá, entre otras, cantidades que también representarán a los números reales y en el cual sí que existirá la solución a la ecuación $z^2 + 1 = 0$.


### Chapa histórica

Los primeros avances en la definición del cuerpo de los números complejos surgen en intentos de obtener fórmulas generales para resolver ecuaciones cúbicas. Es decir, dada la ecuación $ax^3 + bx^2 + cx^1 + d = 0$ queremos una fórmula:
$$
x = f(a,b,c,d)
$$
que nos devuelva las posibles raíces. 

En el caso de las ecuaciones de segundo grado dicha fórmula era conocida desde hace tiempo. Dada la ecuación:

$$ ax^2 + bx + c = 0$$
sabemos que a lo sumo existen dos valores reales que podrán satisfacer la ecuación y estos vienen dados por las dos fórmulas siguientes: 
$$
x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}
$$

$$
x_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a}
$$

Dependiendo del valor de la cantidad real $b^2 - 4ac$ tendremos dos, una o ninguna solución. Si $b^2 - 4ac$ es un número positivo, ambas fórmulas tienen sentido y aportan soluciones distintas. Si $b^2 = 4ac$ ambas fórmulas nos dan el mismo valor por lo que solo existe una solución distinta y,  finalmente, si $b^2 - 4ac$ es un número negativo, ninguna de las fórmulas tiene sentido, pues no existe la raíz de un número negativo, y la ecuación no tendría soluciones. Ejemplos:

:::{table}
ecuación  | $x_1$ | $x_2$ |
 --- | --- | --- |
$x^2 - 3x + 2=0$ | $2$ | $1$ |
$x^2 - 2x + 1=0$ | $1$ | $1$ |
$x^2 - 1x + 1=0$ | ... | ... |
:::

Sin embargo, como ya dijimos, no existían fórmulas análogas para la ecuación de tercer grado.
:::{attention}
Eso no significa que no se conociesen soluciones a ecuaciones de tercer grado, por ejemplo es fácil verificar que la ecuación (real) $x^3 + 8 = 0$ tiene una única solución, $x=-2$. Por una parte, simplemente operando tenemos que $(-2)^3+8 = -8+8=$, por lo que verificamos que se trata de una solución, y por otra parte, no puede tener más soluciones pues la función $x^3$ es una función estrictamente creciente, por lo tanto, para todo $x< -2$ se tiene que $x^3 < -8$ y para todo $x> -2$ se tiene que $x^3 > - 8$. 

Sin embargo dicha solución no la obtuvimos a partir de una fórmula general, es decir, no conocemos $f$ tal que $-2 = f(1,0,0,8)$.
:::

En un intento de obtener estas fórmulas generales, algunos matemáticos llegaron a métodos que resolvían casos particulares, en los cuales a veces en pasos intermedios aparecían cantidades que no tenían sentido pues involucraban la raíz de un número negativo. Sin embargo si uno seguía operando con dichas cantidades como si funcionasen como números reales, finalmente las raíces negativas se anulaban y el resultado que se obtenía era una solución real de la ecuación cúbica. 

Es importante hacer una aclaración. En ningún momento se trató de buscar soluciones a la ecuación real $x^2 + 1 = 0$. Era un hecho conocido que no existen números reales cuyo cuadrado sea un número negativo y no se disponía de problemas en los que fuese necesario resolver una ecuación similar. En este caso el uso es indirecto, como herramienta que permite calcular soluciones reales de ecuaciones de tercer grado.

Podemos preguntarnos, ¿Que pasaría si existiese un *número*, llamemosle $i$, distinto a cualquier otro número real, y que *cumple* que $i^2 = -1$? Es decir, podemos comprobar como funcionaría la suma y el producto de expresiones de la forma $a+bi$. Es fácil comprobar que si asumimos que la cantidad $i$ satisface las mismas propiedades que los reales para la suma y el producto, es decir, asociatividad, conmutatividad, etc, se tiene para la suma:

$$
\begin{align*}
(a_1 + b_1 i)+(a_2 + b_2i)=&a_1 + b_1 i + a_2 + b_2 i \\
                          =&a_1 + a_2 + (b_1 + b_2)i
\end{align*}
$$


y para el producto:

$$
\begin{align*}
(a_1 + b_1 i)(a_2 + b_2i)=& a_1a_2 + a_1b_2i + b_1ia_2 + b_1ib_2i \\
                         =& a_1a_2 + b_1b_2i^2 +  \left(a_1b_2 + b_1a_2\right)\\
                         =& a_1a_2 - b_1b_2 +  \left(a_1b_2 + b_1a_2\right)i
\end{align*}
$$
donde se hizo uso de la suposición de que la cantidad $i$ cumple $i^2 = -1$. 

:::{prf:definition} El cuerpo de los números complejos.
:label: complejos
:nonumber:

Llamamos cuerpo de los números complejos, y lo denotamos por $\mathbb{C}$ a una estructura algebraica formada por el conjunto $\mathbb{R}^2$ y dos operaciones, una de suma y otra de producto: 
- **suma**: Dados $z_1 = (u_1, v_1)\in \mathbb{R}^2$ y $z_2 = (u_2, v_2)\in\mathbb{R}^2$, entonces 
$$
z_1 + z_2 := (u_1 + u_2, v_1 + v_2)
$$ 

- **producto**: Dados $z_1 = (u_1, v_1)\in \mathbb{R}^2$ y $z_2 = (u_2, v_2)\in\mathbb{R}^2$, entonces 
$$
z_1 z_2 := (u_1v_1 - u_2v_2, u_1v_2 + u_2v_1)
$$
:::


Es sencillo comprobar que la estructura algebraica asi definida cumple las propiedades de un [cuerpo](#cuerpo). La suma es conmutativa

:::{prf:proof}
:class: dropdown
Sean $z_1=(a_1,b_1)$ y $z_2=(a_2,b_2)$ se tiene que:
$$
z_1 + z_2 = (a_1+a_2, b_1+b_2) = (a_2+a_1,b_2+b_1) = z_2 + z_1
$$
y asociativa:
:::{prf:proof}
:::

existe un elemento, el $(0,0)$ que es el elemento neutro de la suma:

:::{prf:proof}
Para todo $z=(a,b)$ se tiene que $(0,0)+(a,b)=(a+0,b+0)=(a,b)$.
:::

y para todo complejo $z=(a,b)$, existe el número complejo $(-a,-b)$, [opuesto](#opuesto), que denotaremos como $-z$.

:::{prf:proof}
Para todo $(a,b)$ se tiene que 
$$
(a,b)+(-a,-b)=(a-a,b-b)=(0,0)
$$
:::

Por otra parte, el producto también es conmutativo y asociativo

:::{prf:proof}
:::
y existe un elemento, el $(1,0)$ que es el elemento neutro del producto

:::{prf:proof}
:::

$$
ez = (1,0)(u,v) = (1u - 0v, 1v + 0u) = (u,v)=z
$$


:::{warning}
:class: dropdown
Por comodidad se suele denotar por $1$ al elemento neutro $e$, de manera que uno puede decir que, en números complejos, se cumple que $1z=z$. Sin embargo si denotamos por $1$ al elemento neutro, entonces tenemos que:
$$
1 = (1,0)
$$
Lo cual no tiene sentido, pues $1$ estaría denotando a conceptos diferentes en la misma ecuación.

Lo correcto sería escribir, por ejemplo:

$$
1_\mathbb{C} = (1_\mathbb{R}, 0_\mathbb{R})
$$

de manera que estamos expresando que son conceptos diferentes. Sin embargo, cuando no exista riesgo de confusión, se denotará por $1$ y $0$ a los elementos neutros del producto y de la suma, indistintamente de si se trata del cuerpo de los complejos o el de los reales.
::: 


Del mismo modo que el elemento $(1,0)$ es el elemento neutro, el elemento $(0,1)$ también tiene un tratamiento especial. Se le conoce como unidad imaginaria, lo denotamos por $i$ y cumple que $i^2=-1$, pues:


$$
i^2 = (0,1)(0,1)=(0 - 1, 0 ) = -(1,0) = -e
$$

:::{attention}
:class: dropdown
Esto no significa que hayamos encontrado un número que elevado al cuadrado nos devuelva el número real negativo $-1$. Esto únicamente significa que acabmos de describir una estructura algebraica en $\mathbb{R}^2$ en la cual la multiplicación que definimos nos permite encontrar un elemento que multiplicado por si mismo nos devuelve el elemento neutro de dicha multiplicación cambiado de signo: 

$$
(0,1)(0,1) = -(1,0)
$$

Podemos dormir tranquilos, la raiz cuadrada sigue sin estar definida en números reales negativos.
:::


## Inverso de un número complejo
Al igual que en el caso de los números reales, todo número complejo distinto del $0$ posee un [inverso multiplicativo](#inverso).

Dado un número complejo $z=a+bi\neq 0$ buscamos un complejo $z^{-1}=u+vi$ tal que 
$$
z^{-1}z = 1
$$

Realizando la operación se tiene:

$$
(au - bv) + i(av+bu) = 1 + 0i
$$
de donde se obtiene el sistema:

$$
\begin{array}{c}
au - bv = 1\\
bu + av = 0
\end{array}
$$
cuyas incógnitas son $u$ y $v$. Resolviendo se obtiene:
$$
u = \frac{a}{a^2 + b^2},\quad v = \frac{-b}{a^2 + b^2} 
$$
con lo que el inverso del número $z=a+bi$ será el número:
$$
z^{-1} = \frac{a - bi}{a^2 + b^2}
$$

En la 

:::{prf:definition}{Conjugado de un número complejo}
Dado el número complejo $z = a + bi$ llamamos conjugado y lo denotampor por $\bar{z}$ al número $\bar{z}=a-bi$.
:::

haciendo uso del conjugado podemos reescribir el inverso de un número complejo como 

$$
z^{-1} = \frac{\bar{z}}{|z|^2}
$$

de donde también observamos que $z\bar{z}=|z|^2$.


## Forma binómica de un número complejo

Por definición de la suma de números complejos se tiene que, para todo $z\in\mathbb{C}$:

$$
z=(u,v)=(u,0) + (0,v) = u(1,0) + v(0,1) = u + vi
$$ 



:::{prf:definition} Módulo de un número complejo
Llamamos módulo de un número complejo $z=a+bi$ a la cantidad real $|z|:=\sqrt{a^2 + b^2}$.
:::

::::{prf:property} Desigualdad triangular
$$
|z_1+z_2|\le|z_1| + |z_2|
$$
:::{prf:proof}
:class: dropdown

El módulo es una cantidad real no negativa por lo que probar:

$$
|z_1+z_2|\le|z_1| + |z_2|
$$

es completamente quivalente a probar

$$
|z_1+z_2|^2\le\left(|z_1| + |z_2|\right)^2
$$

Sin embargo lo segundo es más fácil, pues involucra manipular menos raíces. 
$$
|z_1+z_2|^2 = |(a_1+a_2) + i(b_1+b_2)|^2 = (a_1+a_2)^2 + (b_1 +b_2)
$$

$$
= a_1^2 + 2a_1 a_2 + a_2^2 + b_1^2 + 2b_1 b_2 + b_2^2 = 
$$

$$
= (a_1^2 + b_1^2) + (a_2^2 + b_2^2) + 2(a_1 a_2 + b_1 + b_2) =
$$

$$
|z_1|^2 + |z_2|^2 + 2(a_1 a_2 + b_1 + b_2)
$$

Por otra parte

$$
\left(|z_1| + |z_2|\right)^2 = |z_1|^2 + 2|z_1||z_2| + |z_2|^2 = 
$$

:::
::::


::::{prf:property} Módulo del producto
:label: prod_modulo

Dados dos números complejos $z_1$ y $z_2$, se tiene que $|z_1 z_2|=|z_1||z_2|$.

:::{prf:proof}
:class: dropdown

Si $z_1 = a_1 + b_1 i$ y $z_2 = a_2 + b_2 i$, entonces

$$
z_1 z_2 = ( a_1 a_2 - b_1 b_2) + (a_1 b_2 + a_2 b_1 ) i
$$

Por lo que el módulo del producto es:

$$
| z_1 z_2 | = \sqrt{ (a_1 a_2 - b_1b_2)^2 + (a_1 b_2 + a_2 b_1)^2 }
$$

Operando tenemos por un lado que:

$$
(a_1a_2 -b_1b_2)^2 = a_1^2a_2^2 - 2a_1a_2b_1b_2 + b_1^2 b_2^2
$$
y
$$
(a_1b_2 + a_2b_1)^2 = a_1^2b_2^2 + 2a_1a_2b_1b_2 + a_2^2b_1^2
$$

con lo que
$$
(a_1a_2 - b_1b_2)^2 + (a_1b_2 + a_2b_1)^2 = a_1^2a_2^2 + a_1^2b_2^2 + a_2^2b_1^2 + b_1^2b_2^2
$$
o lo que es lo mismo

$$
(a_1a_2 - b_1b_2)^2 + (a_1b_2 + a_2b_1)^2 = (a_1^2 + b_1^2)(a_2^2 + b_2^2)
$$

Por lo que finalmente:

$$
|z_1 z_2 | = \sqrt{a_1^2 + b_1^2}\sqrt{a_2^2 + b_2^2} = |z_1| |z_2|
$$
:::

::::


### Argumento de un número complejo

:::{prf:definition} Argumento
Llamamos argumento de un número complejo $z=a+bi$ a la cantidad real $\arg(z):=\arctan\left(\frac{b}{a}\right)$
:::

DIBUJO (MOTIVAR SU DEFINICIÓN)


Conocido el módulo $\rho$ y el argumento $\theta$ de un número complejo $z$ se pueden conocer sus partes real e imaginaria, pues:

$$
\mathfrak{Re}(z) = \rho\cos\theta,\quad\mathfrak{Im}(z)=\rho\sin\theta.
$$


::::{prf:property} Argumento del producto
:label: prod_argumento
Dados dos números complejos $z_1$ y $z_2$, se tiene que $\arg(z_1z_2)=\arg(z_1)+\arg(z_2)$.

:::{prf:proof}
:class: dropdown

En primer lugar recordamos las expresiones para el coseno y el seno del ángulo suma: 

$$
\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta
$$

$$
\cos(\alpha + \beta) = \cos\alpha \cos\beta - \sin\alpha\sin\beta
$$

Ahora, si escribimos

$$
z_1 = |z_1|\left(\cos\theta_1 + i\sin\theta_1\right)
$$

$$
z_2 = |z_2|\left(\cos\theta_2 + i\sin\theta_2\right)
$$

y los multiplicamos utilizando la definición de producto de dos números complejos tenemos que:

$$
z_1 z_2 = |z_1||z_2|\left(\left(\cos\theta_1\cos\theta_2 - \sin\theta_1 \sin \theta_2\right) + i\left(\cos\theta_1\sin\theta_2 + \cos\theta_2\sin\theta_1\right)\right)
$$

o lo que es lo mismo:

$$
z_1 z_2 = |z_1||z_2|\left(\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)\right)
$$

Finalmente calculando el argumento de $z_1 z_2$ obtemos:

$$
\arg(z_1 z_2 ) = \mathrm{arctan}(\frac{\sin(\theta_1 + \theta_2)}{\cos(\theta_1 + \theta_2)}) = \mathrm{arctan}(\tan(\theta_1 + \theta_2)) = \theta_1 + \theta_2
$$
:::

::::


### Intepretación geométrica de la suma y del producto




## Forma módulo-argumento


Una forma de denotar entonces al número complejo $z$ es como $\rho_\theta$. Esta forma se conoce como módulo-argumento y contiene la misma información que la forma binómica o la cartesiana.

:::{prf:example}
Si $z=1+i$ entonces $z=\sqrt{2}_{\frac{\pi}{2}}$
:::

Las propiedades [{number}](#prod_modulo) y [{number}](#prod_argumento) hacen que sea muy sencillo realizar multiplicaciones de números complejos expresadas en forma módulo-argumento, pues:

$$
\rho_\alpha r_\beta = (\rho r )_{\alpha + \beta}
$$

## Potencia de un número complejo. 
La potencia de un número complejo a un número natural se define de manera análoga a como se hace en números reales: 

$$
z^1 = z
$$

$$
z^n = zz^{n-1},\quad\text{para }n>1
$$

Al igual que en el caso de la multiplicación, la potencia tiene una expresión mucho mas simple en forma módulo-argumento o trigonométrica:

$$
z^n = |z|^n \left(\cos(n\arg z)+i\sin(n \arg z)\right)
$$




## Raíz de un número complejo
En los números reales definimos la raíz cuadrada de un número $x$ como aquel número $y$ que cumple que $y^2=x$. De manera análoga definimos la raiz enésima. 

Por ejemplo, en los reales, la raíz cúbica de $8$ es únicamente $2$ pues $2^3=8$ y la raíz cúbica de $-8$ es únicamente $-2$. 

:::{prf:remark}
En general, si $x$ es un número real podemos afimar que: 
- Si $n$ es par, $\sqrt[n]{x}$ sólo existe para $x>=0$. En ese caso, tanto $y=\sqrt[n]{x}$ como $y=-\sqrt[n]{x}$ cumplen que $y^n = x$.
- Si $n$ es impar, $\sqrt[n]{x}$ existe para cualquier $x$ y es única, siendo un número positivo para $x>0$ y negativo para $x<0$.
:::

En números complejos podemos definir la raíz de la misma manera.  El número complejo $w=\sqrt[n]{z}$ será aquel que cumpla que $w^n=z$, por lo que simplemente tenemos que igualar: 

$$
|z| = |w|^n 
$$

$$
\arg z = n\arg w
$$

o lo que es lo mismo $|w| = |z|^{\frac{1}{n}}=\sqrt[n]{|z|}$ y $\arg w=\frac{\arg z}{n}$.


### Intepretación geométrica
Empezemos primero con las raíces enésimas del número complejo $1$. Como ya sabemos, si $w=\sqrt[n]{1}$ entonces: 

$$|w|=\sqrt[n]{1}=1$$

y tenemos $n$ valores diferentes para el argumento de $w$, estos son:

$$
\left\{0,\frac{1}{n}2\pi,\frac{2}{n}2\pi,\dots,\frac{n-1}{n}2\pi\right\}
$$


## Teorema fundamental del álgebra

:::{prf:definition} Raíz de un polinomio
Dado un polinomio $p(x)$ llamamos _raiz del polinomio_ a un valor $x$ en el cual el polinomio se anula, $p(x)=0$.
:::

:::{prf:definition} Factorización de un polinomio: 
Dado
:::


:::{prf:definition} Multiplicidad de una raiz
Llamamos multiplicidad de una raiz de un polinoimo al número de veces que una raíz anula a un polinomio. Es decir, si $\alpha$ es una raiz de $p$ con multiplicidad $n$, entonces existe un polinomio $q$ tal que
$$
p(z) = q(z)(z-\alpha)^n
$$
y $q(\alpha)\neq 0$.
:::

Por ejemplo decimos que $x=2$ es una raiz doble del polinomio $x^2-4x+4$ mientras que es una raiz simple del polinomio $x^2 -3x + 2$, pues tenemos que 

$$
x^2 -4x + 4 = (x-2)(x-2)
$$
mientras que 
$$
x^2 -3x + 2 = (x-2)(x-1)
$$

:::{note}
La gráfica de un polinomio en un entorno de una raíz simple consiste en una curva que corta el eje de las $x$, mientras que la gráfica entorno a una raíz doble consiste en un punto de tangencia con el eje de las $x$. Ambos son puntos en los que el polinomio vale $0$, pero en la raiz doble la pendiente es también nula.

DIBUJO 

:::


:::{prf:theorem} Teorema fundamental del álgebra
Dado un polinomio $p$ de grado $n$ en variable compleja: 

$$
p(z) :=  a_0 + a_1 z + a_2 z^2 + \dots + a_n z^n,\quad \text{con }a_n\neq 0
$$
Entonces existen exactamente $n$ raices del polinomio, contando multiplicidades. 
:::