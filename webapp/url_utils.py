import requests
from turtle import *

color('purple', 'cyan')
begin_fill()
while True:
    forward(200)
    left(170)
    if (abs(pos()) < 1):
        break
end_fill()
done()

def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.request(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url
