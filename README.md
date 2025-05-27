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
## Explicación del proyecto

Se busca crear el clásico juego **TETRIS**, utilizando clases y métodos, la idea es seccionar el código en sus diferentes funcionalidades como se ve en la `"Estructura de carpetas"`.

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

## Observaciones

- El juego unicamente se corre 1 vez, lo que quiere decir que para volver a jugar es necesario cerrar la ventana y volver a correr el programa.

- Los resultados no se guardan entre partidas debido a que es un código sencillo, por lo que podría mejorarse a futuro.

- Los comandos con las flechas (los controles) funcionan apretando 1 vez la tecla, si se deja presionada solo recibirá la primer orden y ya no hará nada.

- Es recomendable tener una carpeta .gitignore (Aunque esta se crea automaticamente con el ambiente virtual)
## Controles del juego

- Con la flecha izquierda "⬅️" la pieza se moverá en esa dirección.
- Con la flecha derecha "➡️" la pieza se moverá en esa dirección.
- Con la flecha hacia abajo "⬇️" la pieza acelerará y caerá más rápido.
- Con la flecha hacia arriba "⬆️" la pieza rotará.

## Funcionalidad del juego

El usuario verá una pantalla donde comenzarán a salir piezas con diferentes formas, la idea es ir apilandolas de tal forma que al llenar una fila (sin dejar huecos), está se borre y le de al usuario puntos.

Si el jugador permite que una ficha sobrepase el límite de la pantalla, el juego terminará y se mostrará su puntuación total.
