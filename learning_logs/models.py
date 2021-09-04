from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    ''' User learning topic '''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        ''' Returns the string representation of the model'''
        return self.text


class Entry(models.Model):
    '''Specific content on the subject'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''
        Returns the string representation of the model
        and limit the number of displayed words to less than 50
        '''
        return self.text[:50]+'...'
