from django.db import models

class Books(models.Model):
    name = models.TextField(blank=False, null=False)
    author = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    def serialize(self):
        return {
            "id" : self.id,
            "name": self.name,
            "author": self.author,
            "description" : self.description,
            
        }   
        
""" "image" : self.image """
"""     image = models.FileField(upload_to='images/', blank=True, null=True)"""    
