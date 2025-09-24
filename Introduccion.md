# Apuntes de álgebra lineal

Éstos son unos apuntes de álgebra lineal para ingenieros o estudiantes de ciencias. 

Un proceso, fenomeno físico, etc... será lineal si cumple dos propiedades: 

- Las consecuencias son proporcionales a las causas 

- El efecto combinado de dos causas es igual a la suma de los efectos por separado (el todo es igual a la suma de las partes):


En el mundo real es fácil encontrar ejemplos de procesos que son lineales y procesos que no. Por ejemplo, nos puede resultar muy rico tanto el chocolate, como el tomate frito, por separado, y sin embargo una combinación de chocolate y tomate frito *probablemente* no nos lo resulte. En este caso estaríamos fallando a la segunda propiedad. Del mismo modo, puede que echándole una pizca de sal a un arroz nos resulte más sabroso y sin embargo echándole veinte veces más no nos resulte veinte veces más sabroso. 

Otro ejemplo de cantidades con una relación no lineal entre ellas es la de la velocidad que lleva un coche y la distancia que requiere para frenar hasta quedarse parado. Asumiendo que un coche lleva una velocidad $v$, y tiene una masa $m$, su energía cinética es entonces:

:::{math}
:enumerated: false
E_k = \frac{1}{2}mv^2
:::

Si asumimos también que los frenos pueden ejercer una fuerza de frenada máxima $F_\mathrm{max}$, entonces el trabajo máximo que pueden realizar frenando a lo largo de una distancia $h$ es $W=F_\mathrm{max}h$.  Igualándolo a la energía cinética que tenemos que disipar obtenemos:

:::{math}
:enumerated: false
F_\mathrm{max}h = \frac{1}{2}mv^2 \Rightarrow h = \frac{m}{2F_\mathrm{max}}v^2
:::

Podemos comprobar que si para decelerar desde una velocidad $v_1$ requerimos una distancia:

:::{math}
:enumerated: false
h_1 = \frac{m}{2F_\mathrm{max}}v_1^2
:::

entonces para decelerar desde una velocidad $v_2=2v_1$ requerimos: 

:::{math}
:enumerated: false
h_2 = \frac{m}{2F_\mathrm{max}}(2v_1)^2=4\frac{m}{2F_\mathrm{max}}v_1^2 = 4h_1 \neq 2v_1
:::

Por lo tanto la distancia requerida no es proporcional a la velocidad inicial, es una relación no lineal.



