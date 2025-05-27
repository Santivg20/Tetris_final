# Tetris

**Autor:** Santiago Valenzuela Gil  

**Fecha:** Mayo de 2025

**Curso/Asignatura:** Programación 2 

**Profesor:** Oscar Leonel Sanchez Conde

## Introducción 

Se busca crear el clásico juego **TETRIS**, utilizando clases y métodos, la idea es seccionar el código en sus diferentes funcionalidades como se ve en la `"Estructura de carpetas"`.

## Estructura de carpetas

```bash
Juego-de-tetris/
    colors/
        colors.py
    settings/
        settings.py
    shapes/
        shapes.py
    tetris/
        tetris.py
    tetromino/
        tetromino.py
    main.py
    README.md
```
Aquí se separan distintas carpetas que permiten la funcionalidad total del juego, las cuales son:

- **Colors:** Aquí se almacenan y crean los colores para diferenciar cada una de las piezas.
- **Settings:** Aquí se configura la pantalla, el tamaño de las piezas y el tablero para el pygame.
- **Shapes:** Aquí se define la forma de cada una de las piezas.
- **Tetris:** En esta clase está todo el código del juego, con los atributos para el tetromino, el inicio de partida, el cierre de la misma, entre otras funciones.
- **Tetromino:** Esta clase permite la creación de las piezas para el juego.

## Controles del juego

- Con la flecha izquierda "⬅️" la pieza se moverá en esa dirección.
- Con la flecha derecha "➡️" la pieza se moverá en esa dirección.
- Con la flecha hacia abajo "⬇️" la pieza acelerará y caerá más rápido.
- Con la flecha hacia arriba "⬆️" la pieza rotará.

## Funcionalidad del juego

El usuario verá una pantalla donde comenzarán a salir piezas con diferentes formas, la idea es ir apilandolas de tal forma que al llenar una fila (sin dejar huecos), está se borre y le de al usuario puntos.

Si el jugador permite que una ficha sobrepase el límite de la pantalla, el juego terminará y se mostrará su puntuación total.

## Requisitos

### Crear y activar un entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### Instalar librerías necesarias

Se creó un archivo `requirements.txt` con lo siguiente:

```bash
pygame==2.6.1
```

**Para instalarlo:**

```bash
pip install -r requirements.txt
```

## Ejecución del programa

Para ejecutar el programa el usuario debe ubicarse en el archivo `main.py` y correr el programa en la terminal (o si existe algún botón que le permita hacerlo, también es posible).

```bash
python main.py
```
## Pruebas del programa

A la hora de probar el programa, fue necesario inicializar el pygame, con la intención de que los objetos se mostraran allí mismo, lo primero fue crear las piezas y que aparecieran en la pantalla, luego se creó su rotación, se le asignó la función de caida y así sucesivamente hasta la finalización del programa.

Fue un proceso extenso y en ocaciones tedioso debido al desconocimiento de pygame, pero con tiempo se consiguieron solucionar los problemas presentados y mostrar este producto final.

## Observaciones

- El juego unicamente se corre 1 vez, lo que quiere decir que para volver a jugar es necesario cerrar la ventana y volver a correr el programa.

- Los resultados no se guardan entre partidas debido a que es un código sencillo, por lo que podría mejorarse a futuro.

- Los comandos con las flechas (los controles) funcionan apretando 1 vez la tecla, si se deja presionada solo recibirá la primer orden y ya no hará nada.

- Es recomendable tener una carpeta .gitignore (Aunque esta se crea automaticamente con el ambiente virtual)

## Conclusiones

Al final del trabajo, se vieron reforzados los conocimientos sobre las clases, su implementación y su utilidad a la hora de programar códigos avanzados, además de el aprendizaje de una nueva librería como lo es pygame.

Algunas de las mejoras para este programa son:
- Implementar música de fondo para que el jugador no se aburra realizando la misma acción de forma reiterativa, así se haría mas ameno el juego.
- Implementar un avance del tiempo para que la velocidad de caida sea mayor y así incrementar el desafio y diversión para el usuario.
- Implementar un marcador, que permita guardar los puntajes de los jugadores y así intentar superar sus intentos previos.
- Implementar un menú de inicio.
- En la pantalla de "Game Over" colocar un botón de reintentar, para que el usuario no tenga que correr de nuevo el código para iniciar partida.

Pero aún con las falencias y debilidades del código, se aprendió bastante desarrollandolo y entendiendo sus funciones poco a poco, eso es lo que al menos yo me llevo del curso y de este trabajo como tal.
