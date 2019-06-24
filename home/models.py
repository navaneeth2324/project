from django.db import models
from datetime import date

# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=100,help_text='Book name',null=True)
    book_auth=models.CharField(max_length=100,help_text='Book author',null=True)

    def __str__(self):
      return self.name+" by "+self.book_auth

class Movie(models.Model):
    Movie=models.CharField(max_length=100,help_text="Movie Name",null=True)
    Director=models.CharField(max_length=100,help_text="Director Name",null=True)
    Producer=models.CharField(max_length=100,help_text="Producer Name",null=True)
    mychoice=(('1','one'),
    ('2','Two'),
    ('3','Three'))

    typechoice=(
    ('1','Thriller'),
    ('2','Action'),
    ('3','Romantic'),
    ('4','Si-Fi'),
    ('5','Comedy'))
    ReleaseDate=models.DateField(null=True,blank=True)
    Awards=models.CharField(max_length=2,help_text="Awards won",choices=mychoice,default=1)
    Category=models.CharField(max_length=2,help_text="Movie Category",choices=typechoice,default=5)

    def __str__(self):
        return self.Movie
    

class Novel(models.Model):
    #id = models.UUIDField('Novel Id',primary_key=True, default = uuid.uuid4, help_text="generated unique id for book")
    novel_name = models.CharField(max_length=100, help_text='Novel Name',null=True)
    purchase_date = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField('Genre', help_text='genre of Novel')
    author = models.ForeignKey('Author',on_delete=models.SET_NULL ,help_text='Novel Author', null=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.novel_name


class Author(models.Model):
    author_name = models.CharField(max_length=100, help_text='Name of Author',null=True)
    numChoice = (
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5', 'Five')
    )
    total_Novels_written = models.CharField(max_length=1, choices=numChoice)
    date_of_birth = models.DateField('Birth',null=True, blank=True)
    date_of_death = models.DateField('Death',null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author_name

class Genre(models.Model):
    _name = models.CharField(max_length=100, help_text='Book Name',null=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self._name 


class library(models.Model):
    Studentname=models.CharField(max_length=100,help_text='Student Name',null=True)
    Branch=models.CharField(max_length=50,help_text='Branch',null=True)
    IssueDate=models.DateField('Issued',default=date.today,blank=False)
    SubmissionDate=models.DateField('Submission',null=True,blank=False)
    IssuedBooks=models.IntegerField(help_text='BooksIssued',null=True)

   
    
    def __str__(self):
        return self.Studentname
     
    
 
