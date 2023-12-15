from main import app
import os
import requests
import json
from api_helper import get_weather_by_location

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
          "serviceKey": os.environ["WEATHER_SECRET"], 
          "pageNo": "1", 
          "numOfRows": "10",
          "dataType": "JSON", 
          "base_date" : "20231210", 
          "base_time": "1700", 
          "nx": "60", 
          "ny": "120"
        }
      url2 = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
      res_str = requests.get(url=url2, params=params)

    res_json = json.loads(res_str.text)

    return res_json

@app.get("/weather_test2")
async def weather_test2(): 
    print("weather_test2", end="\n")
    weather = get_weather_by_location("seoul")

    return { "weather": weather.name }

@app.get("/json_test")
async def json_test():
    key = "test_key"

    location = "SEOUL"
    user_id = "c025f706-820e-11ee-b962-0242ac120002"

    jwt_payload = {
        "location": location,
        "https://hasura.io/jwt/claims": {
            "x-hasura-default-role": "user",
            "x-hasura-allowed-roles": ["user", "admin"],
            "x-hasura-user-id": user_id,
        },
    }

    encoded = jwt.encode(
        jwt_payload,
        key=key,
        algorithm="HS256",
    )
    decoded = jwt.decode(encoded, key=key, algorithms="HS256")

    return { "payload: ": jwt_payload, "encoded": encoded, "decoded": decoded }