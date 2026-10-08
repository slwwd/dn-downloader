import requests
import re

def get_tt(url):
    print("-> connecting to tikwm...")
    api = f"https://tikwm.com{url}"
    
    try:
        res = requests.get(api).json()
        if res.get("code") == 0:
            clean_title = re.sub(r'[\\/*?:"<>|]', "", res["data"]["title"][:15]) or "video"
            print(f"-> fetching: {clean_title}...")
            
            vid = requests.get(res["data"]["play"]).content
            with open(f"{clean_title}.mp4", "wb") as f:
                f.write(vid)
            print("-> done. check folder.")
        else:
            print("-> error: bad link or private video")
    except Exception as e:
        print(f"-> crash: {e}")

if __name__ == "__main__":
    link = input("url: ")
    get_tt(link)
