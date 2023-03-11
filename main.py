import requests
from colorama import Fore, Back, Style

class Browser:
  def __init__(self, url):
    self.url = url

  def load_page(self):
    r = requests.get(self.url)
    if r.status_code == 200:
      print(Fore.BLUE + "Сторінка загрузилась")
    else:
      print("Ой! Помилка...")


my_b = Browser("https://www.google.com")
my_b.load_page()