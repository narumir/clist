from fastapi import FastAPI
import requests
import os
import json
import jwt

app = FastAPI()

@app.get("/")
async def root():
    return { "msg": "auth_root" }

TEST_QUERY = '''query MyQuery {
  closet(where: {}) {
    color
    clothes_id
    is_upper
    season
    state
    user_id
  }
}
'''

@app.get("/hasura_test")
async def hasura_test():
    hasura_endpoint = "https://fmowl.narumir.io/v1/graphql"
    hasuraSecret = os.environ["HASURA_SECRET"]
    headers = { "content-type": "application/json", "x-hasura-admin-secret": hasuraSecret }
    json_param = { "query": TEST_QUERY }
    res_str = requests.post(hasura_endpoint, headers=headers, json=json_param)
    res_json = json.loads(res_str.text)

    return res_json

@app.get("/weather_test")
async def weather_test():
    res_str = ""
    if True:
      serviceKey = os.environ["WEATHER_SECRET"]
      pageNo = "1"
      numOfRows = "10"
      dataType = "JSON"
      baseDate = "20231113"
      baseTime = "0500"    # 5시
      nx = "55"
      ny = "127"
      url1 = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={serviceKey}&pageNo={pageNo}&numOfRows={numOfRows}&dataType={dataType}&base_date={baseDate}&base_time={baseTime}&nx={nx}&ny={ny}"
      res_str = requests.get(url=url1)
    else: 
      params = {
          "serviceKey": serviceKey, 
          "pageNo": pageNo, 
          "numOfRows": numOfRows,
          "dataType": dataType, 
          "base_date" : baseDate, 
          "base_time": baseTime, 
          "nx": nx, 
          "ny": ny
        }
      url2 = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
      res_str =requests.get(url2, params=params)

    res_json = json.loads(res_str.text)

    return res_json
  
@app.get("/json_test")
async def json_test():
    key = "test_key"
    jwt_payload = {"user_id": "1234-1234"}

    encoded = jwt.encode(jwt_payload, key=key, algorithm="HS256")
    decoded = jwt.decode(encoded, key=key, algorithms="HS256")

    return { "payload: ": jwt_payload, "encoded": encoded, "decoded": decoded }