from src.common.database import Database
from src.models.blog import Blog

class Menu(object):

    def __init__(self):
        print("Welcome to this blogging website ! ")
        self.user = input("Enter your name, Author :")
        self.blog_user = None

        if self._user_has_account():
            print("Welcome back, {} ".format(self.user))
        else :
            self._prompt_user_for_account()


    def _user_has_account(self):
            blog = Database.find_one(collection='blogs', query={'author' : self.user})

            if blog is not None:
                self.blog_user = Blog.from_mongo(blog['id'])
                return True
            else:
                return False


    def _prompt_user_for_account(self):
        print("Let's post your first blog for profile creation !")

        title = input("Insert title here: ")
        description = input("Insert description here: ")

        blog = Blog(author=self.user,
                    title=title,
                    description=description)

        self.blog_user = blog
        self.blog_user.save_to_mongo()

    def _run_menu(self):
        read_or_write = input("Do you want to read(R) or write(W) a blogs ?")
        if read_or_write == "R":
            self._list_blogs()
            self._view_blogs()
        elif read_or_write == "W":
            self._write_post()
        else:
            print("Thank you for blogging !")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        blog_id = input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_id)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))

    def _write_post(self):
        self.blog_user.new_post()







