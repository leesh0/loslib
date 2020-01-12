# LOS LIB

this script is for LoS Challenge

![](https://tva1.sinaimg.cn/large/006tNbRwgy1gatqc2yecwj30rs0c8q3g.jpg)





## 빠른시작

```python
from loslib import *

sql = loslib(id=yourID,pw=yourPW)
sql.send(id="",pw="' or 1=1 %23") #paramName=""
```



## 1. Use

```python
from loslib import *
```



## 2. Login

```python
example = los(id=yourid,pw=yourpw)
```

Success:

```powershell
                                                
            __    _____ _____    __    _ _     
            |  |  |     |   __|  |  |  |_| |_   
            |  |__|  |  |__   |  |  |__| | . |_ 
            |_____|_____|_____|  |_____|_|___|_|
                                                
        
id:(lalaport) login success!
your level : banshee	#현재 풀어야할 문제
```

Fail:

```powershell
                                                
            __    _____ _____    __    _ _     
            |  |  |     |   __|  |  |  |_| |_   
            |  |__|  |  |__   |  |  |__| | . |_ 
            |_____|_____|_____|  |_____|_|___|_|
                                                
        
LOGIN FAIL
```



## send()

```python
loslib.send(praramName="param1") #ex: id="' or 1=1 %23"
```

`send` 함수로 request get기능이 완수되며 아래의 변수들에 값이 들어감

- `loslib.res` : responsed data
- `loslib.ans` : 클리어, 혹은 Hello문자열이 나오는 부분 파싱 (h2)
- `loslib.query` : 보내지는 query부분 파싱
- `loslib.html` : response된 html태그
- `loslib.shtml` : response된 html태그를 BeatifulSoup으로 변환된 데이터 리턴



## Start & end

```python
loslib.start()
loslib.end()
```

sleep()을 이용한 blind sqli에 사용. start()함수가 시작된 지점으로부터 end()지점까지 걸린 시간을 `ms` 단위로 `loslib.runtime` 변수에 입력



## setProb()

```python
loslib.setProb("gremlin")
```

loslib에서는 자동으로 현재 풀지 못한 최상위 문제로 지정되므로 다른문제를 풀고싶은 경우 직접 문제명으로 문제를 지정한뒤 문제를 풀 수 있다.



## Print

- `perror` : 빨간글씨출력
- `psuccess` : 녹색글씨 출력
- `pwarning` : 노란글씨 출력
- `pblue` : 파란글씨 출력
- `load` : loading bar혹은 반복되는 문장(blind sql)을 출력할 때 사용하면 깔끔하게 출력가능(출력시 개행이 아닌 지워졌다가 다시 해당위치에 출력)
- `log` : log출력



## Encoder

- `hex(string)` : 문자열을 hex로 변환 (ex. AAAA ☞ 0x41414141)
- `unhex(hex)` : hex로 변환된 문자열을 다시 string으로 변환
- `urlencode(string)` : string을 url encoding