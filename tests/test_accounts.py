import unittest

from social_network.accounts import User
from tests.factories import UserFactory, TextPostFactory, PicturePostFactory


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User(first_name='John', last_name='Doe', email='john@doe.com')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'john@doe.com')

    def test_user_follow(self):
        user1 = UserFactory()
        user2 = UserFactory()
        user1.follow(user2)
        self.assertEqual(len(user1.following), 1)
        self.assertTrue(user2 in user1.following)

    def test_add_post(self):
        user = UserFactory()
        post1 = TextPostFactory()
        post2 = PicturePostFactory()
        user.add_post(post1)
        user.add_post(post2)
        self.assertEqual(len(user.posts), 2)

    def test_user_get_posts_by_followers(self):
        """Should only return posts from users I'm following"""
        user1 = UserFactory()
        user2 = UserFactory()
        user3 = UserFactory()
        user4 = UserFactory()

        user2_post1 = TextPostFactory()
        user2_post2 = TextPostFactory()
        user3_post1 = PicturePostFactory()
        user4_post1 = TextPostFactory()

        user2.add_post(user2_post1)
        user2.add_post(user2_post2)
        user3.add_post(user3_post1)
        user4.add_post(user4_post1)

        # user1 follows user2 and user3
        user1.follow(user2)
        user1.follow(user3)

        # 2 posts from user2 and 1 from user3
        # post from user4 is excluded
        self.assertEqual(len(user1.get_timeline()), 3)

        self.assertFalse(user4_post1 in user1.get_timeline())

        # should be sorted by creation timestamp
        self.assertEqual(user1.get_timeline(), [
            user2_post1,
            user2_post2,
            user3_post1
        ])
