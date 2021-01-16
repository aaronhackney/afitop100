# afitop100
## AFI Top 100

The [AFI Top 100 movies of all time](https://www.afi.com/afis-100-years-100-movies/) is a movie ranking list by the [American Film Institute](https://www.afi.com/about-afi/).  

This package will scrape the Wikipedia page that contains this listing and make the data avaialble in a structured form.  

As of the writing of this README, there are two lists avaialbe. The list published in 1998 and the list that was updated in 2007. This package will grab both of these lists and provide the following data fields from the film.py dataclass:  

- title
- release_year
- director
- afi_rank_1998
- afi_rank_2007

See the /sample directory or take a look at the unittests in /test for some examples on how to consume this data.  


*Example:*
```
from afitop100 import AFITop100
"""
Get the AFI Top 100 List data in json format
"""
afi = AFITop100()               # instance of the AFITop100 Client
afi.scrape_afi_list()           # scrape the AFI Top 100 from Wikipedia
print(afi.get_afi_list_json())  # pretty print the list
```

