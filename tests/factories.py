from datetime import datetime

import factory

from social_network import accounts, posts


class UserFactory(factory.Factory):
    class Meta:
        model = accounts.User

    first_name = factory.Iterator(['Kevin', 'Joe', 'Ervin', 'Daniel'])
    last_name = factory.Iterator(['Watson', 'Fowler', 'Roberts', 'Wiley'])
    email = factory.LazyAttribute(lambda u: '{}.{}@fake-domain.com'.format(
        u.first_name, u.last_name))


class PostFactory(factory.Factory):
    class Meta:
        model = posts.Post

    text = 'Sample post text'
    timestamp = datetime(2017, 1, 10)


class TextPostFactory(PostFactory):
    class Meta:
        model = posts.TextPost


class PicturePostFactory(PostFactory):
    class Meta:
        model = posts.PicturePost

    image_url = 'http://fake-domain.com/images/sample.jpg'


class CheckInPostFactory(PostFactory):
    class Meta:
        model = posts.CheckInPost

    latitude = -34.603722
    longitude = -58.381592
