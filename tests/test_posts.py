import unittest

from tests.factories import (UserFactory, TextPostFactory, PicturePostFactory,
                             CheckInPostFactory)


class TestPosts(unittest.TestCase):

    def test_post_string_representation(self):
        user = UserFactory()
        post1 = TextPostFactory()
        post2 = PicturePostFactory()
        post3 = CheckInPostFactory()

        post1.set_user(user)
        post2.set_user(user)
        post3.set_user(user)

        self.assertEqual(
            str(post1),
            '@Kevin Watson: "Sample post text"\n\tFriday, Feb 03, 2017'
        )
