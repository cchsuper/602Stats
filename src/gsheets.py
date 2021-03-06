import json
import requests
import settings

def getRacers():
    success=False
    tries = 0
    sheetRacers = []
    with open('settings.json','r') as f:
        j = json.load(f)
        api_key = j['google-api-key']
    url = settings.gsheet + api_key

    while not success:
        response = requests.get(url, headers={})
        tries+=1
        if response.status_code in range(200,300):
            nResponse = json.loads(response.content.decode("UTF-8"))["values"]
            for e in nResponse:
                if e == []:
                    pass
                elif e[0] == "Theoretical WR":
                    pass
                else:
                    sheetRacers.append(e[0])
            success=True
        else:
            nResponse = json.loads(response.content.decode("UTF-8"))["error"]
            print('[!] (Try '+str(tries)+') Google Sheets API request failed. ' + str(nResponse["code"]) +': '+nResponse["message"])
            if tries==5:
                print("[!] Can't request from Google Sheets API. Giving up.")
                success=True
    return sheetRacers
