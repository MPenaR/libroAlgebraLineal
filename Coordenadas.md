# Coordenadas y cambios de coordenadas. 

Sea un espacio vectorial $V$ de dimension $n$. 

:::{prf:definition} Coordenadas de un vector. 
Llamaremos coordenadas de un vector $\mathbf{v}\in V$ en una base $\mathcal{B}=\{\mathbf{e}_1,\mathbf{e}_2,\dots\mathbf{e}_n\}$ de $V$ a los $n$ escalares $x_1,x_2,\dots,x_n$ que cumplen:
$$
\mathbf{v} = x_1\mathbf{e}_1 + x_2\mathbf{e}_2 +\dots + x_n\mathbf{e}_n
$$

Como ya demostramos, dichos escalares son únicos para cada vector $\mathbf{v}$ y base $\mathbf{B}$.
:::

Así, dado un vector $\mathbf{v}$, sus coordenadas serán el elemento de $\mathbb{R}^n$ $(x_1,x_2,\dots,x_n)$.  Por comodidad denotaremos por  $(x_1,x_2,\dots,x_n)_\mathcal{B}$ a la suma:
$$
(x_1,x_2,\dots,x_n)_\mathcal{B} = x_1\mathbf{e}_1+ x_2\mathbf{e}_2 \dots x_n \mathbf{e}_n
$$
de modo que, si $(x_1,x_2,\dots,x_n)$ son las coordenadas del vector $\mathbf{v}$ en la base $\mathcal{B}$, entonces $\mathbf{v}=(x_1,x_2,\dots,x_n)_\mathcal{B}$.

:::{prf:example} Polinomios en la base usual
Sea $\mathcal{B}=\{1,t,t^2\}$ la base usual del espacio vectorial $V=\mathbb{R}_2[t]$. Queremos calcular las coordenadas en dicha base de los polinomios $p_1(t)=1 - t^2$, $p_2(t)=t^2 - t$ y $p_3(t) = t^2 + t$.

Puesto que 
$$
p_1(t) = 1 + 0t + (-1)t^2
$$
entonces $p_1(t) = (1,0,-1)_\mathcal{B}$ y las coordenadas de $p_1$ en $\mathcal{B}$ serían la terna $(1,0,-1)$. Del mismo modo tenemos que 
$$
p_2(t) = (0,-1,1)_\mathcal{B},\quad p_3(t)=(0,1,1)_\mathcal{B}
$$
:::

