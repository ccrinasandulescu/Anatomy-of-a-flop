import requests
import pandas as pd
import os
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

def get_movies(total_pages=100):
    """Descarcă filme de pe TMDB"""
    movies = []
    
    for page in range(1, total_pages + 1):
        url = "https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": API_KEY,
            "language": "en-US",
            "sort_by": "popularity.desc",
            "include_adult": False,
            "page": page,
            "vote_count.gte": 100
        }
        response = requests.get(url, params=params)
        data = response.json()
        movies.extend(data.get("results", []))
        
        if page % 10 == 0:
            print(f"Descărcat pagina {page}/{total_pages}")
        time.sleep(0.25)
    
    return pd.DataFrame(movies)

def get_movie_details(movie_id):
    """Descarcă detalii complete pentru un film"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    return response.json()

def build_dataset(total_pages=50):
    """Construiește dataset-ul complet"""
    print("Descărcăm lista de filme...")
    df = get_movies(total_pages)
    
    budgets, revenues, runtimes = [], [], []
    
    print("Descărcăm detalii pentru fiecare film...")
    for i, movie_id in enumerate(df["id"]):
        details = get_movie_details(movie_id)
        budgets.append(details.get("budget", 0))
        revenues.append(details.get("revenue", 0))
        runtimes.append(details.get("runtime", 0))
        
        if i % 100 == 0:
            print(f"Film {i}/{len(df)}")
        time.sleep(0.25)
    
    df["budget"] = budgets
    df["revenue"] = revenues
    df["runtime"] = runtimes
    
    return df

if __name__ == "__main__":
    df = build_dataset(total_pages=50)
    df.to_csv("data/movies_raw.csv", index=False)
    print(f"Salvat! {len(df)} filme în data/movies_raw.csv")
    