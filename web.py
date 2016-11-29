import re
import sys
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import time

def init():
    url = input_url()
    if url is 'Q' or url is 'q':
        sys.exit()
    allHttpURLs = getURLCount(url)
    return allHttpURLs
  
def input_url():
    url = input("Enter the URL or Enter Q to exit : ")
    return url

def getURLCount(url):
    allHttpURLs = []
    try:
        req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        fHand = urllib2.urlopen(req)
        print(fHand)
    except:
        print ("URL is not correct! Try again!")
        init ( )
    pattern = '\"https?.+?\"'
    for line in fHand:
         urls = re.findall(pattern,line,re.IGNORECASE)
         allHttpURLs.extend(urls)
    return allHttpURLs


print ("*****Program to demonstrate the urlLib and REGEX*****")
allHttpURLs = init()
setallHttpURLs = set(allHttpURLs)
countofURLs = len(setallHttpURLs)
print ("The count of unique URLs on web page is:", countofURLs)
