import json
import os
import sys

import httpx
from dotenv import load_dotenv

load_dotenv()
KEY = os.environ["RIOT_API_KEY"]

match_id = sys.argv[1]
headers = {"X-Riot-Token": KEY}
base = "https://americas.api.riotgames.com/lol/match/v5/matches"

match = httpx.get(f"{base}/{match_id}", headers = headers).json()
timeline = httpx.get(f"{base}/{match_id}/timeline", headers = headers).json()

os.makedirs("data/raw", exist_ok = True)
with open(f"data/raw/{match_id}.json", "w") as f:
    json.dump(match, f)
with open(f"data/raw/{match_id}_timeline.json", "w") as f:
    json.dump(timeline, f)

print("Saved", match_id, "-", len(timeline["info"]["frames"]), "frames")
