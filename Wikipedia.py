import requests
from lxml import html 
encabezdo ={
    "user-agent":"Mozilla/5.0 (x11;Linux x86_64) AppleWebkit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Safari/537.36",
    
}
url = "https://www.wikipedia.org/"

respuesta = requests.get(url, headers=encabezdo)

parser = html.fromstring(respuesta.text)

#espanol = parser.get_element_by_id("js-link-box-es")
#print(espanol.text_content())

#espanol = parser.xpath("//a[@id='js-link-box-es']/strong/text()")
#print(espanol)

idiomas = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")

for idioma in idiomas:
    print(idioma)