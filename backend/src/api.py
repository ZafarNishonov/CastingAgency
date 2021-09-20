import os
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS

from .database.models import setup_db, Actors, Movies
from .auth.auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"Finally! I have done it! Casting Agency API is working"})


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                          Endpoints for movies                        #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


    @app.route('/actors', methods=['GET'])
    def show_actors():
        query_actors = Actors.query.all()

        if query_actors is None:
            abort(404)

        actors = [actors.short() for actors in query_actors]
        return jsonify({
            'success': True,
            'actors': actors
            })


    @app.route('/actors/<int:id>', methods=['GET'])
    def show_actor():
        query_actor = Actors.query.filter_by(Actors.id == id).one_or_none()
        actor = [actor.short() for actor in query_actor]
        return jsonify({
            'success': True,
            'actor_info': actor
            }), 200


    @app.route('/actors-detail', methods=['GET'])
    @requires_auth('get:actors-detail')
    def actors_detail(payload):
        query_actors = Actors.query.all()

        if query_actors is None:
            abort(404)

        actors = [actors.long() for actors in query_actors]
        return jsonify({
            'success': True,
            'actors_detail': actors
            })

    
    @app.route('/actors/<int:id>/detail', methods=['GET'])
    @requires_auth('get:actors/<id>/detail')
    def actor_detail(payload, id):
        query_actor = Actors.query.filter_by(Actors.id == id).one_or_none()

        if query_actor is None:
            abort(404)

        actor = [actor.long() for actor in query_actor]
        return jsonify({
            'success': True,
            'actor_detail': actor
            })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actors(payload):
        body = request.get_json()
        try:
            name = body.get('name')
            age = body.get('age')
            gender = body.get('gender')
            birth_day = body.get('birth_day')
            birth_place = body.get('birth_place')

            new_actor = Actors(name=name, age=age, gender=gender, birth_day=birth_day, birth_place=birth_place)

            new_actor.insert()

            actor = [new_actor.short()]
            return jsonify({
                'success': True,
                'new_actor': actor
                })

        except:
            abort(422)

    @app.route('/actors<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(payload, id):
        query_actor = Actors.query.filter_by(Actors.id == id).one_or_none()
        body = request.get_json()

        if query_actor is None:
            abort(404)

        try:
            name = body.get('name')
            age = body.get('age')
            gender = body.get('gender')
            birth_day = body.get('birth_day')
            birth_place = body,get('birth_place')

            edited_actor = Actors(name=name, age=age, gender=gender, birth_day=birth_day, birth_place=birth_place)

            edited_actor.update()

            actor = [edited_actor.short()]
            return ({
                'success': True,
                'edited_actor': actor
                })

        except:
            abort(422)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        query_actor = Actors.query.filter_by(Actors.id == id).one_or_none()

        if query_actor is None:
            abort(404)

        try:
            query_actor.delete()

            actor = [query_actor.short()]

            return jsonify ({
                'success': True,
                'deleted_actor': actor
                })


        except:
            abort(422)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                          Endpoints for movies                        #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


    @app.route('/movies', methods=['GET'])
#    @requires_auth('get:movies')
    def show_movies():
        query_movies = Movies.query.all()

        if query_movies is None:
            abort(404)

        movies = [movies.short() for movies in query_movies]
        return jsonify({
            'success': True,
            'movies': movies
            })


    @app.route('/movies/<int:id>', methods=['GET'])
#    @requires_auth('get:movies/<id>')
    def show_movie():
        query_movie = Movies.query.filter_by(Movies.id == id).one_or_none()

        if query_movie is None:
            abort(404)

        movie = [movie.short() for movie in query_movie]
        return jsonify({
            'success': True,
            'movie_info': movie
            })


    @app.route('/movies-detail', methods=['GET'])
    @requires_auth('get:movies-detail')
    def movies_detail(payload):
        query_movies = Movies.query.all()

        if query_movies is None:
            abort(404)

        movies = [movies.long() for movies in query_movies]
        return jsonify({
            'success': True,
            'movies_detail': movies
            })

    
    @app.route('/movies/<int:id>/detail', methods=['GET'])
    @requires_auth('get:movies/<id>/detail')
    def movie_detail(payload, id):
        query_movie = Movies.query.filter_by(Movies.id == id).one_or_none()

        if query_movie is None:
            abort(404)

        movie = [movie.long() for movie in query_movie]
        return jsonify({
            'success': True,
            'movie_detail': movie
            })

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movies(payload):
        body = request.get_json()
        try:
            title = body.get('title')
            release_date = body.get('release_date')
            budget = body.get('budget')
            producer = body.get('producer')
            genres = body,get('genres')

            new_movie = Movies(title=title, release_date=release_date, budget=budget, producer=producer, genres=genres)

            new_movie.insert()

            movie = [new_movie.short()]
            return jsonify({
                'success': True,
                'new_movie': movie
                })

        except:
            abort(422)

    @app.route('/movies<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(payload, id):
        query_movie = Movies.query.filter_by(Movies.id == id).one_or_none()
        body = request.get_json()

        if query_movie is None:
            abort(404)

        try:
            title = body.get('title')
            release_date = body.get('release_date')
            budget = body.get('budget')
            producer = body.get('producer')
            genres = body,get('genres')

            edited_movie = Movies(title=title, release_date=release_date, budget=budget, producer=producer, genres=genres)

            edited_movie.update()

            movie = [edited_movie.short()]
            return ({
                'success': True,
                'edited_movie': movie
                })

        except:
            abort(422)

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        query_movie = Movies.query.filter_by(Movies.id == id).one_or_none()

        if query_movie is None:
            abort(404)

        try:
            query_movie.delete()

            movie = [query_movie.short()]

            return jsonify ({
                'success': True,
                'deleted_movie': movie
                })


        except:
            abort(422)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                          Errorhandlers                               #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  unprocessable                   #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  not found                       #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "not found"
        }), 404
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  unauthorized                    #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    
    
    @app.errorhandler(AuthError)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code


    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

