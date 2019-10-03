import socket

# socketサーバを作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポート指定
    s.bind(('0.0.0.0', 50007))
    # 接続
    s.listen(1)
    # connectionするまで待つ
    while True:
        # アクセスがあったらコネクションとアドレスを入れる
        conn, addr = s.accept()
        with conn:
            while True:
                # データを受け取る
                data = conn.recv(1024)
                if not data:
                    break
                print('data : {}, addr: {}'.format(data, addr))
                # クライアントにデータを返す(b -> byte)
                conn.sendall(data)
