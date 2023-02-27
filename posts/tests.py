from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

User = get_user_model()


# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="test",
            email="test@admin.com",
            password="friction",
        )

        cls.post = Post.objects.create(
            title='blog post title',
            body='post body',
            author=cls.user,
        )

    def test_post(self):
        self.assertEqual(self.post.title, 'blog post title')
        self.assertEqual(self.post.body, 'post body')
        self.assertEqual(str(self.post.body), 'post body')
