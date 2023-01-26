import requests
import shutil
from os.path import join, isdir
from os import listdir, mkdir
from time import sleep

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning) # type: ignore

session = requests.Session()
session.verify = False

if not(isdir('cats')): mkdir('cats')

CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

for i in range(100):
    cat_number = len(listdir('cats'))+1
    sleep(1)
    cat = session.get(CAT_API_URL).json()[0]
    url: str = cat['url']
    extension = url.split('.')[-1]
    picture = session.get(url, stream=True).raw
    with open(join('cats',f'cat_{cat_number}.{extension}'), 'wb') as f:
        shutil.copyfileobj(picture, f)