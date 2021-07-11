import pandas
from GetSoup import get_soup
from Busca import search  

def format_text(element):
    text = element.text.title()
    return text

events = {}
titles = []
dates = []


url = "https://pt.wikipedia.org/wiki/Jo%C3%A3o_Pessoa"

soup = get_soup(url)
found_titles = search(soup,"span", "class", "titulo-pagina") 
found_dates  = search(soup,"div", "class", "data-publicacao")