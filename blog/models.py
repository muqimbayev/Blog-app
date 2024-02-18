from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.author}'


class Like(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog}'








#Users
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True)
    telegram_id = models.BigIntegerField(unique=True)
    start_time = models.DateTimeField(auto_now_add=True)
    point = models.IntegerField(default=0)
    entry = models.IntegerField(default=0)
    middle = models.IntegerField(default=0)
    high = models.IntegerField(default=0)
    puzzle = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name
    
#Puzzle
class puzzle(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    a_option = models.CharField(max_length=50)
    b_option = models.CharField(max_length=50)
    c_option = models.CharField(max_length=50)
    d_option = models.CharField(max_length=50)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    

class puzzle_answers(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(puzzle, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_answer = models.BooleanField()
    is_true = models.BooleanField()

    def __str__(self):
        return f"{self.question_id}"
    


#Entry
class entry_questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    a_option = models.CharField(max_length=50)
    b_option = models.CharField(max_length=50)
    c_option = models.CharField(max_length=50)
    d_option = models.CharField(max_length=50)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    

class entry_answers(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(puzzle, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_answer = models.BooleanField()
    is_true = models.BooleanField()

    def __str__(self):
        return f"{self.question_id}"
    

#Middle
class middle_questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    a_option = models.CharField(max_length=50)
    b_option = models.CharField(max_length=50)
    c_option = models.CharField(max_length=50)
    d_option = models.CharField(max_length=50)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    

class middle_answers(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(puzzle, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_answer = models.BooleanField()
    is_true = models.BooleanField()

    def __str__(self):
        return f"{self.question_id}"
    

#High
class high_questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    a_option = models.CharField(max_length=50)
    b_option = models.CharField(max_length=50)
    c_option = models.CharField(max_length=50)
    d_option = models.CharField(max_length=50)
    image = models.ImageField()
    
    def __str__(self):
        return self.name
    

class high_answers(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(puzzle, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    is_answer = models.BooleanField()
    is_true = models.BooleanField()

    def __str__(self):
        return f"{self.question_id}"
    