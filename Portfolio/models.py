from django.db import models
# from django.urlresolvers import reverse_lazy
# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=255,default='SOME STRING')
    image = models.ImageField(
        upload_to="C:/Users/user/Desktop/master/studyProject-1/media"
    )
    content = models.TextField(default="Some String")
    # created_at = models.DateTimeField(auto_now_add=True, default="some") 
      
    # def get_absolute_url(self):
    #     url = reverse_lazy('Portfolio', kwargs={'pk': self.pk})
    #     return url
        
    def __str__(self):
        return self.title
