class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
        
    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)

    def add_post(self, post):
        self.posts.append(post)

        
    def get_timeline(self):
        self.timeline = []
        for i in self.following:
            self.timeline += i.posts
            
        self.timeline = sorted(self.timeline, key= lambda post: post.timestamp)
        return self.timeline
        
    def follow(self, other):
        self.following.append(other)