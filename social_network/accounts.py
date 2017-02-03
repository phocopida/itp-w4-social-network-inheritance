class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        self.following = []
        self.posts = []

    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)

    def get_posts_by_followers(self):
        posts = []
        for user in self.following:
            posts += user.posts

        return sorted(posts, key=lambda p: p.timestamp, reverse=False)

    def follow(self, other):
        self.following.append(other)
