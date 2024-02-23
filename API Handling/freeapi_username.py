import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    res = response.json()

    
    if res["success"] and "data" in res:
        userData = res["data"]
        userName = userData["login"]["username"]
        country = userData["location"]["country"]
        return userName, country
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        userName, country = fetch_random_user_freeapi()
        print(f"UserName : {userName} \nCountry : {country}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()