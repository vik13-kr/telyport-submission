from django.db import models

class Member(models.Model):
    ''' 
    Model to save instances of members
    '''

    id = models.CharField(primary_key= True, max_length= 20)
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length = 100) 
    auth_token = models.CharField(max_length = 64)


    def __str__(self):
        return self.first_name
