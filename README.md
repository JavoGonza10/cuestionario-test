# Cuestionario Test

Un cuestionario tipo test que hice en Python para un proyecto de clase (módulo MPO). La idea parecia simple al principio: un menú, unas preguntas, corregirlas y dar una nota final. A medida que fui agregando las mejoras se ponia bastante más complejo: puedes elegir de qué tema quieres las preguntas, hay un tiempo límite para responder, y se guarda un ranking que aguanta aunque cierres el programa.

## ¿Qué puedes hacer con él?

- Jugar un cuestionario de preguntas tipo test (A/B/C/D) desde la consola.
- Elegir el tema antes de empezar: geografía, astronomía o música.
- Responder cada pregunta antes de que se acabe el tiempo (si no, cuenta como fallo).
- Ver al momento si acertaste o fallaste cada pregunta.
- Al terminar, ver tu porcentaje de aciertos y una valoración de cómo te fue.
- Consultar el ranking con las partidas de todos los que han jugado, ordenado de mejor a peor.
- Cerrar el programa y volver más tarde sin perder el ranking (se guarda en `ranking.json`).

## Cómo lo ejecutas

Necesitas Python instalado (lo hice con la 3.14, pero debería funcionar con versiones algo más antiguas también). No usa ninguna librería externa, así que no hay que instalar nada más.

```bash
python main.py
```

Y ya está, te sale el menú.

## Qué hay en la carpeta

- `main.py` — todo el código del cuestionario.
- `ranking.json` — se crea solo la primera vez que juegas alguien; ahí se van guardando los resultados. No está en el repositorio (lo excluí con `.gitignore`) porque es un archivo que se genera al jugar, no código.

## Autor

Javi
