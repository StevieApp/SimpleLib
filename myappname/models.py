import uuid
from django.db import models

# Create your models here.
class ProfilePhoto(models.Model):
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    id = models.BigAutoField(primary_key=True)

class BookImage(models.Model):
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    id = models.BigAutoField(primary_key=True)

class BookClub(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True) 
    id = models.BigAutoField(primary_key=True) 
    def __str__(self):
        return self.name

class User(models.Model):
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS)
    email = models.EmailField(max_length=100)
    profile_pic = models.OneToOneField(ProfilePhoto, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    id = models.BigAutoField(primary_key=True)
    book_club = models.ManyToManyField(BookClub, blank=True)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    id = models.BigAutoField(primary_key=True) 
    def __str__(self):
        return self.name

#create book model
class Book(models.Model):
    sku = models.IntegerField(serialize=True,unique=True, auto_created=True, default=uuid.uuid4)
    book_image = models.OneToOneField(BookImage, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_published = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True)
    id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return self.name

    # def getId(__self) =
    #     print(__self.id)


#, on_delete =models.CASCADE
# myauthor  = User.objects.create(name ="John Asembo")
# mybook  = Books.objects.create(name ="The Lion and The Rabbit")