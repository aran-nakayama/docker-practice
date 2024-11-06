# Flask Health Check App

このプロジェクトは、Flaskで作成したシンプルなヘルスチェックアプリケーションです。コンテナ化されており、Podmanで簡単にビルドと実行ができます。

## ファイル構成

- `app.py`: Flaskアプリケーション本体。`/health` エンドポイントでヘルスチェックを提供します。
- `Dockerfile`: コンテナイメージをビルドするための設定ファイル。Flaskのインストールやアプリケーションの実行環境を設定しています。

## 必要要件

- [Podman](https://podman.io/) (Dockerでも動作しますが、このREADMEはPodmanを前提としています)
- Python 3.12以降

## セットアップと実行

1. このリポジトリをクローンしてディレクトリに移動します。

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Podmanでイメージをビルドし、コンテナを起動します。ホストのポート 8080 をコンテナのポート 8080 にマッピングします。

   ```bash
   podman build -t health-check-api .
   podman run -d -p 8080:8080 health-check-api
   ```

3. コンテナが起動したら、以下のURLにアクセスしてヘルスチェックエンドポイントを確認します。

   ```bash
   curl http://localhost:8080/health
   ```

   上記のコマンドで、`OK` というメッセージが 200 ステータスコードとともに返されれば、アプリケーションが正常に動作しています。

## コンテナの停止

実行中のコンテナを確認し、コンテナIDを指定して停止します。

```bash
podman ps        # 実行中のコンテナを表示
podman stop <コンテナID>
```

## 注意事項

- 8080 ポートが既に使用されている場合、他のポートを指定して実行してください。

## 参考

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Podman Documentation](https://podman.io/)

