from afitop100 import AFITop100

"""
Get the AFI Top 100 List data in json format
"""
afi = AFITop100()  # instance of the AFITop100 Client

afi.scrape_afi_list()  # scrape the AFI Top 100 from Wikipedia

print(afi.get_afi_list_json())  # pretty print the list