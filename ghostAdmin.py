import requests
import os
import json
import jwt
from dotenv import load_dotenv
from datetime import datetime as date
from pprint import pprint

load_dotenv()



GHOST_BLOG_URL = os.getenv("GHOST_BLOG")
ADMIN_Key = os.getenv("GHOST_ADMIN_KEY")
CONTENT_KEY = os.getenv("GHOST_CONTENT_KEY")


class GhostAdmin():
    def __init__(self, siteName):
        self.siteName = siteName
        self.site = None
        self.setSiteData()
        self.token = None
        self.headers = None
        self.createHeaders()

    def setSiteData(self):
        self.site = {
            'name': 'boydsbar',
            'url': GHOST_BLOG_URL,
            'AdminApiKey': ADMIN_Key,
            'ContentApiKey': CONTENT_KEY
        }

        return None


    def createToken(self):
        key = self.site['AdminApiKey']
        id, secret = key.split(':')
        iat = int(date.now().timestamp())
        header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
        payload = {
        'iat': iat,
        'exp': iat + 5 * 60,
        'aud': '/admin/'
        }
        self.token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)
        
        return self.token

    def createHeaders(self):
        self.token
        self.headers = {
            'Authorization': f'Ghost {self.token}'
            }
        
        return self.headers

    def getSettings(self):
        settings = {}
        url = self.site['url']+"/ghost/api/content/settings/?key="+self.site['ContentApiKey']
        result = requests.get(url, headers=self.headers)
        result.raise_for_status
        if result.ok:
            settings = json.loads(result.content)['settings']
        
        return settings
    
    def getMembers(self):
        members = {}
        url = self.site['url']+'/ghost/api/v3/admin/members'
        result = requests.get(url, headers=self.headers)
        if result.ok:
            members = json.loads(result.content)['members']
            for member in members:
                if member['name'] == None: member['name'] = ''
        
        return members
    
    def getPostBySlug(self,slug):
        url = self.site['url']+'/ghost/api/admin/slug/'+slug+'/'
        params = {'formats': 'html,mobiledoc'}
        result = requests.get(url, params=params, headers=self.headers)
        if result.ok:
            post = json.loads(result.text)['posts'][0]
        else: post = json.loads(result.text)

        return post
    
    def getPostById(self, id):
        url = self.site['url']+'/ghost/api/admin/slug/'+id+'/'
        params = {'formats': 'html,mobiledoc'}
        result = requests.get(url, params=params, headers=self.headers)
        if result.ok:
            post = json.loads(result.text)['posts'][0]
        else: post = json.loads(result.text)

        return post
    
    def getAllPosts(self):
        url = self.site['url']+'/ghost/api/v3/admin/posts/'
        params = {
            'formats': 'html,mobiledoc',
            'limit': 'all',
            'filter': 'slug: -tags'
        }
        result = requests.get(url, params=params, headers=self.headers)
        posts = json.loads(result.text)

        return posts
    
    def getPostByTitle(self, title):
        allPosts = self.getAllPosts()
        posts = []
        for post in allPosts:
            if post['title'] == title:
                posts.append(post)

        return posts 


if __name__ == '__main__':
    ga = GhostAdmin('boydsbar')
    posts = ga.getAllPosts()
    members = ga.getMembers()
    settings = ga.getSettings()

print(ga.getMembers())