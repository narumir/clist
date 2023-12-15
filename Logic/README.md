### FastAPI 설치
```
pip install fastapi
pip install uvicorn
```

### HTTP 통신 위한 requests 설치
```
pip install requests
```

### JWT 라이브러리
```
pip install pyjwt
```

### 환경변수
* WEATHER_SECRET  
* HASURA_SECRET  
* JWT_SECRET  
* JWT_ALOG

### 날씨 API
신청 링크: https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15084084


### 서버 실행
```
uvicorn main:app --reload --port=8080
```