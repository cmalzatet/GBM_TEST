CLASIFICADOR DE CLIENTES

Este ejercicio se realizó en un cuaderno de jupyter para facilitar su manejo y observación
En este se realiza un procesamiento y análisis de dato para generar un modelo que clasifique a los clientes de una tienda en clientes de alto, medio o bajo valor

- Inicialmente se hace una carga y procesamiento del conjunto de datos para que esten acordes a sus formatos

- Se procesan los datos para extraer características de cada cliente individual, estas siendo:
-- total gastado
-- promedio gastado
-- máximo gastado
-- total de visitas
-- total meses visitados
-- promedio mensual gastado
-- promedio mensual visitado

- Se utiliza un modelo de K-vecinos más cercanos para clasificar los clientes en los tres grupos a partir de sus hábitos de compra, obteniendo etiquetas 0-bajo valor, 1-medio valor, 2-alto valor

- Como en total solo hay menos de 7000 clientes, esta es una cantidad de datos insuficiente para entrenar adecuadamente una red neuronal, por lo que se decide entrenar un bosque aleatorio (argumentando el no uso de keras en este ejercicio)

- Se hace la partición de los datos, el entrenamiento del modelo y verificación de su desempeño

NOTA 1: El programa requiere las librerías:
-- pandas
-- seaborn
-- matplotlib
-- sklearn
