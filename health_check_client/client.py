import requests

def main():
    # APIコンテナのホスト名とポート
    url = 'http://localhost:8080/health'
    try:
        response = requests.get(url)
        print(f"ステータスコード: {response.status_code}")
        print(f"レスポンスボディ: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"リクエスト中にエラーが発生しました: {e}")

if __name__ == '__main__':
    main()
