from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp or datetime.utcnow()

    def set_user(self, user):
        self.user = user


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{date}'.format(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            text=self.text,
            date=self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{img}\n\t{date}'.format(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            text=self.text,
            img=self.image_url,
            date=self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return ('@{first_name} Checked In: "{text}"'
                '\n\t{coordinates}\n\t{date}').format(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            text=self.text,
            coordinates="{}, {}".format(self.latitude, self.longitude),
            date=self.timestamp.strftime("%A, %b %d, %Y"))
