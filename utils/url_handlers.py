__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from typing import Callable, Dict, List
from flask import Flask
from flask_restful import Api, Resource
from flask_socketio import SocketIO


def add_api_resource(resource: Resource, urls: tuple, endpoint: str, api: Api) -> None:
    urls = tuple([f"/api/v1/{route}" for route in urls])
    api.add_resource(resource, *urls, endpoint=endpoint)


def register_api_urls(api_urls: Dict, api: Api) -> None:
    for api_url in api_urls:
        add_api_resource(api_url.get("resource"), api_url.get("urls"), api_url.get("endpoint"), api)


def add_app_url(func: Callable, url: str, app: Flask, endpoint: str, method: List) -> None:
    app.add_url_rule(f"/api/v1/{url}", endpoint=endpoint, view_func=func, methods=method)


def register_app_urls(app_urls: List, app: Flask) -> None:
    for app_url in app_urls:
        add_app_url(app_url.get("func"), app_url.get("url"), app, app_url.get("endpoint"), method=app_url.get("methods"))


def add_views(func: Callable, url: str, app: Flask) -> None:
    app.add_url_rule(f"/api/v1/{url}", view_func=func)


def register_views(views: List, app: Flask) -> None:
    for view in views:
        add_views(view.get("func"), view.get("url"), app)


def register_events(events: List, socketio: SocketIO) -> None:
    for event in events:
        socketio.on_event(event.get("event"), event.get("func"), event.get("namespace"))
