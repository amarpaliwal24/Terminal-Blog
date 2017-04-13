import uuid
from database import Database
import datetime

class Post(object):

    def __init__(self, title, content, author, blog_id, created_date=datetime.datetime.utcnow(), id=None, _id=None):
        self.title=title
        self.content=content
        self.author=author
        self.blog_id=blog_id
        self.created_date=created_date
        self.id=uuid.uuid4().hex if id is None else id
        self._id=_id

    def json(self):
        return {
            'id' : self.id,
            'blog_id' : self.blog_id,
            'author' : self.author,
            'title' : self.title,
            'content' : self.content,
            'created_date' : self.created_date
        }

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    @classmethod
    def from_mongo(cls, post_id):
        post_data = Database.find_one(collection='posts', query={'id' : post_id})
        post_object = cls(**post_data)
        return post_object

    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find(collection='posts', query={'blog_id' : blog_id})]
