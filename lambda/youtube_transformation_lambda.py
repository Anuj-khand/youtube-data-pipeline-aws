import json
import boto3
import os

s3 = boto3.client("s3")

DEST_BUCKET = "youtube-transformed-anuj"
DEST_PREFIX = "processed_data/"

def lambda_handler(event, context):
    src_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    src_key = event["Records"][0]["s3"]["object"]["key"]

    response = s3.get_object(Bucket=src_bucket, Key=src_key)
    data = json.loads(response["Body"].read())

    records = []
    for item in data.get("items", []):
        records.append({
            "video_id": item["id"],
            "title": item["snippet"]["title"],
            "published_at": item["snippet"]["publishedAt"],
            "view_count": int(item["statistics"].get("viewCount", 0)),
            "like_count": int(item["statistics"].get("likeCount", 0)),
            "comment_count": int(item["statistics"].get("commentCount", 0))
        })

    output_key = DEST_PREFIX + src_key.split("/")[-1]

    s3.put_object(
        Bucket=DEST_BUCKET,
        Key=output_key,
        Body=json.dumps(records)
    )

    return {
        "status": "processed",
        "records": len(records)
    }
