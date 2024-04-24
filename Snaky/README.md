<img src="https://iqdotnet.net/iqcode/iqcode.png" style="zoom: 25%;" />

# Snaky Game <img src="https://iqdotnet.net/iqcode/1.png" style="zoom:12%;" />

<img src="https://iqdotnet.net/iqcode/portada_snaky.png" style="zoom:30%;" />

## Español

### Descripción
Este código es una implementación del juego Snake en Python utilizando la biblioteca Pygame. El juego consiste en controlar una serpiente que se mueve por la pantalla, recolectando manzanas para aumentar su longitud y puntaje, evitando chocar con los bordes de la pantalla o consigo misma.

### Técnicas Utilizadas
- Programación orientada a objetos (POO): El juego está estructurado en una clase principal `SnakeGame` y una clase de configuración `Config`, utilizando objetos y métodos para organizar y gestionar el comportamiento del juego.
- Manipulación de eventos: Se utilizan los eventos de Pygame para detectar las acciones del usuario, como presionar teclas o cerrar la ventana del juego.
- Detección de colisiones: Se implementa un método para verificar si la cabeza de la serpiente colisiona con los bordes de la pantalla o con su propio cuerpo.
- Generación aleatoria de elementos: Las manzanas y la posición inicial de la serpiente se generan aleatoriamente dentro de la pantalla.
- Control de tiempo y velocidad: Se utiliza un bucle principal para controlar la velocidad del juego mediante el reloj de Pygame.

### Funcionalidad Principal
1. **Inicialización del juego:** Se configuran los parámetros iniciales del juego, como el tamaño de la ventana, la velocidad de fotogramas por segundo (FPS) y los colores.
2. **Bucle principal del juego:** El juego se ejecuta en un bucle principal que maneja la lógica del juego y la actualización de la pantalla.
3. **Control de la serpiente:** El jugador puede controlar la dirección de la serpiente utilizando las teclas de flecha o las teclas 'W', 'A', 'S' y 'D'.
4. **Detección de colisiones:** Se verifica si la serpiente colisiona con los bordes de la pantalla o consigo misma.
5. **Generación de manzanas:** Se generan nuevas manzanas de forma aleatoria en la pantalla.
6. **Puntuación:** Se lleva un registro de la puntuación del jugador, que aumenta cada vez que la serpiente consume una manzana.
7. **Pantallas de inicio y fin:** Se muestran pantallas de inicio y fin de juego, con mensajes para indicar al jugador cómo comenzar o reiniciar el juego.

## English

### Description
This code is an implementation of the Snake game in Python using the Pygame library. The game involves controlling a snake that moves around the screen, collecting apples to increase its length and score, while avoiding collisions with the screen edges or itself.

### Techniques Used
- Object-oriented programming (OOP): The game is structured around a main class `SnakeGame` and a configuration class `Config`, using objects and methods to organize and manage the game's behavior.
- Event handling: Pygame events are used to detect user actions, such as pressing keys or closing the game window.
- Collision detection: A method is implemented to check if the snake's head collides with the screen edges or its own body.
- Random element generation: Apples and the snake's initial position are randomly generated within the screen.
- Time and speed control: A main loop controls the game speed using Pygame's clock.

### Main Functionality
1. **Game initialization:** Initial parameters such as window size, frames per second (FPS) and colors are configured.
2. **Main game loop:** The game runs in a main loop that handles the game logic and screen updates.
3. **Snake control:** The player can control the snake's direction using arrow keys or 'W', 'A', 'S', and 'D' keys.
4. **Collision detection:** Checks if the snake collides with the screen edges or itself.
5. **Apple generation:** New apples are randomly generated on the screen.
6. **Scoring:** The player's score is kept track of, increasing each time the snake consumes an apple.
7. **Start and game over screens:** Screens are displayed to indicate how to start or restart the game.

------

> [IQDOTNET CODE](https://www.facebook.com/IQDotNetCode) - by NelsoN
