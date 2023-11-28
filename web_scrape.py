# Retrieving HTML data from a domain name
# Parsing that date for target information
# Storing the target information
# Optionally, moving to another page to repeat the process


from urllib.request import urlopen

html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())








# import requests


# url = 'https://api.example.com/data'
# response = requests.get(url)

# if response.status_code == 200:
    data = response.json()
    # process the data here
# else:
    #print('Failed to retrieve data from the API')