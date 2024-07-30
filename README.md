# Taiwan Holy Young 2024 - Crypto Lab

## Deploy

### CTFd Deploy
> Requirement :
>   - CTFdTools（我自己的工具）

在和 `ctfd.py` 同一個資料夾下建立一個 `secret.py`，這個 `secret.py` 的格式如下

```py
SERVER='34.81.172.164'
CTFD='http://34.81.172.164'
USERNAME='...'
PASSWORD='...'
```

其中 `USERNAME` 和 `PASSWORD` 是管理員的 CTFd 帳號和密碼，接著執行以下指令

```shell
./ctfd.py
```

就可以把所有題目上傳到 CTFd


### Deploy Challenge
> Requirement :
>   - Python 的 `PyYaml` package
>   - Docker
>   - 執行的使用者有執行 Docker 的權限

開啟 Challenge

```shell
./deploy.py start
```

關閉 Challenge

```shell
./deploy stop
```


---
## 解答
> Requirement : 
>   - Python 的 `gmpy2` package
>   - Python 的 `Requests` package
>   - Python 的 `PyCryptodome` package

所有 challenge 資料夾底下都有一個 `sol` 資料夾，資料夾底下有 `README.md` 或 `solve.py` 解釋題目要怎麼解

