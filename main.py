import requests
from bs4 import BeautifulSoup

base_url = "https://fbla-pbl.org"

site = requests.get(base_url)
site_soup = BeautifulSoup(site.content, "html.parser")
#print(site_soup.prettify())

class FBLA:
    def get_announcements(self):
        announcements = site_soup.select("#content > div > div > div:nth-child(5) > div.col_one_third.col_last.nobottommargin > div > div")
        #print(type(announcements))
        announcement_list = [{}]  # List of dicts
        links = announcements.find_all('a')
        for link in links:
            names = link.contents[0]
            fullLink = link.get('href')
            print(names)
            print(fullLink)

fbla = FBLA()

fbla.get_announcements()