from trendsapi_steam import TrendsAPI

client = TrendsAPI()                    # TRENDSAPI_KEY
# client = TrendsAPI(api_key="YOUR_KEY")

series = client.get_time_series("counter-strike 2")
print(series[-1].date, series[-1].value)

growth = client.get_growth("counter-strike 2", percent_growth=["3M", "12M"])
print(growth.results[0].growth, growth.results[0].direction)

hot = client.get_live(limit=10)
print(hot.data)                         # [[1, "..."], ...]
