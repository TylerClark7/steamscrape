# What?
I made a webscraper to return steams Top 100 played games at the moment.

```
[
  {
    "Counter-Strike 2": {
      "Current Player Count": "745,925",
      "Top Daily Player Count": "1,235,393"
    }
  },
  {
    "HELLDIVERS™ 2": {
      "Current Player Count": "404,735",
      "Top Daily Player Count": "458,709"
    }
  },
```

# Why?
This project combines FastAPI and Playwright to scrape a website generated with Javascript. I wanted the data to be accessible from any device. Having the ability to run this in a docker container
allows the user to run the Docker Image wherever they choose.

# How
This program scrapes data from <https://store.steampowered.com/charts/mostplayed>. 

After installing requirements.txt use 
```
uvicorn top_games.main:app --reload
```

In a browser go to
```
http://127.0.0.1:8000/top_games 
```
The full list of top 100 current steam games based off of the numbers of players will be disolayed in JSON within the browser.

## Cloud Potential
My original goal with this was to see how playwright could be used in a Dockerfile which could then be pushed to a cloud service such as AWS, GCP, or in my case Digital Ocean.

Currently I am running a different version of this in a Digital Ocean Droplet.

