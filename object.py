from user import User
from post import Post

app_user_one = User("dmtest@gmal.com", "Deba Mukher", "secret", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("Cloud Engineer")
app_user_one.get_user_info()

app_user_post = Post("we are hiring", app_user_one.name)
app_user_post.get_post_info()
