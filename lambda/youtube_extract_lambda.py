import json
import boto3
import os
from datetime import datetime
from urllib.request import urlopen
from urllib.parse import urlencode

s3 = boto3.client("s3")

def lambda_handler(event, context):
    api_key = os.environ["YOUTUBE_API_KEY"]
    channel_id = os.environ["CHANNEL_ID"]
    bucket = os.environ["RAW_BUCKET"]

    # ---- Search API (get latest video IDs) ----
    search_params = {
        "key": api_key,
        "channelId": channel_id,
        "part": "id",
        "order": "date",
        "maxResults": 10
    }

    search_url = "https://www.googleapis.com/youtube/v3/search?" + urlencode(search_params)
    search_response = json.loads(urlopen(search_url).read())

    video_ids = [
        item["id"]["videoId"]
        for item in search_response.get("items", [])
        if item["id"]["kind"] == "youtube#video"
    ]

    # ---- Videos API (get stats) ----
    video_params = {
        "key": api_key,
        "id": ",".join(video_ids),
        "part": "snippet,statistics"
    }

    video_url = "https://www.googleapis.com/youtube/v3/videos?" + urlencode(video_params)
    video_response = json.loads(urlopen(video_url).read())

    file_name = f"raw_data/youtube_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

    s3.put_object(
        Bucket=bucket,
        Key=file_name,
        Body=json.dumps(video_response)
    )

    return {
        "status": "success",
        "records": len(video_response.get("items", []))
    }
