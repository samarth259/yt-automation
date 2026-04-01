import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video(title, description):
    creds = Credentials(
        None,
        refresh_token=os.getenv("YOUTUBE_REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("YOUTUBE_CLIENT_ID"),
        client_secret=os.getenv("YOUTUBE_CLIENT_SECRET")
    )

    youtube = build('youtube', 'v3', credentials=creds)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["shorts", "viral"]
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload("output.mp4")
    )

    response = request.execute()
    print("Uploaded:", response)
