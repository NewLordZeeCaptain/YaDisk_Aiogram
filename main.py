from Yandex.yandex import YaDisk
from pprint import pprint
import json
with open('Token/token.json','r') as f:
    result=json.load(f)
    YANDEX_TOKEN=result['yandex_token']
    BOT_TOKEN=result['telegram_token']
    del result
    


User = YaDisk(YANDEX_TOKEN)
pprint(User.getUsrInfo(fields="user.country,user.login,user.uid"))
pprint(User.getCatalogInfo(path='/',fields='_embedded.items.name,_embedded.items.type'))
pprint(User.getFileList("/Screenshots/"))
pprint(User.deleteDir("/Just\ meow"))
# pprint(User.createDir("/Just\ meow/"))
User.deleteDir("/Just\ meow/",permanently=True)
User.createDir("/Just\ meow/Meow/emow")
pprint(User.move(path_from="/Just\ meow/Meow/emow",path_to="Emow"))