import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

titulo = "Scatterplot: Gráfico de Dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.scatter(x, y, label = "Pontos", color = "r", marker="h", s=100) # plota os pontos da dispersão
plt.plot(x, y) # plota as linhas, unindo os pontos
plt.legend()
plt.show()

''' 
Documentação Oficial do Matplotlib
Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

A seguir, alguns exemplos de argumentos que podem ser aplicados ao método plot( ).

color:	cor (ver exemplos abaixo)

label:	rótulo

linestyle:	estilo de linha (ver exemplos abaixo)

linewidth: largura da linha

marker:	marcador (ver exemplos abaixo)

#### CORES (color)
'b'	blue

'g'	green

'r'	red

'c'	cyan

'm'	magenta

'y'	yellow

'k'	black

'w'	white

#### Marcadores (marker)
'.'	point marker

','	pixel marker

'o'	circle marker

'v'	triangle_down marker

'^'	triangle_up marker

'<'	triangle_left marker

'>'	triangle_right marker

'1'	tri_down marker

'2'	tri_up marker

'3'	tri_left marker

'4'	tri_right marker

's'	square marker

'p'	pentagon marker

'*'	star marker

'h'	hexagon1 marker

'H'	hexagon2 marker

'+'	plus marker

'x'	x marker

'D'	diamond marker

'd'	thin_diamond marker

'|'	vline marker

'_'	hline marker

##### Tipos de linha (linestyle)
'-'	solid line style

'--'	dashed line style

'-.'	dash-dot line style

':'	dotted line style

Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
'''