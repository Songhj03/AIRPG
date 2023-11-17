from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 사용자가 입력한 텍스트를 받아 AI의 답변을 생성하는 코드를 여기에 작성합니다.
        pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)