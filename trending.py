from googleapiclient.discovery import build
import os

def get_trending():
    youtube = build('youtube', 'v3', developerKey=os.getenv("YOUTUBE_API_KEY"))

    request = youtube.videos().list(
        part='snippet',
        chart='mostPopular',
        regionCode='IN',
        maxResults=1
    )

    response = request.execute()
    return response['items'][0]['snippet']['title']
