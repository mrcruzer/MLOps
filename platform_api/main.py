#Importo dependencias/librerías necesarias
from fastapi import FastAPI
import pandas as pd
from pandasql import sqldf
import os
import numpy as np
os.environ["OPENBLAS_L2SIZE"]="512k"
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse


#creo una instancia de FastAPI
app = FastAPI(title='API - Score Movies - By Isaac Avelino')


# Endpoint principal
@app.get("/")
async def index():
    html_content = """
    <!DOCTYPE html>
<html>
<head>
<style>
body {
	margin: 0;
	padding: 0;
	font-family: Arial, sans-serif;
}

header {
	background-color: #333;
	color: #fff;
	padding: 10px 20px;
}

nav ul {
	list-style: none;
	margin: 0;
	padding: 0;
}

nav li {
	display: inline-block;
	margin-right: 20px;
}

nav a {
	color: #fff;
	text-decoration: none;
}

main {
	margin: 20px;
}

section {
	margin-bottom: 20px;
}

.contenido {
	display: flex;
	flex-direction: column;
	align-items: center;
}

img {
	width: 50%;
	height: auto;
	margin-bottom: 20px;
}

button {
	background-color: #333;
	color: #fff;
	padding: 10px 20px;
	border: none;
	border-radius: 5px;
	font-size: 16px;
	cursor: pointer;
}
</style>
	<title>Mi página web</title>
	<link rel="stylesheet" type="text/css" href="estilos.css">
</head>
<body>
	<header>
		<h1>API</h1>
		<nav>
			<ul>
				<li><a href="/">Inicio</a></li>
				<li><a href="/about/">Acerca de</a></li>
			</ul>
		</nav>
	</header>
	<main>
		<section>
			<div class="contenido">
				<img src="https://raw.githubusercontent.com/mrcruzer/MLOps/main/src/plataformas.png" alt="Imagen">
                <form action="/docs">
                    <button type="submit">Consultas</button>
                </form>
			</div>
		</section>
	</main>
</body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get('/about/')
async def about():
    return {'Proyecto, Realizado por Isaac Avelino'}


# 1 - Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))
@app.get("/get_max_duration/")
def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    df = pd.read_csv('./datasets/movies_completo_api.csv')

    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                         'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                         'hulu': ['h', 'hu', 'hul', 'hulu'],
                         'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    duration_dict = {'min': ['min', 'mi', 'm'], 'season': ['season', 's', 'se', 'sea', 'seas', 'seaso']}

    # Buscar la plataforma correspondiente en el diccionario
    platform_complete = platform_dict.get(platform, platform)

    # Buscar el tipo de duración correspondiente en el diccionario
    duration_type_complete = duration_type
    for duration, combos in duration_dict.items():
        if duration_type in combos:
            duration_type_full = duration


    # Filtrar el DataFrame
    if duration_type_complete is not None:
        filtered_df = df[df['duration_type'] == duration_type_complete]
    else:
        filtered_df = df.copy()
    if year is not None:
        filtered_df = filtered_df[filtered_df['release_year'] == year]
    if platform_complete is not None:
        filtered_df = filtered_df[filtered_df['platform'] == platform_complete]

    # Ordenar el DataFrame y obtener la fila con la duración máxima
    sorted_df = filtered_df.sort_values(by='duration_int', ascending=False)
    max_duration = sorted_df.iloc[0][['title']]
    
    return max_duration
    
# 2 - Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))   
@app.get("/get_score_count/")
def get_score_count(platform: str, scored: int, year: int):
    df = pd.read_csv('./datasets/movies_completo_api.csv')
    
    if platform == "amazon":
        plat = "a%"
    elif platform == "disney":
        plat = "d%"
    elif platform == "hulu":
        plat = "h%"
    elif platform == "netflix":
        plat = "n%"
    else:
        return ("Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")

    filter_movies = df[(df['platform'] == platform) & (df['release_year'] == year) & (df['score_medio'] > scored)]
    count_movies = filter_movies.shape[0]

    return {'Platform': platform, 'Count Movies': count_movies, 'Year': year}

 
# 3 - Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))
@app.get("/get_count_platform/")
def get_count_platform(platform: str):
    df = pd.read_csv('./datasets/movies_completo_api.csv')
    
    if platform != "amazon":
        plat = "amazon"
    elif platform != "disney":
        plat = "disney"
    elif platform != "hulu":
        plat = "hulu"
    elif platform != "netflix":
        plat = "netflix"
    else:
        return ("Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")

    filter_movies = df[df['platform'] == plat]
    count_movies = filter_movies.shape[0]

    return {'Platform': platform, 'Count Movies': count_movies}
    

# 4 - Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
@app.get("/get_actor")
def get_actor(platform: str, year: int ):
    # Cargar el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv('./datasets/movies_completo_api.csv')
    
    if platform == "amazon":
            plat = "a%"
    elif platform == "disney":
        plat = "d%"
    elif platform == "hulu":
        plat = "h%"
    elif platform == "netflix":
        plat = "n%"
    else:
        return ("Las opciones son: amazon, disney, hulu, netflix. Recuerde escribir todo en minúsculas.")
    
    
    filter_movies = df[(df['platform'] == platform) & (df['release_year'] == year)]
    cast_filter = filter_movies['cast'].str.split(',').explode()
    cast_repetidos = cast_filter.value_counts().index[0]
    
    return {'Platform': platform, 'Year': year, 'Actor mas repetido': cast_repetidos}
