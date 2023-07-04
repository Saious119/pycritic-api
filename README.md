# pycritic-api

This is a simple Flask API to wrap the pycritic scrapper in

## How to use

start up the api with ```python main.py```

The app is also hosted with vercel at https://pycritic-api.vercel.app

make requests with your app or api tester (I use Insomnia) and hit an endpoint!

options are:

- ```/game/<platform>/<name>```
  
- ```/game/metaurl/<url>```

This API will return a json string with properties: name, release date, category, metacritic score, user score, and description

## Requirements

- python 3.9 or higher
- Flask (pip install flask)
- urllib (pip install urllib)
- json (pip install json)
- requests (pip install requests)
- beautiful soup 4 (pip install bs4)

## Pycritic
to see the pycritic project go here https://github.com/saious119/pycritic 
