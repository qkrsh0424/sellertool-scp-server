from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource
from flask_cors import CORS

from domain.hello.controller.HelloApi import HelloApi  # Api 구현을 위한 Api 객체 import
from domain.n_rank.controller.NRankApi import NRankApi

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록

cors = CORS(
    app, 
    origins=[
        "http://localhost:3000",
        "http://www.sellertl.com", 
        "https://www.sellertl.com",
        "http://www.sellertool.io",
        "https://www.sellertool.io",
    ], 
    headers=['Content-Type'], 
    expose_headers=['Access-Control-Allow-Origin'], 
    supports_credentials=True
)

api.add_namespace(HelloApi, "/scp/v1/hello")
api.add_namespace(NRankApi, '/scp/v1/n-rank')

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8082)

# waitress WSGI Start
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="127.0.0.1", port=8082)