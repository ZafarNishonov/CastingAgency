# Casting Agency API - Udacity FSND Capstone project
------------------------------------------------------------------------
## Introduction

<a href="https://online-casting-agency.herokuapp.com">Casting Agency</a> is the final (5th) project od Udacity FSND. The main goal of this project is to write an API (build backend) for the Capstone project and deploy it live to heroku.
Casting Agency is an API that helps different users to make requests to various endpoints of the API.

### The API is running on:

 https://online-casting-agency.herokuapp.com



## Getting started

### Pre-requisites and Local Development

To run this project make sure that you have already installed <a href="python.org">Python <img style="width: 25px; height: 25px" src="https://icons.iconarchive.com/icons/cornmanthe3rd/plex/16/Other-python-icon.png"/></a>(for backend), 
<a href="postgresql.org">Postgresql<img style="width: 20px; height: 20px" src="https://cdn.iconscout.com/icon/free/png-64/postgresql-3521647-2945091.png"></a>(as database), <a href="git-scm.com">Git <img style="width: 30px; height: 30px" src="https://cdn.iconscout.com/icon/free/png-64/git-17-1175218.png"></a>(to run commands), <a href="getpostman.com">Postman <img style="width: 20px; height: 20px" src="https://cdn.iconscout.com/icon/free/png-64/postman-3628992-3030217.png"></a>(for testing)

#### 1. First of all install python libraries and packages that are required for correct work of backend. Run this command from the `backend` folder:

```bash
 pip install -r requirements.txt
```

#### 2. Run next commands in `Git Bash` to create database named `trivia`:

```bash
psql -U {username}
#password for username
CREATE DATABASE casting_agency;
```

#### 3. Run this command from `backend` folder to upgrade database:

```
python manage.py db upgrade
```

#### 4. Finally start the API:

```
python manage.py runserver
```


## Authentication

#### The login page is <a href="https://fsnd-udacity-project.us.auth0.com/authorize?audience=casting_agency&response_type=token&client_id=9pgVHkMpuL7DrsSjhpOn1swtgYtqDCWw&redirect_uri=http://127.0.0.1:8100/login-results">here </a> 

 1. This API is using auht0 authentication system

 2. There are 5 public endpoints:

  ```
  GET '/'
  GET '/actors'
  GET '/movies'
  GET '/actors/<id>'
  GET '/movies/<id>'
  ```
 So this endpoints can be reached by anyone and do not require authentication

 3. Users and passwords:
      * Casting Assistant   - assistant@capstone.com `CAassistant5!`
      * Casting Director    - director@capstone.com  `CAdirector5!` 
      * Executive Producer  - producer@capstone.com  `CAproducer5!` 

 4. Here are roles and permissions:

  ```
  casting assistant:
    - get:actors
    - get:movies
    - get:actors/<id>
    - get:movies/<id>
    - get:actors-detail
    - get:movies-detail

  casting director:
    - get:actors
    - get:movies
    - get:actors/<id>
    - get:movies/<id>
    - get:actors-detail
    - get:movies-detail
    - get:actors/<id>/detail
    - get:movies/<id>/detail
    - post:actors
    - patch:actors
    - delete:actors

  executive producer:
    - get:actors
    - get:movies
    - get:actors/<id>
    - get:movies/<id>
    - get:actors-detail
    - get:movies-detail
    - get:actors/<id>/detail
    - get:movies/<id>/detail
    - post:actors
    - patch:actors
    - delete:actors
    - post:movies
    - patch:movies
    -delete:movies

  ```

 * The logout page is <a href="https://fsnd-udacity-project.us.auth0.com/logout">here</a>

## Errors

 * There are 3 errorhandlers:
   
  * 401 - AuhtError `unauthorized`
  * 404 - `not found`
  * 422 - `unprocessable`


## API Testing

* For this project I used <b>Postman</b> for testing

1. There are two postman collections for testing:
  * First (capstone.postman_collection.json) is for testing API that is running locally.
  * Second (heroku.postman_collection.json) is for tesing API that is running on heroku.com

2. Import collections.

3. Run collections.


# API Documentation

## GET `/`

1. This endpoint is public.

2. Permission is not required.

3. Request:

```postman
GET `http://127.0.0.1:5000`
```

4. Response:

```
Finally! I have done it! Casting Agency API is working
```

5. There are no errors for this endpoint.


## GET `actors`

1. This endpoint is public.

2. Permission is not required.

3. Request:

```postman
GET `http://127.0.0.1:5000/actors`
```

4. Response:

```
{
  "actors":[],
  "success":true
}
```

5. There is 404 errorhandler for this endpoint.


## GET `movies`

1. This endpoint is public.

2. Permission is not required.

3. Request:

```postman
GET `http://127.0.0.1:5000/movies`
```

4. Response:

```
{
  "movies":[],
  "success":true
}
```

5. There is 404 errorhandler for this endpoint.


## GET `actors/<id>`


1. This endpoint is public.

2. Permission is not required.

3. Request:

```postman
GET `http://127.0.0.1:5000/actors/<id>`
```

4. Response:

```
{
  "success": True,
  "actor": []
}
```

5. There are no errorhandlers for this endpoint.


## GET `movies/<id>`


1. This endpoint is public.

2. Permission is not required.

3. Request:

```postman
GET `http://127.0.0.1:5000/movies/<id>`
```

4. Response:

```
{
  "success": True,
  "movie": []
}
```

5. There are no errorhandlers for this endpoint.


## GET `actors-detail`


1. This endpoint is not public.

2. Permission is required:

  * `get:actors-detail`

3. Request:

```postman
GET `http://127.0.0.1:5000/actors-detail`
```

4. Response:

```
{
    "actors_detail": [],
    "success": true
}
```

5. There is 401 errorhandler for this endpoint.


## GET `movies-detail`


1. This endpoint is not public.

2. Permission is required:

  * `get:movies-detail`

3. Request:

```postman
GET `http://127.0.0.1:5000/movies-detail`
```

4. Response:

```
{
    "movies_detail": [],
    "success": true
}
```

5. There is 401 errorhandler for this endpoint.


## GET `actors-detail`


1. This endpoint is not public.

2. Permission is required:

  * `get:actors/<id>/detail`

3. Request:

```postman
GET `http://127.0.0.1:5000/actors/<id>/detail`
```

4. Response:

```
{
    "actor_detail": [],
    "success": true
}
```

5. There is 401 errorhandler for this endpoint.


## GET `movies/<id>/detail`


1. This endpoint is not public.

2. Permission is required:

  * `get:movies/<id>/detail`

3. Request:

```postman
GET `http://127.0.0.1:5000/movies/<id>/detail`
```

4. Response:

```
{
    "movie_detail": [],
    "success": true
}
```

5. There is 401 errorhandler for this endpoint.


## POST `actors`


1. This endpoint is not public.

2. Permission is required:

  * `post:actors`

3. Request:

```postman
POST `http://127.0.0.1:5000/actors`

json ({
  'name': <name>,
  'age': <age>,
  'gender': <gender>,
  'birth_day': <birth_day>,
  'birth_place': <birth_place>
  })

```

4. Response:

```
{
  'success': True,
  'new_actor': []
}
```

5. There is 401 errorhandler for this endpoint.


## POST `movies`


1. This endpoint is not public.

2. Permission is required:

  * `post:movies`

3. Request:

```postman
POST `http://127.0.0.1:5000/movies`

json ({
  'title': <title>,
  'release_date': <release_date>,
  'budget': <budget>,
  'producer': <producer>,
  })

```

4. Response:

```
{
  'success': True,
  'new_movie': []
}
```

5. There is 401 errorhandler for this endpoint.


## PATCH `actors/<id>`


1. This endpoint is not public.

2. Permission is required:

  * `patch:actors`

3. Request:

```postman
PATCH `http://127.0.0.1:5000/actors/<id>`

json ({
  'name': <name>,
  'age': <age>,
  'gender': <gender>,
  'birth_day': <birth_day>,
  'birth_place': <birth_place>
  })

```

4. Response:

```
{
  'success': True,
  'edited_actor': []
}
```

5. There is 401 errorhandler for this endpoint.


## PATCH `movies/<id>`


1. This endpoint is not public.

2. Permission is required:

  * `patch:movies`

3. Request:

```postman
PATCH `http://127.0.0.1:5000/movies/<id>`

json ({
  'title': <title>,
  'release_date': <release_date>,
  'budget': <budget>,
  'producer': <producer>,
  })

```

4. Response:

```
{
  'success': True,
  'edited_movie': []
}
```

5. There is 401 errorhandler for this endpoint.



## DELETE `actors/<id>`

1. This endpoint is not public.

2. Permission is required:

  * `delete:actors`

3. Request:

```postman
DELETE `http://127.0.0.1:5000/actors/<id>`
```

4. Response:

```
{
  'success': True,
  'deleted_actor': []
}
```

5. There is 401 errorhandler for this endpoint.


## DELETE `movies/<id>`

1. This endpoint is not public.

2. Permission is required:

  * `delete:movies`

3. Request:

```postman
DELETE `http://127.0.0.1:5000/movies/<id>`
```

4. Response:

```
{
  'success': True,
  'deleted_movie': []
}
```

5. There is 401 errorhandler for this endpoint.


# Author:

  ©Zafar Nishonov 

# CastingAgency
