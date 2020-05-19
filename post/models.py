from django.db import models
from django.db.models.signals import pre_save
from slug_generator.utils import unique_slug_generator

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=250, null= True, blank= True)
	body = models.TextField()

	def __str__(self):
		return self.title


def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance)       #instance.slug = unique_slug_generator(instance,instance.title)
  
  
pre_save.connect(pre_save_receiver, sender = Post) 

