import requests
from urllib.parse import urlparse, parse_qs

def create_playlist(url, headers):
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        data = response.json()
        tab_code = parse_qs(urlparse(url).query).get('tab_code', ['ALL'])[0]
        playlist = ""
        for channel in data['response'].get('channels', []):
            if channel.get('streamType') == 'live':
                stream_url = f"https://neptv.guruusr.workers.dev/yupp/{channel['code']}/playlist.m3u8"
                playlist += f"#EXTINF:-1 tvg-id=\"{channel['code']}\" tvg-name=\"{channel['name']}\" tvg-logo=\"{channel['logo']}\" tvg-language=\"{channel['language']}\" group-title=\"{tab_code}\",{channel['name']}\n{stream_url}\n"
        return playlist
    except Exception as e:
        print(f"Error processing playlist for {url}: {e}")
        return ""

def save_playlist(playlist, filename='yupptv_fta.m3u8'):
    with open(filename, 'a') as f:
        f.write(playlist)

if __name__ == "__main__":
    categories = ["Spiritual", "NEWS", "Education", "MOV", "ENT", "MUS", "SPO", "Life", "Live", "BUSNEWS", "OTH"]
    base_url = "https://prodapi.yupptv.com/yupptv/api/v2/tvguide/channels?directed_from=freetv&tab_code={}&skip_tabs=true&skip_genres=true&languages=HIN%2CTEL%2CTAM%2CMAL%2CKAN%2CBEN%2CMAR%2CPUN%2CENG%2CGUJ%2CORI%2CBAN%2CNEP%2CBHOJ%2CURD%2CSIN%2CARA%2COTH"
    headers = {
        "user-agent": "okhttp/4.9.2",
        "box-id": "f17dc321839161b2", //this is temp
        "session-id": "YT-69f0c9f6-f998-4ac7-a4c7-00530e815aeb" //this is temp
    }
    playlist = "#EXTM3U\n"
    for category in categories:
        url = base_url.format(category)
        playlist_data = create_playlist(url, headers)
        if playlist_data:
            playlist += playlist_data
    save_playlist(playlist)
    print("Playlist created successfully!")
