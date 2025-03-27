from django.core.management.base import BaseCommand
from django.utils.timezone import now
from posts.models import Post

class Command(BaseCommand):
    help = "Publishes scheduled posts"

    def handle(self, *args, **kwargs):
        posts = Post.objects.filter(scheduled_time__lte=now(), is_published=False)
        for post in posts:
            post.publish()
            self.stdout.write(self.style.SUCCESS(f"Published: {post.content}"))
