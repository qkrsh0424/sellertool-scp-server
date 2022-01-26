from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import request
from flask_restx import Resource, Namespace
from http import HTTPStatus

from domain.message.dto.Message import Message
from domain.n_rank.service.NRankScrapingService import NRankScripingService
from domain.n_rank.service.NRankBusinessService import getAdRank
from structure.Queue import Queue

NRankApi = Namespace('NRankApi')


# TODO : 쓰레드 만들어야됨.
@NRankApi.route('')
class NRank(Resource):
    def get(self):
        message = Message()

        query = request.args.get('keyword', default=None, type=str)
        mallName = request.args.get('mallName', default=None, type=str)

        # query = '강아지옷'
        # mallName = '춘식이몰'
        if query == None or query == '' or mallName == None or mallName == '':
            message.setStatus(HTTPStatus.OK)
            message.setMessage("no_contents")
            message.setData(None)
            return message.__dict__, message.statusCode, {'ContentType': 'application/json'}

        nRankScrapingService = NRankScripingService(query)

        itemList = nRankScrapingService.scrapingWithThread()
            

        # itemList = nRankScrapingService.scrapingFirst(1,2)
        result = getAdRank(query, mallName, itemList)

        message.setStatus(HTTPStatus.OK)
        message.setMessage("success")
        message.setData(result)
        return message.__dict__, message.statusCode, {'ContentType': 'application/json'}
