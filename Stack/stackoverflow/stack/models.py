from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    image = models.FileField(upload_to='images', null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
    


class BaseModel(models.Model):
    created_at=models.DateField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        abstract = True

class Questions(BaseModel):
    name=models.CharField(max_length=255)
    tag=models.CharField(max_length=50)
    description=models.TextField()
    up_vote = models.IntegerField(null=True,blank=True)
    down_vote = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name

class Answer(BaseModel):
    name=models.TextField()   
    questions=models.ForeignKey(Questions,on_delete=models.CASCADE)
    up_vote = models.IntegerField(null=True,blank=True)
    downvote=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name
    

class Reply(BaseModel):
    ans=models.TextField()
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.ans



    

