import requests
import sys
from tld import get_tld
from bs4 import BeautifulSoup
from filter import filter

# Given a page URL, we first get the entire HTML code of the page and begin
# scraping the page to find all the other URLs that are on it.
def get_page_urls(page_url):
    my_timeout = 30
    url = ""
    code = ""
    cert = True
    all_urls = []
    all_urls.append(page_url)
    try:
        code = requests.get(page_url, timeout=my_timeout)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        cert = False
        print("Invalid certificate OR Timeout: {}".format(page_url))

    if cert:
        plain = code.text
        s = BeautifulSoup(plain, "html5lib")
        if s.findAll("a"):
            for link in s.findAll("a"):
                url = str(link.get("href"))
                if url != '':
                    if url[0] == '/':
                        url = page_url + url[1:]
                if not url.find("https") or not url.find("http"):
                    if (not url in all_urls):
                        all_urls.append(url)
    return all_urls

# Given a list of all the scraped URLs, we remove all URLs that are not of the
# same domain name.
def get_internal_urls(all_urls, main_url):
    internal_urls = []
    domain = get_tld(main_url, as_object=True).parsed_url[1]

    for url in all_urls:
        if get_tld(url, as_object=True).parsed_url[1] == domain:
            internal_urls.append(url)

    return internal_urls

# Function that saved the list of scraped URLs to a file.
def save_urls(urls):
    site_name = get_tld(urls[0], as_object=True).domain

    f = open("Output.txt", "a")
    f.write("#{}\n".format(site_name))
    for url in urls:
        f.write(url)
        f.write("\n")
    f.close()

# Function that reads from a given file.
def read_file(filename):
    f = open(filename, "r")
    return f.readlines()

# Main function
if __name__ == '__main__':
    domain_list_filename = sys.argv[1]
    domain_list = read_file(domain_list_filename)
    for domain in domain_list:
        domain = domain[:-1]
        if domain != "":
            if domain[len(domain) - 1] != '/':
                domain += '/'

            all_urls = get_page_urls(domain)
            if all_urls:
                internal_urls = get_internal_urls(all_urls, domain)
                if internal_urls or len(internal_urls) == 1:
                    save_urls(internal_urls)
                    print("Done: {}\n".format(domain))
                else:
                    print("Skipped {}\n".format(domain))


    filter("Output.txt")
    print("Success!")
