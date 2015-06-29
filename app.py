from bottle import route, run, response, request, app, redirect
import urllib
import json
import re
from jpaddress import get_jp_address


def get_page_data(url):
    p = re.compile(r'<.*?>')
    page = urllib.urlopen(url)
    data = page.read()
    # Remove html tags
    data = p.sub('', data)
    # Remove whitespace
    data = data.replace(' ','')
    # return as unicode
    return unicode(data, 'utf-8')

@route('/')
def get_address():
    query = dict(request.query)
    url = query['q']
    data = get_jp_address(get_page_data(url))
    results = [{'address':x[0]} for x in data]
    response.set_header('Content-Type','text/json')
    return json.dumps(results)



if __name__ == '__main__':
    run(host='0.0.0.0', port=9080)
