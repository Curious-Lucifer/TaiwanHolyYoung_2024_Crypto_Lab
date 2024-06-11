# Taiwan Holy Young - Crypto Lab

## Deploy Challenge To CTFd
> 需要 install [CTFdTools](https://github.com/Curious-Lucifer/CTFdTools) 到 `sys.path` 上

寫一個 `.env` 開頭的檔案放在跟 `ctfd.py` 同一個資料夾

```
BASE_URL='http://.../'
TOKEN='...'
SERVER='...'
```

其中 `BASE_URL` 是 CTFd 首頁的連結，`TOKEN` 是 CTFd token，`SERVER` 是打算 deploy challenge 的機器 IP 或 Domain

如果不想要改 `ctfd.py` 的話，那前面的設定檔檔名就叫 `.env.dev`，如果不是用這個黨名的話要把第 9 行改掉

接著執行

```shell
./ctfd.py
```

就可以把題目 deploy 到 CTFd 了


---
## Deploy Challenge
> 需要 install Docker 且有執行 `docker` 的權限

開啟 challenge

```shell
./deploy.py start
```

關閉 challenge

```shell
./deploy.py stop
```

