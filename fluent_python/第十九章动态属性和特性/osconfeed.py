from urllib.request import urlopen
import warnings
import os
import json

url = 'http://www.oreilly.com/pub/sc/osconfeed'
Json = './osconfeed.json'

def load():
    if not os.path.exists(Json):
        msg = 'downloading {} to{}'.format(url,Json)
        warnings.warn(msg)
        with urlopen(url) as remote,open(Json,'wb' ) as local:
            local.write(remote.read())

        with open(Json) as fp:
            return json.loads(fp)



feed = load()
print(feed)
        