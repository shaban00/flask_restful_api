__author__ = "Shaban Hassan"

from typing import Dict
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from app import create_app, socketio
from utils.exceptions import BaseError
from utils.url_handlers import register_api_urls, register_app_urls, register_events, register_views
from urls import API_URLS, APP_URLS, SOCKET_EVENTS, VIEWS


app, mail = create_app()

handle_exceptions = app.handle_exception
handle_user_exceptions = app.handle_user_exception


api = Api(app)

socketio.init_app(app, cors_allowed_origins="*")


register_api_urls(API_URLS, api)
register_app_urls(APP_URLS, app)
register_events(SOCKET_EVENTS, socketio)
register_views(VIEWS, app)


app.handle_exception = handle_exceptions
app.handle_user_exception = handle_user_exceptions


@app.errorhandler(BaseError)
def handle_errors(error: BaseError) -> Dict:
    response = jsonify({
        "error": error.to_dict()
    })
    response.status_code = error.error_code
    return response

@app.errorhandler(404)
def url_not_found(error):
    '''
    Handler for errors that occur when the url for a request cannot be found
    '''
    response = jsonify({
        "error": {
            "message": "Url not found"
        }
    })
    response.status_code = 404
    return response


@app.errorhandler(405)
def method_not_allowed(error):
    '''
    Handler for errors that occur as a result of an invalid HTTP method to a route
    '''
    response = jsonify({
        "error": {
            "message": "This HTTP method is not allowed on this route"
        }
    })
    response.status_code = 405
    return response


@app.errorhandler(500)
def handle_server_error(error):
    '''
    Handler for returning sensible messages to users when an unknown exception occurs.
    '''
    # we want to rollback any uncommitted db changes
    # this error would have been logged already
    response = jsonify({
        "error": {
            "message": "An error occurred from our end. The backend developers are actively investigating this; an email has been sent to the team lead"
        }
    })
    response.status_code = 500
    return response


@app.after_request
def after_request(response):
    '''
    Called after every request, when returning the response.
    We add extra fields to the response header.
    :param response(flask_restful.Response): The response returned for the current request
    '''
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods',
                         'POST, GET, OPTIONS, DELETE')
    response.headers.add('Access-Control-Allow-Headers',
                         'content-type, Authorization')
    return response

if __name__ == '__main__':
    socketio.run(app, port=5000, host='0.0.0.0')
    # app.run(debug=True, use_evalex=False, host='0.0.0.0', port=5000)