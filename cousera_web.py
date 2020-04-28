# Regular expressions - Quick guide
'''
	^		- Matches the beguinning of a line
	&		- Matches the end of a line
	.		- Matches any character 
	/s		- (Backslash) Matches whitespace
	/S		- (Backslash) Matches any non-whitespace character
	*		- Repeats a character zero or more times
	*?		- Repeats a character zero or more times (non - greedy)
	+		- Repeats a character one or more times
	+?		- Repeats a character one or more times (non - greedy)\
    [aeious]- Matches a single character in the listed set
    [^XYZ]  - Matches a single character not in the listed set
    [a-Z0-9]- The set of characters can include a range
    (		- Indicates where string extraction is due to start
    )		- Indicates where string extraction is due to end
	
'''


'''
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_404058.txt (There are 61 values and the sum ends with 323)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
'''

import re

name = input("Enter file:")
if len(name) < 1 : name = "r_expression(actual).txt"
fh = open(name)
numlist = []
extract_list = []


def convert(item_list):
    # converting strings to integers
    numlist = []
    for item in item_list:
        num = int(item)
        numlist.append(num)
    return numlist

def add_list(item_list):
    # Adding up elements in list
    result = 0
    for item in item_list: 
        result = result + item
    return result


for line in fh:
    line = line.rstrip()
    extract = re.findall('([0-9]+)', line)
    if len(extract) < 1:
        continue
    else:
        converted = convert(extract)
        total = add_list(converted)
        numlist.append(total)


total = add_list(numlist)
print(total)




# Retrieving webpages:

# Using sockets:
'''
import sockets


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(({'domain_name'}, {port}))
'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()




# Using Urllib:
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

counts = dict()
for line in fhand:
	words = line.decode().split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

print(counts)



# Web scraping - Beautiful Soup template


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

'''
Scraping Numbers from HTML using BeautifulSoup 

In this assignment you will write a Python program that will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_404060.html (Sum ends with 35)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format
The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter Url - ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_404060.html\n'


html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = 0
total = 0
comment_num = None

tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    comments = int(tag.contents[0])
    count = count + 1  
    total = total + comments


print('Count', count)
print('Sum', total)




'''Following Links in Python

In this assignment you will write a Python program that will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Drew.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: F
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = int(input('Enter count '))
position = int(input('Enter position '))
run_count = 0
active = True

def get_link(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


    # Retrieve all of the anchor tags
    link_position = 0
    tags = soup('a')
    for tag in tags:
        link_position = link_position + 1
        if link_position == position:
            link = tag.get('href', None)
            return link
        else:
            continue

print('Retrieving:', url)
new_url = get_link(url)

while active:
    if run_count != count:
        print('Retrieving:', new_url)
        new_url = get_link(new_url)
        run_count = run_count + 1
    else:
        active = False
        # print('Retrieving:', get_link(url))
        break




'''
Extracting Data from XML

In this assignment you will write a Python program which will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_404062.xml (Sum ends with 8)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.   
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_404062.xml'

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx).read()
    uh = uh.decode()
    print('Retrieved', len(uh), 'characters')
    result = 0

    tree = ET.fromstring(uh)
    lst = tree.findall('comments/comment')
    print('Count:',len(lst))
    for comment in lst:
        num = int(comment.find('count').text)
        result = result + num
    print('Sum:', result)
    break



'''
Extracting Data from JSON

In this assignment you will write a Python program that will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_404063.json (Sum ends with 47)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_404063.json'

print('Retrieving:', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
headers = dict(connection.getheaders())
print('Retrieved', headers['Content-Length'], 'characters')
count_sum = 0


info = json.loads(data)
print('Count:',len(info['comments']))


for item in info['comments']:
    item_count = int(item['count'])
    count_sum = count_sum + item_count

print('Sum:', count_sum)


'''
Calling a JSON API

In this assignment you will write a Python program. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.
'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    place_id = js['results'][0]['place_id']
    print('Place_id', place_id)
    break
