from datetime import datetime
from http import HTTPStatus


class Message(object):
    def __init__(self):
        self.status = HTTPStatus.BAD_REQUEST.phrase
        self.statusCode = HTTPStatus.BAD_REQUEST.value
        self.statusMessage = HTTPStatus.BAD_REQUEST.phrase
        self.data=None
        self.message=None
        self.memo=None
        self.timestamp = str(datetime.now())

    def setStatus(self, status):
        self.status = status.phrase
        self.statusCode = status.value
        self.statusMessage = status.phrase
    
    def setData(self, data):
        self.data = data
    
    def setMessage(self, message):
        self.message = message
    
    def setMemo(self, memo):
        self.memo = memo