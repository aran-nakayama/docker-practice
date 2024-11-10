# 最新のPython 3.12のスリムイメージを使用
FROM python:3.12-slim

# requestsライブラリをインストール
RUN pip install requests

# 作業ディレクトリの設定
WORKDIR /app

# クライアントコードをコンテナにコピー
COPY client.py /app/client.py

# アプリケーションの実行
CMD ["python", "client.py"]
