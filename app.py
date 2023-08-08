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

    # ----start----[시험에서 추가된 부분]
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_list) + 1
    # ----end----[시험에서 추가된 부분]

    print(bucket_receive)
    # [POST-2] 클라이언트로부터 받은 데이터를 DB에 넣자 MongoDB연결을 위한 임포트부터 시작(더블체크)
    # [POST-5] DB연결이 완료되었으니 Dictionary key:value형태 데이터들을 doc=리스트 객체에 담는다.
    # INSERT_ONE
    # 저장 - 예시
    # doc = {'name':'bobby','age':21}
    doc = {
    # ----start----[시험에서 추가된 부분]
        'num':count,  #버킷 등록 시, db에서 특정 버킷을 찾기 위해 'num' 이라는 고유 값 부여
        'done' : 0,   #'done' key값을 추가 해 각 버킷의 완료 상태 구분(0 = 미완료, 1 = 완료)
    # ----end----[시험에서 추가된 부분]
        'bucket' : bucket_receive
    }
    # [POST-6] doc에 담았으니 DB에 insert 한다.
    db.bucket.insert_one(doc)
    # [POST-7] insert가 완료되었으니 완료 메시지를 반환한다.
    return jsonify({'msg': 'POST 연결 완료!'+'DB 저장 완료!'})
    
# ----start----[시험에서 추가된 부분]
# 등록한 버킷을 ‘완료’ 상태로 바꾸는 기능을 만들어 주세요
# - 이미지 참고 (▶️ 버튼을 눌러주세요)
#    1. 등록한 버킷을 ‘완료’ 상태로 바꾸는 기능을 만들어 주세요. 등록한 버킷의 우측에 ‘완료’ 버튼을 생성하고, 버튼을 클릭 시 버킷 문구 뒤에 ‘완료!!’ 가 추가되면 완성입니다!
#        - [완료!] 버튼 클릭 시 → [완료!!] 텍스트 생기도록 하기
# 추가된 업데이트문
@app.route("/update", methods=["POST"])
def bucket_update():
    num_receive = request.form['num_give']
    print(num_receive)
    #해당글 찾아서
    find_content_filter = {'num': int(num_receive)}
    #업데이트 할 부분 key부분 set
    update = {'$set': {'done': 1}}

    # [POST-6] doc에 담았으니 DB에 update 한다.
    db.bucket.update_one(find_content_filter, update)
    # [POST-7] update 완료되었으니 완료 메시지를 반환한다.
    return jsonify({'msg': 'POST 연결 완료!'+'DB UPDATE 완료!'})

# 수정을 또 복구하는 업데이트문
@app.route("/restore", methods=["POST"])
def restore_post():
    num_receive = request.form['num_give']
    find_content_filter = {'num': int(num_receive)}
    update = {'$set': {'done': 0}}  # done 값을 0으로 업데이트

    db.bucket.update_one(find_content_filter, update)
    return jsonify({'msg': '복구 완료!'})
# ----end----[시험에서 추가된 부분]

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


