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

1- Transformaciones:
He utilizado python, las librerias pandas y numpy. 
Tengo dos notebook: [Links](https://github.com/mrcruzer/MLOps/blob/main/transform_data_api.ipynb "transform_data_api.ipynb"), Para la parte de la API generando un csv ubicado en scored_api
transform_data_ML y por último convertí el dataframe en el archivo data.csv para utilizar en la elaboración de la API.