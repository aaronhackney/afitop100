import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from .common.wikipedia import Wikipedia


@dataclass
class Film:
    """Class to hold film data"""

    title: str
    release_year: int
    director: str
    afi_rank_1998: str
    afi_rank_2007: str
    change: str


class AFITop100:
    """Class to obtain the AFI Top 100 Films of all time"""

    def __init__(self, **kwargs):
        self.wikipedia = Wikipedia()
        self.afi_list = list()

    def get_afi_all_time(self) -> None:
        """Get the current all time AFI Top 100 movies from wikipedia"""
        self.scrape_afi_list(self.wikipedia.get_wikipedia_page("AFI's_100_Years...100_Movies", section="2"))

    def scrape_afi_list(self, wiki_json: dict) -> None:
        """
        Screen scrape the AFI top 100 list from the wikipedia page
        """
        soup = BeautifulSoup(wiki_json["parse"]["text"], "html.parser")
        table = soup.find("table", attrs={"class": "wikitable"})
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            if len(cells) == 6:
                self.afi_list.append(
                    Film(
                        cells[0].text.strip(),
                        int(cells[1].text.strip()),
                        cells[2].text.strip(),
                        cells[3].text.strip(),
                        cells[4].text.strip(),
                        cells[5].text.strip(),
                    )
                )
