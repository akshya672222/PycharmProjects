# SSW 540 - Assignment 11 - P11: Browsing the Web
# Akshay Sunderwani

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import io
import re


url_input = input('Please enter the URL: ')
response = ''

try:
    req = urllib2.Request(url_input, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(req)
except:
    print('The webpage is not accessible.')
    quit()

f = io.TextIOWrapper(response,encoding='utf-8')
the_page = f.read()
lines = the_page.split('\n')
url_list = []
for line in lines:
    lower_url = line.lower()
    urls = re.findall ( 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' , lower_url )
    if len(urls) > 0:
        for items in urls:
            if items not in url_list:
                url_list.append ( items )
print('Total no of unique weblinks : ',len(url_list))
