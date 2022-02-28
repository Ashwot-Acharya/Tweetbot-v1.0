import requests,json
from io import StringIO
str_io_obj = StringIO()

URL ="https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw&format=txt"
respose =  requests.get(url= URL )
print(respose.text)