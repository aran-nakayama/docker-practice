# 最新のPython 3.12のスリムイメージを使用
FROM python:3.12-slim

# Flaskをインストール
RUN pip install flask

# 作業ディレクトリの設定
WORKDIR /app

# アプリケーションコードをコンテナにコピー
COPY app.py /app/app.py

# ポート8080を公開
EXPOSE 8080

# ヘルスチェックの設定 (podmanだとサポートされてないらしい？ エンドポイントは動く)
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# アプリケーションの実行
CMD ["python", "app.py"]
