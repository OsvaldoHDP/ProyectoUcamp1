# ProyectoUcamp1
Calculadora de IMC en Python

Este es mi primer proyecto del módulo de Fundamentos de Python del bootcamp. Consiste en una calculadora de Índice de Masa Corporal (IMC).

¿Qué hace el programa?

El programa le pide al usuario que ingrese su nombre, apellidos, edad, peso y estatura. Con esos datos calcula el IMC usando la fórmula:

IMC = peso / estatura²
Al final muestra todos los datos junto con el resultado y el dice al usuario en qué categoría está (bajo peso, peso normal, sobrepeso u obesidad).

¿Cómo lo hice?

La verdad al principio no sabía muy bien por donde empezar, pero fui dividiendo el problema en partes más pequeñas. Cabe mencionar que tuve que investigar sobre la sintaxis de python de los que aún no me habían explicado, pero base la experiencia en programar en otros idiomas pude hacer uso de bucles y en este caso encontré el bloque de try/except para mejor validación de datos de entrada.

Captura de datos Lo primero fue usar input() para pedirle los datos al usuario y guardarlos en variables. Para los textos como el nombre fue simple, solo tuve que asegurarme de que no queden vacíos con un tiempo.

Validación Esta parte fue la más complicada para mí. Tuve que asegurarme de que el usuario no dejará campos vacíos y que en edad, peso y estatura sí ingresará un número. Para eso use try/except, que básicamente le dice al programa: "intenta convertir esto a número, y si no puedes, muestra un error y vuelve a pedir el dato" en lugar de que el programa truene.

El cálculo Una vez que tenia los datos validados, el cálculo fue la parte más fácil. Solo apliqué la formula con el operador ** para elevar la estatura al cuadrado.

La salida Por último imprimí todo con print(), concatenando las variables con cadenas de texto usando + y convirtiendo los números a texto con str().

¿Qué aprendí?

A usar variables de distintos tipos: str, int y float.
A validar datos con while y try/except, que es tema que adelanté base a mis conocimientos previos.
A usar operadores matemáticos dentro del código basado en python
Que dividir un problema grande en partes pequeñas hace todo mucho más manejable.
Lo que más me costó trabajo fue la validación, porque hay que pensar en todos los casos en los que el usuario puede meter algo incorrecto. Más que nada fue mi propia exigencia de que el código tuviera mejor ejecución.

Reflexión del bootcamp

Hasta ahora el bootcamp me ha enseñado que programar no es solo escribir código que funcione, sino escribir código que sea claro y que no se rompa cuando el usuario hace algo inesperado. Eso fue exactamente lo que practiqué en este proyecto.

Todavía me falta mucho por aprender pero siento que ya tengo una base más sólida de cómo estructurar un programa desde cero.
