import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

import urllib.request
from bs4 import BeautifulSoup


# trends.build_payload(kw_list=["Data Science"])
# data = trends.interest_by_region()
# print(data.sample(10))



# df = data.sample(15)
# df.reset_index().plot(x="geoName", y="Data Science", figsize=(120,16), kind="bar")
# plt.show()



# data = trends.trending_searches(pn="india")
# print(data.head(10))



# keyword = trends.suggestions(keyword="Programming")
# data = pd.DataFrame(keyword)
# print(data.head())



class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()