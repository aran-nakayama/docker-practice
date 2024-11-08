from flask import Flask

app = Flask(__name__)

# ヘルスチェックエンドポイント
@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

if __name__ == "__main__":
    # アプリケーションをポート8080で実行
    app.run(host="0.0.0.0", port=8080)
