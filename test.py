# Flask 모듈을 가져옵니다.
from flask import Flask

# Flask 앱 객체를 생성합니다.
app = Flask(__name__)

# 루트 경로('/')에 대한 뷰 함수를 정의합니다.
# GET 요청을 받으면 'Hello, World!'라는 문자열을 반환합니다.
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 직접 실행된 경우에만 아래의 코드를 실행합니다.
if __name__ == '__main__':
    # Flask 앱을 실행합니다.
    # 모든 IP 주소에서 접근 가능하도록 설정하고 포트 5000을 사용합니다.
    app.run(host='0.0.0.0', port=5000)
