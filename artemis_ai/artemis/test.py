import os
import bottle
from bottle import route, run, post, Response


app = bottle.default_app()


@route('/')
def index():
    """Returns standard text response to show app is working."""
    return Response("Bottle app up and running!")


if __name__ == '__main__':
    run(host='127.0.0.1', port=5000, debug=False, reloader=True)