# 라이브러리 임포트
# Flask Framework
# view페이지 렌더링을 위한 render_template 메서드
# 요청 데이터에 접근 할 수 있는 flask.request 모듈
# dictionary를 json형식의 응답 데이터를 내보낼 수 있는 jsonify 메서드
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# [POST-3] MongoDB사용을 위한 pymongo와 certifi 임포트
from pymongo import MongoClient
import certifi
# [POST-4] DB 커넥션 구성
ca = certifi.where()
client = MongoClient('mongodb+srv://ohnyong:test@cluster0.lu7mz8j.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

# "localhost:5001/" URL요청에 메인 뷰 페이지 반환 응답
@app.route('/')
def home():
    return render_template('index.html')

# [POST-0] CREATE 부분부터 코드를 작성하는 것(==POST)이 확인이 가능(READ부터하면 데이터가없어서 테스트 어려움)
# fetch('URL')부분, 반환값은 res로 전달.
# "localhost:5001/bucket" URL POST방식 요청에 응답
@app.route("/bucket", methods=["POST"])
def bucket_post():
    # [POST-1] 프론트로부터 무엇을 받아야 하는가? -> 프론트 input으로부터 (html)bucket->(js)bucket_give를 받을 것이다.
    bucket_receive = request.form['bucket_give']
    print(bucket_receive)
    # [POST-2] 클라이언트로부터 받은 데이터를 DB에 넣자 MongoDB연결을 위한 임포트부터 시작(더블체크)
    # [POST-5] DB연결이 완료되었으니 Dictionary key:value형태 데이터들을 doc=리스트 객체에 담는다.
    # INSERT_ONE
    # 저장 - 예시
    # doc = {'name':'bobby','age':21}
    doc = {
        'bucket' : bucket_receive
    }
    # [POST-6] doc에 담았으니 DB에 insert 한다.
    db.bucket.insert_one(doc)
    # [POST-7] insert가 완료되었으니 완료 메시지를 반환한다.
    return jsonify({'msg': 'POST 연결 완료!'+'DB 저장 완료!'})
    
# [GET-0] CREATE 부분이 테스트 완료되어 DB에 자료가 추가되는 상황, READ로 View 페이지에 DB 데이터를 가져와서 보여주자.
# fetch('URL')부분, 반환값은 res로 전달.
# "localhost:5001/bucket" URL GET방식 요청에 응답
@app.route("/bucket", methods=["GET"])
def bucket_get():
    # [GET-1] 필요한 데이터는? -> DB에서 API 데이터를 가져와야 한다.
    all_bucket = list(db.bucket.find({},{'_id':False}))
    # [GET-2] 가져온 데이터는? -> json으로 변환하여 반환 -> 프론트(js)로 이동
    return jsonify({'result': all_bucket})

# app이라는 메인 함수 
# if __name__ == "__main__" 의 의미는 메인 함수의 선언, 시작을 의미
# 이 파이썬 스크립트가 직접 실행될 때에는 main() 함수를 실행하라
if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)