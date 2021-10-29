# URL spider

## What does the URL spider do:
Given a list of domains in text format it will "click through" all of the links on the page that are specific to that domain
and saves them in two text files. One of which contains all of the URLs, `Output.txt`, and another that contains a maximum of 5 per domain, `FILTERED_Output.txt`.

- NOTE: The spider does not group the URLs into specific categories, this needs to be done manually.

## Unwanted URLs in output
If the output file contains irrelevant URLs that lead to sign up or other unwanted
pages, please feel free to add `key words` that occur in the URL to the list of words in `filter.py`,
## Format of the input domain list: eg. domain_list_travel.txt
```
http://www.caesars.com
http://www.sclv.com/
http://alamo.fr
http://www.totalrewards.com/
http://www.poferries.be/
http://www.skyparksecure.com
http://www.hotwire.com/
http://www.uniplaces.com
.
.
.
```
## Format of output file
```
#caesars
http://www.caesars.com/
#sclv
http://www.sclv.com/
http://www.sclv.com/Promotions
http://www.sclv.com/Promotions/Dining-Promotions
http://www.sclv.com/Promotions/Gaming-Promotions
http://www.sclv.com/Promotions/Hotel-Packages
#alamo
http://alamo.fr/
http://alamo.fr/usa/
http://alamo.fr/offres/
http://alamo.fr/agences/
http://alamo.fr/vehicules/us/
#totalrewards
http://www.totalrewards.com/
http://www.totalrewards.com/myrewards
http://www.totalrewards.com/myrewards/benefits-overview
http://www.totalrewards.com/myrewards/earn-and-redeem
http://www.totalrewards.com/myrewards/promotions
.
.
.
```
## How to run:
`python3 url_spider.py URL_list.txt`

## Dependencies
- pip3 install beautifulsoup4
- pip3 install tld
- filter.py
