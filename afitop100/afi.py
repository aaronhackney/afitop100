import requests
from bs4 import BeautifulSoup
from .film import Film
from .common import wikipedia

import json


class AFITop100:
    """Class to obtain the AFI Top 100 Films of all time"""

    def __init__(self, **kwargs):
        self.wikipedia = wikipedia.Wikipedia()
        self.afi_list = list()

    def get_afi_list_by_year(self, year: int) -> list:
        """
        Given a valid list year, Return a list of Films objects sorted by AFI Ranking (Ascending)
        Valid list years as of Jan 2021 are 1998 and 2007
        """
        afi_list_by_year = list()
        for film in self.afi_list:
            if film[f"afi_rank_{year}"] is not None:
                afi_list_by_year.append(film)
        return sorted(afi_list_by_year, key=lambda k: k[f"afi_rank_{year}"])

    def scrape_afi_list(self, wiki_title="AFI's_100_Years...100_Movies", section="2") -> None:
        """
        Screen scrape the AFI top 100 list from the wikipedia page and store the data in this class instance
        """
        wiki_json = self.wikipedia.get_wikipedia_page(wiki_title, section=section)
        soup = BeautifulSoup(wiki_json["parse"]["text"], "html.parser")
        table = soup.find("table", attrs={"class": "wikitable"})
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            if len(cells) == 6:
                self.afi_list.append(
                    Film(
                        cells[0].text.strip(),  # film title
                        int(cells[1].text.strip()),  # year will always be an integer
                        cells[2].text.strip(),  # director's name
                        cells[3].text.strip(),  # 1998 rank might be a '-' and not an integer so pass as a str
                        cells[4].text.strip(),  # 2007 rank might be a '-' and not an integer so pass as a str
                    )
                )

    def get_rank_movement(self, film, afi_year_1=1998, afi_year_2=2007) -> int or None:
        """Return the rank delta from year to year"""
        year_1 = getattr(film, f"afi_rank_{afi_year_1}")
        year_2 = getattr(film, f"afi_rank_{afi_year_2}")
        if year_1 is not None and year_2 is not None:
            return year_1 - year_2

    def get_film_by_title(self, film: str) -> Film:
        """Return a film object when searching for a fiulm by name (Case insensitive)"""
        for film_obj in self.afi_list:
            if film_obj.title.lower() == film.lower():
                return film_obj

    def get_afi_list_json(self) -> str:
        """Return a json string representation of the AFI TOP 100 list"""
        return json.dumps([film.__dict__ for film in self.afi_list])