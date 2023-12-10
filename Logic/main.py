from fastapi import FastAPI
import requests
import os
import json
import jwt
from data_model import RecommandRequest
from fastapi import FastAPI, HTTPException
from jwt.exceptions import InvalidTokenError
from api_helper import get_weather_by_location, get_user_closet, g_color_match_map, UpperCloth, LowerCloth, MatchedClothes
from typing import List
import random

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALOG = os.getenv("JWT_ALOG")

app = FastAPI()

@app.get("/")
async def root():
    return { "msg": "logic_root" }

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

USER_CLOSET_QUERY = '''query MyQuery {
  closet(where: {user_id: {_eq: "user_id"}, season: {_eq: "season"}}) {
    clothes_id
    color
    is_upper
  }
}'''

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

@app.post("/recommand")
async def recommand(request: RecommandRequest):
    key = "test_key"
    algo = "HS256"
    if False:
        key = JWT_SECRET
        algo = JWT_ALOG


    try:
        decoded = jwt.decode(request.token, key=key, algorithms=algo)

        location = decoded["location"]
        claims = decoded["https://hasura.io/jwt/claims"]
        user_id = claims["x-hasura-user-id"]

        weather = get_weather_by_location(location)
        closet = get_user_closet(user_id, weather)

        upper_clothes : List[UpperCloth] = []
        lower_clothes : List[LowerCloth] = []

        for cloth in closet: 
            if cloth["is_upper"]:
                upper = UpperCloth(cloth["clothes_id"], cloth["color"])
                upper_clothes.append(upper)
            else:
                lower = LowerCloth(cloth["clothes_id"], cloth["color"])
                lower_clothes.append(lower)

        matched_clothes_list : List[MatchedClothes] = []
        for upper in upper_clothes:
            lower_map = g_color_match_map[upper.color]
            for lower in lower_clothes:
                if lower.color in lower_map:
                    matched_clothes_list.append(MatchedClothes(upper, lower))
        
        if len(matched_clothes_list) == 0:
            return { HTTPException(status_code=404, detail="no match found") }
        else:   # select random from matched list
            selected = random.choice(matched_clothes_list)
            
            return { "upper_id": selected.upper.id, "lower_id":selected.lower.id }

    except InvalidTokenError: 
        raise HTTPException(status_code=400, detail="Invalid Token")
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Invalid Key: {e}")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"Exception: {e}")
