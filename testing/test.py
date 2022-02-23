import requests
from bs4 import BeautifulSoup
import nmap

url = 'https://mtb.com'


def getInputField(url):

    allinput = []

    req = requests.get(url)

    print(req.status_code)

    soup = BeautifulSoup(req.text, 'html.parser')

    inputs = soup.findAll('input')

    for input in inputs:
        tag = input.attrs
        try:
            if  ('id' and 'type' and 'value') in tag.keys():
                id = tag['id']
                type = tag['type']
                value = tag['value']
                if tag['value'] == '':
                    value = 'Empty Value'
                allinput.append({'Id': id, 'Type': type, 'Value': value})
            elif ('id' and 'type') in tag.keys():
                id = tag['id']
                type = tag['type']
                allinput.append({'Id': id, 'Type': type, 'Value': 'No Value tag'})
            else:
                allinput.append({'fulltag': tag})
        except Exception as e:
            allinput.append({'Error': str(e), 'Error: No class defined for': str(input)})
    return allinput
    
    
# inputs = getInputField(url)

# for input in inputs:
#     for k, v in input.items():
#         print(k + ' ' + v)



def getLinks(url):

    allUrls = []

    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'html.parser')

    links = soup.findAll('a')

    for link in links:
        l = link.attrs
        try:
            if 'href' in l.keys():
                href = l['href']
                if '#' in l['href']:
                    continue
                allUrls.append({'href': href})
        except Exception as e:
            print(str(e))
    return allUrls


allLinks = getLinks(url)



def enumSite(links, url):

    alllinks = []

    for link in links:
        for v in link.values():
            if 'sitemap' in v:
                uri = v
            else:
                uri = v

    if 'sitemap' in uri:

        alllinks.append(getLinks(url + uri))

    else:

        alllinks.append(getLinks(url + uri))
    
    

print(getInputField(url))