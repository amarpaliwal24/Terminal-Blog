import uuid
import datetime
from database import Database
from models.post import Post


class Blog(object):

    def __init__(self, author, title, description, id=None, _id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id
        self._id=_id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYYYY): ")

        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, '%d%m%Y')

        post = Post(
                author = self.author,
                title = title,
                content = content,
                blog_id = self.id,
                created_date = date
               )

        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert('blogs', data=self.json())

    def json(self):
        return {
            'id' : self.id,
            'author' : self.author,
            'title' : self.title,
            'description' : self.description
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'id' : id})
        blog_object = cls(**blog_data)
        return blog_object