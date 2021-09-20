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


### Authentication

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
      - Casting Assistant   - CAassistant5!
      - Casting Director    - CAdirector5! 
      - Executive Producer  - CAproducer5! 

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






# CastingAgency
