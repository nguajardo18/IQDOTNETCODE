<img src="https://iqdotnet.net/iqcode/iqcode.png" style="zoom: 25%;" />

# QuickLink: Advanced URL Shortener <img src="https://iqdotnet.net/iqcode/1.png" style="zoom:15%;" />

## English Documentation

# QuickLink: Advanced URL Shortener

This program allows you to shorten URLs using different services like TinyURL, Bitly, and IS.gd.

## Class `URLShortener`

The `URLShortener` class encapsulates the functionality of shortening URLs and supports multiple services.

### Method `__init__`

Initializes the class with a shortener object and a service mapping.

- `shortener`: Shortener object created using the `pyshorteners` library.
- `service_mapping`: Dictionary mapping service names to shortening functions.

### Method `shorten_url`

Shortens a URL using the specified shortening service.

- `url`: The URL to be shortened.
- `service`: The shortening service to use (default is TinyURL).

Returns the shortened URL.

### Method `check_internet_connection`

Checks if there is an Internet connection by making a request to a website.

Returns `True` if there is an Internet connection, otherwise returns `False`.

## Function `main`

The main function runs the program in a loop until the user decides to exit.

1. Initializes the `URLShortener` class.
2. Prompts the user to enter a URL and the shortening service.
3. Shortens the URL and displays the shortened URL.
4. Copies the shortened URL to the clipboard.
5. Handles errors such as invalid URLs or lack of Internet connection.
6. Handles program interruption (e.g., by pressing Ctrl+C).

## Program Execution

The program runs in a loop until the user decides to exit by entering "exit". During each iteration of the loop, the user can input a URL and select a shortening service. The program will display the shortened URL and copy it to the clipboard. The program handles errors and user interruption appropriately.

## Documentación en Español

# QuickLink: Advanced URL Shortener

Este programa permite acortar URLs utilizando diferentes servicios como TinyURL, Bitly e IS.gd.

## Clase `URLShortener`

La clase `URLShortener` encapsula la funcionalidad de acortar URLs y admite múltiples servicios.

### Método `__init__`

Inicializa la clase con un objeto de acortador y un mapeo de servicios.

- `shortener`: Objeto de acortador creado utilizando la biblioteca `pyshorteners`.
- `service_mapping`: Diccionario que mapea nombres de servicios a funciones de acortamiento.

### Método `shorten_url`

Acorta una URL utilizando el servicio especificado.

- `url`: La URL que se va a acortar.
- `service`: El servicio de acortamiento a utilizar (por defecto es TinyURL).

Devuelve la URL acortada.

### Método `check_internet_connection`

Verifica si hay conexión a Internet haciendo una solicitud a un sitio web.

Devuelve `True` si hay conexión a Internet, de lo contrario, devuelve `False`.

## Función `main`

La función principal ejecuta el programa en un bucle hasta que el usuario decide salir.

1. Inicializa la clase `URLShortener`.
2. Solicita al usuario que ingrese una URL y el servicio de acortamiento.
3. Acorta la URL y muestra la URL acortada.
4. Copia la URL acortada al portapapeles.
5. Controla errores como URLs inválidas o falta de conexión a Internet.
6. Maneja la interrupción del programa (por ejemplo, al presionar Ctrl+C).

## Ejecución del Programa

El programa se ejecuta en un bucle hasta que el usuario decide salir ingresando "exit". Durante cada iteración del bucle, el usuario puede ingresar una URL y seleccionar un servicio de acortamiento. El programa mostrará la URL acortada y la copiará al portapapeles. El programa controla errores y maneja la interrupción del usuario de manera adecuada.

------

[IQDOTNET CODE](https://www.facebook.com/IQDotNetCode) - by NelsoN