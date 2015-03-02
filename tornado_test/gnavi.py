#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import urllib
import json

def reserve(price, category, lat, lng):
    url = 'http://api.gnavi.co.jp/ver1/RestSearchAPI/?'
    params = urllib.urlencode({
        'keyid': '2843445f5bdf7684d3c406f7382a38dd',
        'format': 'json',
        'category_l': category,
        'input_coordinates_mode': 1,
        'latitude': lat,
        'longitude': lng,
        'range': 4,
        })
    response = urllib.urlopen(url + params)
    print url+params
    shops = json.load(response)
    for i in xrange(len(shops['total_hit_count'])):
        if int(shops['rest'][i]['budget']) <= price:
            return shops['rest'][i]
    return None



if __name__ == '__main__':
    print reserve(5000, 'RSFST05000', 35.659185, 139.700523)




# End of Line.
