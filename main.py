from flask import Flask, jsonify, request
import csv

from storage import all_movies,liked_movies,not_liked_movies,did_not_watch
#from demographic_filtering import output
from content_filtering import get_recommendations

all_movies = []

with open("movies.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
notliked_movies = []
didnotwatch = []

app = Flask(__name__)

@app.route("/get-movies")
def get_movies():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked-movies", methods = ["post"])
def liked_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movies)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/notliked-movies", methods = ["post"])
def notliked_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    notliked_movies.append(movies)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/didnotwatch", methods = ["post"])
def didnotwatch():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    didnotwatch.append(movies)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()