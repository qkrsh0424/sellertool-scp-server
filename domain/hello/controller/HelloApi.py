from http import HTTPStatus
from flask import request
from flask_restx import Namespace, Resource

from domain.message.dto.Message import Message

HelloApi = Namespace("HelloApi")

@HelloApi.route('')
class Hello(Resource):
    def get(self):
        message = Message()
        hello = request.args.get('hello', default = None, type = str)
        world = request.args.get('world', default = None, type =str)

        print('param hello : {0}'.format(hello))
        print('param world : {0}'.format(world))


        message.setStatus(HTTPStatus.OK)
        message.setMessage("success")
        message.setData(None)
        return message.__dict__, message.statusCode, {'ContentType': 'application/json'}