from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User

# পোস্ট মডেল টেস্ট
class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.post = Post.objects.create(title="Test Post", content="This is a test post.", author=self.user)

    def test_post_content(self):
        """এখানে আমরা পোস্টের কনটেন্ট টেস্ট করছি"""
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.author.username, "testuser")

# পোস্ট লিস্ট ভিউ টেস্ট
class PostListViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.post = Post.objects.create(title="Test Post", content="This is a test post.", author=self.user)

    def test_post_list_view(self):
        """এখানে আমরা পোস্ট লিস্ট ভিউ টেস্ট করছি"""
        response = self.client.get(reverse('home'))  # 'home' হল পোস্ট লিস্টের URL
        self.assertEqual(response.status_code, 200)  # সঠিক HTTP স্ট্যাটাস কোড আশা করছি
        self.assertContains(response, 'Test Post')  # আমাদের পোস্টের শিরোনাম দেখে নিশ্চয়তা নেওয়া হচ্ছে

# পোস্ট ডিটেইল ভিউ টেস্ট
class PostDetailViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.post = Post.objects.create(title="Test Post", content="This is a test post.", author=self.user)

    def test_post_detail_view(self):
        """এখানে আমরা পোস্ট ডিটেইল ভিউ টেস্ট করছি"""
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test post.')
