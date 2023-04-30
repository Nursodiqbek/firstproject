from django.db import models

class Article(models.Model):
    LOCAL='local'
    WORLD='world'
    SPORT='sport'

    TAG=(

        ('local',LOCAL),
        ('world',WORLD),
        ('sport',SPORT)
    )


    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True, blank=True)
    context = models.TextField()
    tag=models.CharField(max_length=20,choices=TAG,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def image_url(self):
        return self.image.url


    def __str__(self):
        return self.title
