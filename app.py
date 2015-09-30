import urllib
import json
import re
import os
import chardet
from bottle import route, run, response, request, app, redirect
from jpaddress import get_jp_address


def get_page_data(url):
    p = re.compile(r'<.*?>')
    page = urllib.urlopen(url)
    data = page.read()
    enc = chardet.detect(data)
    # Remove html tags
    data = p.sub('', data)
    # Remove whitespace
    data = data.replace(' ','')
    # return as unicode
    return unicode(data, enc['encoding'])

@route('/')
def get_address():
    query = dict(request.query)
    url = query['q']
    data = get_jp_address(get_page_data(url))
    results = [{'address':x[0]} for x in data]
    response.set_header('Content-Type','application/json')
    return json.dumps(results, indent=2, sort_keys=True, ensure_ascii=False)

@route('/pt')
def get_address_pt():
    query = dict(request.query)
    url = query['q']
    data = get_jp_address(get_page_data(url))
    response.set_header('Content-Type','text/plain')
    return '\n'.join([x[0] for x in data])

if __name__ == '__main__':
    # Use
    # heroku config:set HEROKU=true
    # to set the env variable
    if os.getenv("HEROKU")==None:
        run(host="localhost", port=(os.environ.get("PORT",5200)), debug=True, reloader=True)
    else:
        run(host="0.0.0.0", port=(os.environ.get("PORT",5200)))
