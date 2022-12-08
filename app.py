import requests

api_key = ""
with open("apikey.txt", "r") as file:
    # Read the first line of the file
    api_key = file.readline()
url = input("Please input URL to be checked: ")


#def microsoft_ss_check(url):
#    # Set the URL and headers for the request
#    api_url = "https://nav.smartscreen.microsoft.com/windows/browser/edge/service/navigate/4/sync"
#    headers = {
#        "Content-Type": "application/json",
#        "X-Request-ID": "your-request-id",
#        "User-Agent": "phishblade",
#    }
#    request_body = {
#        "destination":  {
#            "ip": None,
#            "uri": url
#        }
#    }
#
#    # Make the request and get the response
#    response = requests.post(api_url, headers=headers, json=request_body)
#    print(response.status_code)



def google_sb_check(url, api_key):
    # Set the URL and headers for the request
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"
    headers = {"Content-Type": "application/json"}
    # Set the request body with the URL to check and the API key
    request_body = {
        "client": {"clientId": "your-client-id", "clientVersion": "1.0.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }
    # Make the request and get the response
    response = requests.post(api_url, headers=headers, json=request_body)
    response_json = response.json()
    if "matches" in response_json:
        return True
    else:
        return False


# Use the function to check the safety of a URL
print(google_sb_check(url, api_key))
#print(microsoft_ss_check(url))
