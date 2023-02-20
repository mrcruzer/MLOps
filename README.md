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
[transform_data_ML](https://github.com/mrcruzer/MLOps/blob/main/transform_data_ML.ipynb), Genere un archivo con extension .parquet para ahorrar espacio.

- Genere un campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

- Reemplaze Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

- Cambie el formato de las fechas, las pase a formato Datetime, con el formato AAAA-mm-dd

- Los campos de texto los coloque en minúsculas, sin excepciones

- Separe el campo duration en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

2 - Desarrollo de la API en FastAPI:

Para esta parte use un entorno virtual donde se instaló FastAPI, Pandas y Uvicorn. Desarrollé la API con FastApi (ubicado en scored/api [main.py](https://github.com/mrcruzer/MLOps/blob/main/scored_api/main.py).

get_word_count: cantidad de veces que aparece una palabra en el título de peliculas o series, por plataforma.
get_score_count: cantidad de películas por plataforma con un puntaje mayor a 'xx' en determinado año.
get_second_score: la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
get_longest: película o serie que más duró según año, plataforma y tipo de duración.
get_rating_count: cantidad de series y películas por tipo de rating.
Durante la etapa de desarrollo revisé el funcionamiento integral de la API y sus consultas de manera local desde la terminal con el comando uvicorn main:app --reload en el localhost http://127.0.0.1:8000/ . Una vez logrado el adecuado funcionamiento de API de manera local realice en archivo de requerimientos con el comando pip freeze > requirements.txt.

Aclaracion: Si ha utilizado el comando pip freeze > requirements.txt en powershell Windows, el archivo creado no está codificado en UTF-8. Cambie la codificación o cree un nuevo archivo con la codificación correcta para poder realizar el deploy. No olvide borrar de los requerimientos a uvicorn ya que no es necesario para el deploy.