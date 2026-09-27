from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from blog.models import Category, Post, Comment, ContactMessage
from blog.forms import contact_form, CommentForm


class CategoryModelTest(TestCase):
    def test_category_creation_and_str(self):
        category = Category.objects.create(name="Technology")
        self.assertEqual(str(category), "Technology")


class PostModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Python")

    def test_slug_auto_generation(self):
        post = Post.objects.create(
            title="Django Web Development Framework",
            content="Content about Django web app building.",
            category=self.category
        )
        self.assertEqual(post.slug, "django-web-development-framework")
        self.assertEqual(str(post), "Django Web Development Framework")


class ContactMessageModelTest(TestCase):
    def test_contact_message_creation_and_str(self):
        msg = ContactMessage.objects.create(
            name="John Doe",
            email="john@example.com",
            message="Hello Django team!"
        )
        self.assertEqual(str(msg), "John Doe (john@example.com)")


class CommentModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Sample Article",
            content="Sample article content body."
        )

    def test_comment_creation_and_str(self):
        comment = Comment.objects.create(
            post=self.post,
            name="Alice",
            email="alice@example.com",
            content="Great article!"
        )
        self.assertEqual(str(comment), f"Comment by Alice on {self.post.title}")
        self.assertIn(comment, self.post.comments.all())


class BlogViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cat1 = Category.objects.create(name="Django")
        self.cat2 = Category.objects.create(name="Python")

        # Create 7 posts for pagination testing
        self.posts = []
        for i in range(1, 8):
            post = Post.objects.create(
                title=f"Article Title {i}",
                content=f"Detailed body text for article number {i}.",
                category=self.cat1 if i % 2 != 0 else self.cat2
            )
            self.posts.append(post)

    def test_index_view_status_code_and_pagination(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('page_obj', response.context)
        self.assertEqual(len(response.context['page_obj']), 5)

        # Page 2 should have remaining 2 posts
        response_p2 = self.client.get(reverse('blog:index') + '?page=2')
        self.assertEqual(response_p2.status_code, 200)
        self.assertEqual(len(response_p2.context['page_obj']), 2)

    def test_index_view_search_filter(self):
        # Search matching "Title 1"
        response = self.client.get(reverse('blog:index') + '?q=Title 1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['page_obj']), 1)
        self.assertEqual(response.context['page_obj'][0].title, "Article Title 1")

        # Search matching non-existent string
        response_none = self.client.get(reverse('blog:index') + '?q=NonExistentKeyword')
        self.assertEqual(len(response_none.context['page_obj']), 0)

    def test_index_view_category_filter(self):
        response = self.client.get(reverse('blog:index') + f'?category={self.cat1.id}')
        self.assertEqual(response.status_code, 200)
        for post in response.context['page_obj']:
            self.assertEqual(post.category, self.cat1)

    def test_detail_view_and_related_posts(self):
        post = self.posts[0]
        url = reverse('blog:detail', kwargs={'slug': post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], post)
        
        # Related posts should exclude current post
        related = response.context['related_post']
        self.assertNotIn(post, related)

    def test_detail_view_404_for_invalid_slug(self):
        url = reverse('blog:detail', kwargs={'slug': 'non-existent-slug'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_comment_submission(self):
        post = self.posts[0]
        url = reverse('blog:detail', kwargs={'slug': post.slug})
        post_data = {
            'name': 'Tester',
            'email': 'tester@example.com',
            'content': 'This is a test comment.'
        }
        response = self.client.post(url, post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        # Check comment in database
        self.assertEqual(Comment.objects.filter(post=post).count(), 1)
        
        # Check messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn("added successfully", str(messages[0]))

    def test_contact_view_get_and_post_valid(self):
        url = reverse('blog:contact')
        response_get = self.client.get(url)
        self.assertEqual(response_get.status_code, 200)

        contact_data = {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'message': 'Hello from contact test!'
        }
        response_post = self.client.post(url, contact_data, follow=True)
        self.assertEqual(response_post.status_code, 200)

        # Check message saved in DB
        self.assertTrue(ContactMessage.objects.filter(email='jane@example.com').exists())

        # Check success flash message
        messages = list(get_messages(response_post.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn("sent successfully", str(messages[0]))

    def test_contact_view_invalid_post(self):
        url = reverse('blog:contact')
        invalid_data = {'name': '', 'email': 'not-an-email', 'message': ''}
        response = self.client.post(url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ContactMessage.objects.exists())

    def test_about_view(self):
        url = reverse('blog:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
