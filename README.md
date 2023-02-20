# PROYECTO 1 -- Machine Learning Operations (MLOps)

### Tema principal

Este proyecto consiste en hacer un proceso ETL sobre cuatro datasets proporcionados, conteniendo información relativa a los catálogos de series y películas de cuatro plataformas de streaming (Netflix, Hulu, Amazon Prime Video y Disney).

Por igual solicitaba elaborar una API a efectos de disponibilizar los datos de manera online, los cuales debían ser accedidos mediante cuatro consultas predefinidas.

### Objetivos

- Efectuar el Análisis exploratorio de datos (EDA) a los datasets.
- Hacer las transformaciones necesarias y unificar el dataset.
- Realizar las consultas al dataset.
- Llevar a cabo el desarrollo de la API a través de FastApi.
- Ejecutar el deployment de la API en Deta.
- Crear un modelo de machine learning

### Datos

Tengo 4 datasets de HULU, DISNEY PLUS, AMAZON PRIME, NETFLIX

![](https://raw.githubusercontent.com/mrcruzer/MLOps/main/src/plataformas.png)

### Pasos:

`1- Transformaciones:`

He utilizado python, las librerias pandas y numpy. 
Tengo dos notebook: [transform_data_api.ipynb](https://github.com/mrcruzer/MLOps/blob/main/transform_data_api.ipynb), Para la parte de la API generando un csv movies_completo_api.csv ubicado en scored_api/datasets.
[transform_data_ML.ipynb](https://github.com/mrcruzer/MLOps/blob/main/transform_data_ML.ipynb), Genere un archivo con extension .parquet para ahorrar espacio.

- Genere un campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

- Reemplaze Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

- Cambie el formato de las fechas, las pase a formato Datetime, con el formato AAAA-mm-dd

- Los campos de texto los coloque en minúsculas, sin excepciones

- Separe el campo duration en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

`2 - Desarrollo de la API en FastAPI:`

Para esta parte use un entorno virtual donde se instaló FastAPI, Pandas y Uvicorn. Desarrollé la API con FastApi (ubicado en platform_api/api [main.py](https://github.com/mrcruzer/MLOps/blob/main/scored_api/main.py).

- get_max_duration(year, platform, duration_type): Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.

- get_score_count(platform, scored, year): Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

- get_count_platform(platform): Cantidad de películas por plataforma con filtro de PLATAFORMA.

- get_actor(platform, year): Actor que más se repite según plataforma y año.

`3 - Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)`

- Cantidad de filas:  9564574
- id object Valores no nulos:  9564574
- userId int64 Valores no nulos:  9564574
- score float64 Valores no nulos:  9564574
- title object Valores no nulos:  9564574

- 113937 usuarios únicos.
- los valores de score van en un rango de 1 a 5, con una media de 3.53

`4 - Deployment en Deta Space:`
Como primer paso hay que realizar una cuenta en Deta, luego crear una carpeta solo con los archivos main.py y requirements.txt:

iwr https://get.deta.dev/cli.ps1 -useb | iex -- Instalación del CLI.
space login -- Abre el navegador para que pueda loguearse con su cuenta .
space new --python -- Acaba de crear una nueva micro. Pruebe en el navegador el "endpoint" que otorga en la pantalla si dice "Hola Mundo" la conexión fue exitosa.
space push -- Realiza el deploy del proyecto
space release
space auth disable -- Disponibiliza el proyecto para cualquier persona.`