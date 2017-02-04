import unittest

from tests.factories import (UserFactory, TextPostFactory, PicturePostFactory,
                             CheckInPostFactory)


class TestPosts(unittest.TestCase):

    def test_post_default_user(self):
        post = TextPostFactory()
        self.assertEqual(post.user, None)

    def test_post_set_user(self):
        user = UserFactory()
        post = TextPostFactory()
        post.set_user(user)
        self.assertEqual(post.user, user)

    def test_post_string_representation(self):
        user = UserFactory(first_name='Kevin', last_name='Watson')
        post1 = TextPostFactory()
        post2 = PicturePostFactory()
        post3 = CheckInPostFactory()

        post1.set_user(user)
        post2.set_user(user)
        post3.set_user(user)

        self.assertEqual(
            str(post1),
            '@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'
        )
        self.assertEqual(
            str(post2),
            '@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'
        )
        self.assertEqual(
            str(post3),
            '@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
        )
