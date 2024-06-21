import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"] ["username"]
        country = user_data["location"] ["country"]
        return user_name, country
    else:
        raise Exception("Faild to fetch userdata")
    

def main():
    try:
        username, country = fectch_random_user_freeapi()
        print(f"username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))
       
if __name__ == "__main__":
    main()
