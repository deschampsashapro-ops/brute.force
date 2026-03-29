import requests

API_KEY = "461E8C52F6DF43EB1FBE24F3219443EB"
STEAM_ID = "76561198108535861"

def get_cs2_stats(api_key, steam_id):
    url = "https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/"
    
    params = {
        "appid": 730,  
        "key": api_key,
        "steamid": steam_id
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data

stats = get_cs2_stats(API_KEY, STEAM_ID)

print(stats)

def extract_main_stats(data):
    stats_list = data["playerstats"]["stats"]

    stats_dict = {stat["name"]: stat["value"] for stat in stats_list}

    kills = stats_dict.get("total_kills", 0)
    deaths = stats_dict.get("total_deaths", 1)
    headshots = stats_dict.get("total_kills_headshot", 0)

    kd = round(kills / deaths, 2)
    hs_percent = round((headshots / kills) * 100, 2) if kills > 0 else 0

    return kills, deaths, kd, hs_percent

kills, deaths, kd, hs = extract_main_stats(stats)

print("Kills:", kills)
print("Deaths:", deaths)
print("K/D:", kd)
print("HS%:", hs)