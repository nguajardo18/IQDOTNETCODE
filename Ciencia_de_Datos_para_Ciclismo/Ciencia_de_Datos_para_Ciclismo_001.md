<img src="https://iqdotnet.net/iqcode/iqcode.png" style="zoom: 25%;" />



# Ciencia de Datos para Ciclismo - Cómo Leer Rutas GPX de Strava con Python

<img src="https://iqdotnet.net/iqcode/portada.jpg" style="zoom:50%;" />

## Introducción a GPX, exploración y visualización de una ruta de Strava

------

Disfruto mucho del ciclismo y me divierto utilizando Strava para  realizar un seguimiento de mis paseos por la montaña. Sin embargo, como  entusiasta de los datos, me siento un poco decepcionado con el análisis  proporcionado. Aunque Strava ofrece información sobre velocidad,  potencia, cadencia, ritmo cardíaco y más, lo que realmente me gustaría  ver es un análisis más profundo del gradiente. Creo que comprender cómo  varía el terreno durante mis rutas sería invaluable para mejorar mi  rendimiento y estrategia tanto en mis salidas habituales como en eventos competitivos en los que me inscriba.

Ahora bien, cuando hablamos de gradiente en el contexto de la ciencia de datos y el ciclismo, no necesariamente nos referimos a lo mismo. E<u>n el  ciclismo, el gradiente es básicamente la inclinación de la superficie  por la que estás montando</u>. Siendo un ciclista de estatura media y algo  pesado, encuentro los cerros especialmente desafiantes, por lo que  considero que un análisis más detallado del gradiente sería muy útil.  Por ejemplo, me gustaría poder ver cuánta distancia he recorrido en  tramos con un gradiente del 3 al 5 por ciento, cuánto en pendientes  superiores al 10 por ciento, y todas las variaciones intermedias.  ¿Captas la idea?

Al analizar el gradiente de las rutas de mountain bike, los ciclistas  pueden entender mejor la dificultad y el desafío de cada sección del  recorrido. Esto les permite adaptar su ritmo, técnica y elección de  equipo de acuerdo con las características del terreno, optimizando así  su rendimiento y disfrute en el camino.

Strava no ofrece esa funcionalidad, así que decidí hacer los cálculos desde cero utilizando mis habilidades en Python.  `Acompáñame en una mini-serie de 5 artículos que comenzará con un curso intensivo sobre el formato de archivo GPX y terminará en un panel de control que muestra tus datos de entrenamiento con más profundidad que Strava.`

## Curso Intensivo de GPX para Ciencia de Datos

------

Strava permite exportar tus entrenamientos y rutas en formato de archivo GPX. En términos simples, GPX significa Formato de Intercambio GPS, y no es más que un archivo de texto con información geográfica, como latitud, longitud, elevaciones, rastros, puntos de interés, y demás.

Un archivo GPX de una ruta exportada de Strava tiene muchos puntos tomados en diferentes momentos, cada uno conteniendo latitud, longitud y elevación. En términos simples, sabes exactamente dónde estabas y cuál era tu altitud. Esto es esencial para calcular gradientes y rangos de gradientes, lo cual haremos en un par de artículos.

Si estás siguiendo el proceso, dirígete a Strava y descarga cualquiera de tus rutas guardadas (botón Exportar GPX): 

botón Exportar GPX

![GPXStrava](https://iqdotnet.net/iqcode/GPXStrava.png)

######                                                                                                                                              Imagen1

Crear rutas requiere una suscripción de pago en Strava, así que por razones de seguridad no compartiré mis archivos GPX contigo. Usa cualquier archivo GPX de tus rutas o del registro de entrenamiento. Si no estás usando Strava, simplemente encuentra un archivo GPX de muestra en línea, debería funcionar igualmente.

¿Tienes el archivo GPX listo? Genial — veamos cómo leerlo con Python a continuación.

## Cómo Leer Archivos GPX con Python

------

Necesitarás el paquete dedicado `gpxpy` para leer GPX con Python. Instálalo con Pip: 

```python
pip install gpxpy
```

Ahora puedes lanzar Jupyter o cualquier otro editor de código para comenzar. Primero lo primero, vamos a ocuparnos de las importaciones de las bibliotecas:

![image-20240427183813409](https://iqdotnet.net/iqcode/image-20240427183813409.png)

Utiliza la sintaxis del gestor de contexto de Python para leer y analizar un archivo GPX:

![image-20240427183900483](https://iqdotnet.net/iqcode/image-20240427183900483.png)

Ten en cuenta que tendrás que cambiar la ruta para que coincida con tu sistema y el nombre del archivo GPX. Si todo salió bien, ahora deberías tener el archivo disponible en Python.

Pero, ¿qué hay dentro? Vamos a ver:

![image-20240427183949492](https://iqdotnet.net/iqcode/image-20240427183949492.png)

Es un objeto GPX específico con el nombre del recorrido y segmento, donde cada segmento contiene puntos de datos (latitud, longitud y elevación). Profundizaremos en estos en la siguiente sección, pero primero, exploremos un par de funciones útiles.

Por ejemplo, puedes extraer el número total de puntos de datos en un archivo GPX:

![image-20240427184059900](https://iqdotnet.net/iqcode/image-20240427184059900.png)

Hay un total de 6842 puntos, cada uno conteniendo datos de latitud, longitud y elevación. Esto será útil más adelante.

También puedes obtener el rango de altitud:

![image-20240427184141310](https://iqdotnet.net/iqcode/image-20240427184141310.png)

En términos simples, esto significa que el punto más bajo del recorrido está a 1843.4 metros sobre el nivel del mar, mientras que el más alto está a 1995.0 metros.

También puedes extraer los metros totales de elevación ganados y perdidos:

![image-20240427184246086](https://iqdotnet.net/iqcode/image-20240427184246086.png)

Mi ruta representa un recorrido de ida y vuelta, por lo que se espera ver valores idénticos o casi idénticos. Por último, puedes mostrar el contenido de tu archivo GPX en formato XML:

![image-20240427184338306](https://iqdotnet.net/iqcode/image-20240427184338306.png)

Y eso es todo para lo básico. A continuación, verás cómo extraer puntos de datos individuales y convertirlos en un formato más legible: DataFrame de Pandas. Cómo Analizar Archivos GPX con Python

Puedes verificar cuántos recorridos tiene tu archivo GPX ejecutando len(gpx.tracks). El mío tiene solo uno, y puedo acceder a él con la notación de indexación de listas de Python:

![image-20240427184433030](https://iqdotnet.net/iqcode/image-20240427184433030.png)

No nos importa el nombre del recorrido, ya que es arbitrario en este caso. Lo que sí nos importa son los segmentos. Al igual que con los recorridos, mi archivo GPX tiene solo un segmento en este recorrido. Así es como puedes acceder a él:

![image-20240427184458007](https://iqdotnet.net/iqcode/image-20240427184458007.png)

Y ahora puedes acceder a los puntos de datos individuales accediendo al array de puntos. Aquí están los primeros diez para mi ruta:

![image-20240427184526090](https://iqdotnet.net/iqcode/image-20240427184526090.png)

Eso es todo lo que necesitamos para divertirnos un poco. Ahora verás cómo extraer puntos de datos individuales del archivo GPX:

![image-20240427184558179](https://iqdotnet.net/iqcode/image-20240427184558179.png)

No es el código más bonito que hayas visto, pero hace el trabajo. Imprimamos las primeras tres entradas para verificar que hicimos todo correctamente:

![image-20240427184622225](https://iqdotnet.net/iqcode/image-20240427184622225.png)

¿Sabes qué es aún más práctico acerca de una lista de diccionarios? Puedes convertirla en un DataFrame de Pandas en un instante.

![image-20240427184650963](https://iqdotnet.net/iqcode/image-20240427184650963.png)

Tienes que admitirlo, ¡fue bastante fácil! Necesitaremos este conjunto de datos en los siguientes artículos, así que vamos a guardarlo en un archivo CSV.

![image-20240427184718283](https://iqdotnet.net/iqcode/image-20240427184718283.png)

Eso es todo por el análisis básico y el preprocesamiento que haremos hoy. También te mostraré cómo visualizar este conjunto de datos con Matplotlib, solo para ver si vamos por el camino correcto. 

# Cómo Visualizar Archivos GPX con Python y Matplotlib

Trabajaremos en la visualización de rutas con Python y Folium en el siguiente artículo, pero hoy quiero mostrarte cómo hacer una visualización básica con Matplotlib. No verás el mapa, claro está, pero los puntos de ubicación deberían parecerse a la ruta de la Imagen 1.

Pista: no hagas la figura demasiado ancha, ya que haría que el mapa se vea extraño.

El siguiente código para visualizar la ruta:

![image-20240427184913423](https://iqdotnet.net/iqcode/image-20240427184913423.png)

![image-20240427184925760](https://iqdotnet.net/iqcode/image-20240427184925760.png)

Y quién lo diría, es idéntico a lo que teníamos en la Imagen 1, sin tener en cuenta lo obvio. Aprenderás todo sobre la visualización de mapas y rutas en el siguiente artículo.

# Conclusiones

Y ahí lo tienes: has exportado exitosamente un archivo GPX de ruta/entrenamiento desde Strava, lo has analizado con Python y has extraído características clave como latitud, longitud y elevación. Esto es solo la punta del iceberg, y puedes esperar aprender más aplicaciones de programación y ciencia de datos en ciclismo en los próximos artículos.

¡Gracias por leer y mantente atento para más!

------

**by Nelson Guajardo**