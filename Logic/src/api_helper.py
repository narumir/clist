import requests
import os
from datetime import date
import json
from enum import Enum

class EWeather(Enum):
    spring = 0
    summer = 1
    fall = 2
    winter = 3

class Position:
    def __init__(self, nx: int, ny: int): 
        self.nx = nx
        self.ny = ny

# register locations by nx, ny here
g_position_map = {
    "seoul": Position(60, 120),
    "default": Position(60, 120),
}

WEATHER_SECRET = os.environ["WEATHER_SECRET"]

HASURA_ENDPOINT = "https://fmowl.narumir.io/v1/graphql"
HASURA_SECRET = os.environ["HASURA_SECRET"]
USER_CLOSET_QUERY = '''
    query MyQuery {
    closet(where: {user_id: {_eq: "%s"}, season: {_eq: "%s"}}) {
    clothes_id
    color
    is_upper
  }
}''' 

class EUpperolor(Enum):
    navy = 0
    green = 1
    yellow = 2
    blue = 3
    beige = 4
    red = 5

class ELowerColor(Enum): 
    light_blue = 0
    dark_blue = 1
    black = 2
    beige = 3
    cream = 4
    khaki = 5
# 색 조합표에서 쌍 동그라미, 동그라미만 채택
g_color_match_map = {
    EUpperolor.navy.name: { 
        ELowerColor.light_blue.name, 
        ELowerColor.black.name, 
        ELowerColor.beige.name, 
        ELowerColor.cream.name, 
        ELowerColor.khaki.name 
    }, 
    EUpperolor.green.name: { 
        ELowerColor.light_blue.name, 
        ELowerColor.dark_blue.name,
        ELowerColor.black.name, 
        ELowerColor.beige.name 
    }, 
    EUpperolor.yellow.name: { 
        ELowerColor.dark_blue.name,
        ELowerColor.black.name, 
        ELowerColor.beige.name, 
        ELowerColor.khaki.name
    }, 
    EUpperolor.blue.name: { 
        ELowerColor.light_blue.name,
        ELowerColor.dark_blue.name,
        ELowerColor.black.name
    }, 
    EUpperolor.beige.name: { 
        ELowerColor.light_blue.name,
        ELowerColor.dark_blue.name,
        ELowerColor.black.name, 
        ELowerColor.cream.name,
        ELowerColor.khaki.name
    }, 
    EUpperolor.red.name: { 
        ELowerColor.light_blue.name,
        ELowerColor.black.name, 
        ELowerColor.beige.name,
        ELowerColor.cream.name
    }, 
}

class UpperCloth: 
    def __init__(self, id: int, color: EUpperolor):
        self.id = id
        self.color = color

class LowerCloth: 
    def __init__(self, id: int, color: ELowerColor):
        self.id = id
        self.color = color
        
class MatchedClothes: 
    def __init__(self, upper: UpperCloth, lower: LowerCloth):
        self.upper = upper
        self.lower = lower

def get_weather_by_location(location: str) -> EWeather:
    position : Position = None
    if location in g_position_map:
        position = g_position_map[location]
    else:
        position = g_position_map["default"]

    # call wheather API
    today = date.today()
    serviceKey = WEATHER_SECRET
    pageNo = "1"
    numOfRows = "10"
    dataType = "JSON"
    baseDate = today.strftime("%Y%m%d")
    baseTime = today.strftime("%H%M")
    nx = position.nx
    ny = position.ny
    url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={serviceKey}&pageNo={pageNo}&numOfRows={numOfRows}&dataType={dataType}&base_date={baseDate}&base_time={baseTime}&nx={nx}&ny={ny}"

    try: 
        res = requests.get(url=url, timeout=3)
    except requests.exceptions.Timeout:     # 타임아웃 발생 시, 그냥 월별로 계절을 구분해버린다. 
        m = today.month
        if m in [3, 4, 5]:
            return EWeather.spring
        elif m in [6, 7, 8]: 
            return EWeather.summer
        elif m in [9, 10, 11]: 
            return EWeather.fall
        elif m in [12, 1, 2]: 
            return EWeather.winter

    # 타임아웃 발생하지 않은 경우
    json_res = json.loads(res.text)

    temperature = 0.0
    items = json_res["response"]["body"]["items"]["item"]
    for item in items:
        if item["category"] == "T1H":
            temperature = float(item["obsrValue"])

    if temperature <= 0.0:  
        return EWeather.winter
    elif temperature <= 10:
        return EWeather.fall
    elif temperature <= 20:
        return EWeather.spring
    else:
        return EWeather.summer

def get_user_closet(user_id: str, weather: EWeather):
    # print(f"user_closet: {user_id} weather: {weather.name}", end="\n")

    headers = { "content-type": "application/json", "x-hasura-admin-secret": HASURA_SECRET }
    json_param = { "query": USER_CLOSET_QUERY % ( user_id, weather.name )}

    res_str = requests.post(HASURA_ENDPOINT, headers=headers, json=json_param)

    print(res_str.text, end="\n")

    res_json = json.loads(res_str.text)

    return res_json["data"]["closet"]
