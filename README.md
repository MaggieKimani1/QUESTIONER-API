# QUESTIONER-API

[![Build Status](https://travis-ci.com/MaggieKimani1/QUESTIONER-API.svg?branch=develop)](https://travis-ci.com/MaggieKimani1/QUESTIONER-API)
[![Coverage Status](https://coveralls.io/repos/github/MaggieKimani1/QUESTIONER-API/badge.svg?branch=develop)](https://coveralls.io/github/MaggieKimani1/QUESTIONER-API?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/043d24abfe9927d9ec1f/maintainability)](https://codeclimate.com/github/MaggieKimani1/QUESTIONER-API/maintainability)

## Brief Description

Questioner is a UI that hosts crowd-source questions for a meetup.

### Heroku link

[(https://kquestioner-api--heroku.herokuapp.com/)]

### Pivotal Tracker Board

[https://www.pivotaltracker.com/n/projects/2236318]

### Deploy

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/37d23da53d4fb0c08b92)

### Pre-requisites

1. Python3
2. Flask
3. Flask restful
4. Postman

### Getting started

Clone this repository
[https://github.com/MaggieKimani1/QUESTIONER-API.git]

Navigate to the cloned repository
`cd Questioner-API-v1`

### Installation

Create a virtual environment
`virtualenv -p python3 venv`

Activate the virtual environment
`source venv/bin/activate`

Install git
`sudo apt-get install git-all`

Switch to 'develop' branch
`git checkout develop`

Install requirements
`pip install -r requirements.txt`

Run the application
`python3 run.py`

### Endpoints

| Endpoint                            |                   Functionality                    |
| ----------------------------------- | :------------------------------------------------: |
| POST/meetups                        |               Create a meetup record               |
| GET/meetups/<meetup_id>             |           Fetch a specific meetup record           |
| GET /meetups/upcoming/              |         Fetch all upcoming meetup records          |
| POST /questions                     |      Create a question for a specific meetup       |
| PATCH /questions/<question_id>/vote | Vote (increase votes by 1) for a specific question |
| POST /meetups/<meetup_id>/rsvps     |             Respond to a meetup(RSVP)              |

### Authors

MAGGIE KIMANI

### License

This project is licensed under the MIT license.
