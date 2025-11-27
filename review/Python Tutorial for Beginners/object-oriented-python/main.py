"""_summary_
"""
from user import User
from post import Post

if __name__ == "__main__":
    alex = User("apaquette@email.com", "Alex Paquette", "pwd1", "Software Developer")
    alex.get_user_info()
    alex.change_job_title("Senior Developer")
    alex.get_user_info()

    alex_post = Post("on a secret mission", alex.name)
    alex_post.get_post_info()
