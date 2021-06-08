import requests
from pprint import pprint

URL = 'https://api.covid19api.com/summary'

covid19 = requests.get(URL)
covid19_global = covid19.json()["Global"]
covid19 = covid19.json()["Countries"]
# pprint(covid19)

# pprint(covid19_global)
tytles = ([ item for item in list(covid19[0].keys()) if item not in ['ID', 'CountryCode', 'Slug', 'Date', 'Premium']])

for item in tytles:
    if item == 'Country':
        print("{0:_^30s}".format(item), end='')
    else:
        print("{0:_^20s}".format(item), end='')
else:
    print(' ')


def byNewConfirmed_key(covid19):
    return covid19["NewConfirmed"]

covid19 = sorted(covid19, key=byNewConfirmed_key, reverse=True )

for item in covid19:
    for key in item:
        if key in tytles:
            if key == 'Country':
                print("{0:<30}".format(item[key]), end='')
            else:
                print("{0:>20}".format(item[key]), end='')
    else:
        print('')
