from Yandex.yandex import YaDisk
from pprint import pprint
import json
with open('Token/token.json','r') as f:
    TOKEN=json.load(f)['token']
    


User = YaDisk(TOKEN)
pprint(User.getUsrInfo(fields="user.country,user.login,user.uid"))
pprint(User.getCatalogInfo(path='/',fields='_embedded.items.name,_embedded.items.type'))
pprint(User.getFileList("/Screenshots/"))
pprint(User.deleteDir("/Just\ meow"))
pprint(User.createDir("/Just\ meow/"))