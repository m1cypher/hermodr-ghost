# https://xbopp.com/ghost-api-python-3-x-1/
# Note that the admin urls have changed to REMOVE v3 from the line. e.g. ghost/api/v3/admin/members = ghost/api/admin/members
# https://ghost.org/docs/admin-api/#


import requests
import os
import json
import jwt
from dotenv import load_dotenv
from datetime import datetime as date
from pprint import pprint
from io import BytesIO

load_dotenv()



GHOST_BLOG_URL = os.getenv("GHOST_BLOG")
ADMIN_Key = os.getenv("GHOST_ADMIN_KEY")
CONTENT_KEY = os.getenv("GHOST_CONTENT_KEY")


class GhostAdmin():
    """
    A class to interact with the Ghost API for administrative tasks.

    Example:
    
    ga = GhostAdmin('boydsbar')
    settings = ga.getSettings()
    members = ga.getMembers()
    post = ga.getPostBySlug('your-post-slug')
    post = ga.getPostById('your-post-id')
    allPosts = ga.getAllPosts()
    posts = ga.getPostByTitle('Your Post Title')
    result = ga.createPost('Your Post Title', 'Your Post Content', status='published')
    image = ga.loadImage('path/to/your/image.jpg')
    result = ga.imageUpload('YourImage.jpg', image)
    result = ga.updatePostByTitle('Old Post Title', 'New Post Title', 'New Post Content')
    result = ga.deletePostById('your-post-id')

    make sure you print or the returns, which include error messages, will not show.

    Example:
    # create post ---------------------------------------
    title = 'new post x'
    body = '''<div>Lorem ipsum dolor sit amet, ...</div>'''
    excerpt = 'this post is about ...'
    tags = [{'name':'my new tag x', 'description': 'a new tag'}]
    authors = [{'name':'Jacques Bopp', 'slug': 'jacques'}]
    featureImage = 'content/images/2020/09/featureImage1.jpg'
    slug = 'my-new-postx'
    result = ga.createPost(title, body, bodyFormat='html', excerpt=excerpt, tags=tags, authors=authors, status='draft', featured=False, featureImage=featureImage)
    # update post ---------------------------------------
    oldTitle = 'new post x'
    newTitle = 'updated post x'
    body = '''<div>Lorem ipsum  ...</div>'''
    excerpt = 'this post is about an update ...'
    tags = [{'name':'my new tag', 'description': 'a new tag'},{'name':'my second new tag', 'description': 'a second new tag'}]
    authors = [{'name':'Jacques Bopp', 'slug': 'jacques'},{'name':'Ghost', 'slug': 'ghost'}]
    featureImage = 'content/images/2020/09/featureImage2.jpg'
    result = ga.updatePostByTitle(oldTitle, newTitle, body, bodyFormat='html', excerpt=excerpt, tags=tags, authors=authors, status='draft', featured=False, featureImage=featureImage)
    """


    def __init__(self, siteName):
        """
        Initializes the GhostAdmin class.

        Args:
            siteName (str): The name of the site.
        """
        self.siteName = siteName
        self.site = None
        self.setSiteData()
        self.token = None
        self.headers = None
        self.createHeaders()

    def setSiteData(self):
        """
        Sets site data.
        """
        self.site = {
            'name': 'boydsbar',
            'url': GHOST_BLOG_URL,
            'AdminApiKey': ADMIN_Key,
            'ContentApiKey': CONTENT_KEY
        }

        return None


    def createToken(self):
        """
        Creates a token for authentication.
        
        Returns:
            str: The authentication token.
        """
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
        """
        Creates headers for the API request.
        
        Returns:
            dict: The headers for the API request.
        """
        self.createToken()
        self.headers = {
            'Authorization': f'Ghost {self.token}'
            }
        return self.headers

    def getSettings(self):
        """
        Retrieves settings from the Ghost API.
        
        Returns:
            dict: The settings from the Ghost API.
        """
        settings = {}
        url = self.site['url']+"/ghost/api/content/settings/?key="+self.site['ContentApiKey']
        result = requests.get(url, headers=self.headers)
        result.raise_for_status
        if result.ok:
            settings = json.loads(result.content)['settings']
        
        return settings
    
    def getMembers(self):
        """
        Retrieves members from the Ghost API.
        
        Returns:
            dict: The members from the Ghost API.
        """
        members = {}
        url = self.site['url']+'/ghost/api/admin/members'
        result = requests.get(url, headers=self.headers)
        if result.ok:
            members = json.loads(result.content)['members']
            for member in members:
                if member['name'] == None: member['name'] = ''
        
        return members
    
    def getPostBySlug(self,slug):
        """
        Retrieves a post by its slug from the Ghost API.
        
        Args:
            slug (str): The slug of the post.
        
        Returns:
            dict: The post retrieved by its slug.
        """
        url = self.site['url']+'/ghost/api/admin/slug/'+slug+'/'
        params = {'formats': 'html,mobiledoc'}
        result = requests.get(url, params=params, headers=self.headers)
        if result.ok:
            post = json.loads(result.text)['posts'][0]
        else: post = json.loads(result.text)

        return post
    
    def getPostById(self, id):
        """
        Retrieves a post by its ID from the Ghost API.
        
        Args:
            id (str): The ID of the post.
        
        Returns:
            dict: The post retrieved by its ID.
        """
        url = self.site['url']+'/ghost/api/admin/slug/'+id+'/'
        params = {'formats': 'html,mobiledoc'}
        result = requests.get(url, params=params, headers=self.headers)
        if result.ok:
            post = json.loads(result.text)['posts'][0]
        else: post = json.loads(result.text)

        return post
    
    def getAllPosts(self):
        """
        Retrieves all posts from the Ghost API.
        
        Returns:
            dict: All posts retrieved from the Ghost API.
        """
        url = self.site['url']+'/ghost/api/admin/posts/'
        params = {
            'formats': 'html,mobiledoc',
            'limit': 'all',
            'filter': 'slug: -tags'
        }
        result = requests.get(url, params=params, headers=self.headers)
        posts = json.loads(result.text)

        return posts
    
    def getPostByTitle(self, title):
        """
        Retrieves a post by its title from the Ghost API.
        
        Args:
            title (str): The title of the post.
        
        Returns:
            dict: The post retrieved by its title.
        """
        allPosts = self.getAllPosts()
        posts = []
        for post in allPosts:
            if post['title'] == title:
                posts.append(post)

        return posts

    def createPost(self, title, body, bodyFormat='markdown', excerpt=None, tags=None, authors=None, status='draft', featured=False, featuredImage=None, slug=None):
        """
        Args:
            body (string): the content of the post
            bodyFormat (string): 'html' , or 'markdown' (default)
            excerpt (string): the excerpt for a post
            tags (list): a list of dictionaries e.g. [{'name': 'my new tag', 'description': 'a very new tag'}]
            authors (list): a list of dictionaries e.g. [{'name': 'Odin The AllFather', 'slug': 'odin'}]
            status (string): 'published' or 'draft' (default)
            featured (bool): if the post should be featured
            featureImage (string): the image url (e.g. "content/images/2020/01/featureImage1_stamped.jpg) --> see uploadImage()

        Returns:
            result (string): If creation was successful or not

        Example:
            title = 'new post'
            body = <div>Lorem ipsum dolor sit amet</div>
            excerpt = 'this post is about ...'
            tags = [{'name':'my new tag', 'description': 'a new tag'}]
            authors = [{'name':'Jacques Bopp', 'slug': 'jacques'}]
            slug = 'my-new-post'
    
            result = ga.createPost(title, body, bodyFormat='html', excerpt = excerpt, tags=tags, authors=authors, status='draft', featured=False, featuredImage=None, slug=slug)
        """ 
        content = {'title': title}
        if bodyFormat == 'markdown':
            content['mobiledoc'] = json.dumps({'version': '0.3.1', 'markups': [], 'atoms': [], 'cards': [['markdown', {'cardName': 'markdown', 'markdown': body}]], 'sections': [[10, 0]]})
        else: 
            content['html'] = body
        if excerpt != None: 
            content['custom_excerpt'] = excerpt
        if tags != None: 
            content['tags'] = tags
        if authors != None: 
            content['authors'] = authors
        content['status'] = status
        content['featured'] = featured
        if featuredImage != None: 
            content['featuredImage'] = self.site['url'] + featuredImage
        if slug != None: 
            content['slug'] = slug

        url = self.site['url'] + '/ghost/api/admin/posts'
        params = {'source': 'html'}
        result = requests.post(url, params=params, json={"posts": [content]}, headers=self.headers)

        status_code = result.status_code

        if result.ok: 
            result = f'success: post created (status_code: {status_code})'
        else:
            result = f'error: post not created (status_code: {status_code})'
        
        return result
    
    def loadImage(self, imagePathandName):
        """
        Loads an image.
        
        Args:
            imagePathandName (str): The path and name of the image file.
        
        Returns:
            BytesIO: The image object.
        """
        image = open(imagePathandName, 'rb')
        imageObject = image.read()
        image.close()
        image = BytesIO(imageObject)

        return image
    
    def imageUpload(self, imageName, imageObject):
        """
        Uploads an image to the Ghost API.
        
        Args:
            imageName (str): The name of the image.
            imageObject (BytesIO): The image object to be uploaded.
        
        Returns:
            str: A message indicating whether the image upload was successful as well as the url for the image to be used as featured image or in the post.
        """
        url = self.site['url'] + '/ghost/api/admin/images/upload'
        files = {"file": (imageName, imageObject, 'image/jpeg')}
        params = {'purpose': 'image', 'ref': imageName} # 'image', 'profile_image', 'icon'
        result = requests.post(url, files=files, params=params, headers=self.headers)
        print(result.status_code)
        print(result.text)
        if result.ok:
            result = 'success: ' + json.loads(result.text)['images'][0]['url']
        else:
            result = f'error: upload failed (status code: {result.status_code})'

    def updatePostByTitle(self, oldTitle, newTitle, body, bodyFormat='markdown', excerpt=None, tags=None, authors=None, status='draft', featured=False, featuredImage=None):
        """
        Updates a post by its title.
        
        Args:
            oldTitle (str): The old title of the post.
            newTitle (str): The new title of the post.
            body (str): The content of the post.
            bodyFormat (str): The format of the post content. Default is 'markdown'.
            excerpt (str): The excerpt for the post.
            tags (list): A list of dictionaries.
            authors (list): A list of dictionaries.
            status (str): The status of the post. Default is 'draft'.
            featured (bool): Whether the post should be featured.
            featureImage (str): The URL of the featured image.
        
        Returns:
            str: A message indicating whether the post update was successful.
        """
        posts= self.getPostByTitle(oldTitle)
        if len(posts) > 1:
            result = 'error: more than 1 post found'
        elif len(posts) == 0:
            result = 'error: no posts found'
        else:
            post = posts[0]
            content = {'title': newTitle}
            if bodyFormat == 'markdown':
                content['mobiledoc'] = json.dumps({'version': '0.3.1', 'markups': [], 'atoms': [], 'cards': [['markdown', {'cardName': 'markdown', 'markdown': body}]], 'sections': [[10, 0]]})
            else: 
                content['html'] = body
            if excerpt != None: 
                content['custom_excerpt'] = excerpt
            if tags != None: 
                content['tags'] = tags
            if authors != None: content['authors'] = authors
            content['status'] = status
            content['featured'] = featured
            if featuredImage != None: 
                content['feature_image'] = self.site['url'] + featuredImage
            content['updated_at'] = post['updated_at']
            url = self.site['url'] + '/ghost/api/admin/posts/' + post['id'] + '/'
            result = requests.put(url, json={"posts": [content]}, headers=self.headers)
            if result.ok: 
                result = 'success: post updated (status_code:' + str(result.status_code) + ')'
            else: 
                result = 'error: post not updated (status_code:' + str(result.status_code) + ')'

        return result
    
    def deletePostById(self, id):
        """
        Deletes a post by its ID.
        
        Args:
            id (str): The ID of the post to be deleted.
        
        Returns:
            str: A message indicating whether the post deletion was successful.
        """
        url = self.site['url'] + '/ghost/api/admin/posts/' + id + '/'
        result = requests.delete(url, headers=self.headers)
        if result.ok:
            result = f'success: post deleted (status_code: {result.status_code})'
        else:
            result = f'error: post NOT deleted (status_code: {result.status_code})'

        return result

