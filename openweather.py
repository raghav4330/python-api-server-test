import requests, uvicorn
from fastapi import FastAPI


appppp = FastAPI()

@appppp.get("/")
def root():
    """ root """
    return "Welcome Babes"

@appppp.get("/test_weather")
def test_weather():
	url = "https://open-weather13.p.rapidapi.com/fivedaysforcast"

	querystring = {"latitude":"40.730610","longitude":"-73.935242","lang":"EN"}

	headers = {
		"x-rapidapi-key": "51903dcc2dmshe6a6b61ace3acbfp1ac3d4jsnd50cffa48849",
		"x-rapidapi-host": "open-weather13.p.rapidapi.com",
		"Content-Type": "application/json"
	}

	response = requests.get(url, headers=headers, params=querystring)

	print(response.json())
	return response.json()
 
if __name__ == "__main__":
    print("Inside")
    uvicorn.run("openweather:appppp", host = "0.0.0.0", port = 9321) # filename: fastAPI instance name
    
    # Global practice is to name main file as "app" and instance also as app, hence making it below - 
    # uvicorn.run("app:app", host = "0.0.0.0", port = 9321)
