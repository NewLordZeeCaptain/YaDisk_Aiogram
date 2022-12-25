import json
import requests as r


class YaDisk(object):
    """This object is used to work with Yandex.Disk API"""
    ways = ['/resources', '/public/resources', '/trash/resources']

    def __init__(self, token):
        super(YaDisk, self).__init__()
        self.BASE = 'https://cloud-api.yandex.net/v1/disk'
        self.URL = [str(self.BASE + way) for way in self.ways]
        self.headers = {"Content-Type": "application/json",
                        "Authorization": token}

    def getUsrInfo(self, fields='user.country,user.login,user.uid'):
        """Return User Info"""
        params = {'fields': fields}
        resp = r.get(self.BASE, headers=self.headers, params=params)
        return json.loads(resp.text)

    def getCatalogInfo(self, fields='_embedded.items.name,_embedded.items.type', path='/'):
        params = {"fields": fields, "path": path}
        resp = r.get(self.URL[0], headers=self.headers, params=params)
        return json.loads(resp.text)

    def getFileList(self, path, fields='items.name,items.path,items.type,items.media_type', media_type='', sort=''):
        """User to get file List and filter result

        Args:
            path (str): Directory where you're searching files
            fields (str, optional): This shows what fields of json output you will see. Defaults to 'items.name,items.path,items.type,items.media_type'.
            media_type (str, optional): filter with content type. Defaults to ''.
        """
        params = {'path': path, 'fields': fields,
                  'media_type': media_type, 'sort': sort}
        resp = r.get(self.URL[0]+'/files', params=params, headers=self.headers)
        return json.loads(resp.text)

    def deleteDir(self, path, permanently=False):
        params = {'path': path, 'permanently': permanently}

        resp = r.delete(self.URL[0], headers=self.headers, params=params)
        if resp.status_code == 404:
            print("File doesn't exist yet")
            return
        else:
            print("File has been deleted. Have a good day.")

    def createDir(self, path, fields=''):
        params = {'path': path, 'fields': fields}
        resp = r.put(self.URL[0], params=params, headers=self.headers)
        if resp.status_code == 409:
            print(
                "This dir is already exists. Whould you like to delete it and create new? ")
        return json.loads(resp.text)

    def move(self, path_from, path_to, fields='', overwrite=False):
        params = {"from": path_from, "path": path_to+path_from,
                  "fields": fields, "overwrite": overwrite}
        resp = r.post(self.URL[0]+"/move", params=params, headers=self.headers)
        return json.loads(resp.text)
