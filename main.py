import pandas as pd
import numpy as np


# Cargar los datos de películas y usuarios en un DataFrame de pandas
data = pd.read_csv("ratings.csv") # suponiendo que los datos están en un archivo CSV

# Crear una matriz de usuarios y películas, donde las entradas representan las calificaciones dadas por los usuarios a las películas
ratings_matrix = data.pivot_table(index='userId', columns='id', values='score')

# Rellenar los valores faltantes (donde el usuario no ha calificado la película) con ceros
ratings_matrix.fillna(0, inplace=True)

# Descomposición de valores singulares (SVD) para reducir la dimensión de la matriz
svd = TruncatedSVD(n_components=20) # elegimos 20 componentes principales
latent_matrix = svd.fit_transform(ratings_matrix)

# Calcular la similitud coseno entre las películas
movie_similarity = cosine_similarity(latent_matrix)

# Definir una función para obtener las películas más similares a una película determinada
def get_similar_movies(movie_id):
    similarity_scores = movie_similarity[movie_id]
    similar_movies = []
    for idx, score in enumerate(similarity_scores):
        if idx != movie_id:
            similar_movies.append((idx, score))
    return similar_movies

# Definir una función para obtener las recomendaciones de películas para un usuario dado
def get_recommendations(user_id, movie_id):
    # Obtener las películas más similares a la película dada
    similar_movies = get_similar_movies(movie_id)

    # Calcular las calificaciones predictivas para las películas similares basadas en el historial del usuario
    user_ratings = ratings_matrix.loc[user_id]
    predicted_ratings = np.zeros(ratings_matrix.shape[1])
    for movie, score in similar_movies:
        predicted_ratings += score * ratings_matrix.loc[:, movie]
    predicted_ratings /= np.sum([score for movie, score in similar_movies])
    
    # Filtrar las películas que el usuario ya ha visto
    seen_movies = list(user_ratings[user_ratings > 0].index)
    unseen_movies = [movie for movie in ratings_matrix.columns if movie not in seen_movies]
    predicted_ratings = predicted_ratings[unseen_movies]
    
    # Obtener el índice de la película recomendada con la calificación más alta
    movie_idx = np.argmax(predicted_ratings)
    recommended_movie = predicted_ratings.index[movie_idx]
    
    return recommended_movie