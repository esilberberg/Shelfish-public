from django.db import models
from django.urls import reverse

# Create your models here.
class Classification(models.Model):
    """Model representing the language of a text."""
    term = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.term

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('classification-detail-view', args=[str(self.id)])

class Language(models.Model):
    """Model representing the language of a text."""
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('language-detail-view', args=[str(self.id)])

class Book(models.Model):
    """Model representing a physical book."""
    title = models.CharField(max_length=200)
    pub_year = models.CharField(max_length=4, blank=True)
    publisher = models.CharField(max_length=200, blank=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    cover_url = models.URLField(max_length=200, blank=True)
    summary = models.TextField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ManyToManyField(Language, blank=True)
    classification = models.ManyToManyField(Classification, blank=True)

    LOCATIONS = (
        ('PR', 'Processing'),
        ('AS', 'Astoria'),
        ('QC', 'Queens College'),
        ('SC', 'Scarsdale'),
        ('BW', 'Bushwick'),
        ('OL', 'On Loan'),
        ('XX', 'Deaccessioned'),
    )

    location = models.CharField(
        max_length=2,
        choices=LOCATIONS,
        blank=True,
        default='PR',
    )

    class Meta:
        ordering = ['date_created']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('book-detail-view', args=[str(self.id)])

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200)
    birth_year = models.CharField(max_length=4, blank=True)
    death_year = models.CharField(max_length=4, blank=True)

    class Meta:
        ordering = ['surname', 'first_name']
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.surname}, {self.first_name}'

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('author-detail-view', args=[str(self.id)])