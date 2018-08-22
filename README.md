## Web Crawler

This repository contains the source-code of a web crawler developed to extract informations of products available to sell in the Mercado Livre platform. 

I used Scrapy to do the crawling tasks and the results obtained was stored as csv files. This data needs to be, first, cleanned and then, we can apply 
some interesting techniques to observe/analyse that data, like:
- Price monitor (detect changes occurred in the price of a specified item)
- Apply clustering techniques to find similar itens (so we can compare prices)
- Some geographic analysis, because we have the location of the seller
- Etc.
