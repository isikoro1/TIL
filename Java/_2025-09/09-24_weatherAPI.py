import requests
cities = ["tokyo", "osaka", "kyoto", "okinawa"]

for city in cities:
    url = f"http://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        print(response.text)
    except Exception as e:
        print(f"{city}: エラーが発生しました({e})")