from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Dupe(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('dupes_detail', kwargs={'pk': self.id})

class Makeup(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description =  models.TextField(max_length=300)
    price = models.IntegerField()
    dupes = models.ManyToManyField(Dupe)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'makeup_id': self.id})


RATINGS = (
    ('0', '☆☆☆☆☆'),
    ('1', '★☆☆☆☆'),
    ('2', '★★☆☆☆'),
    ('3', '★★★☆☆'),
    ('4', '★★★★☆'),
    ('5', '★★★★★')
)

class Reviews(models.Model):
    date = models.DateField('review date')
    review = models.CharField(max_length=100)
    rating = models.CharField(max_length=6 , choices=RATINGS, default=RATINGS[0][0])

    # Create a makeup_id FK
    makeup = models.ForeignKey(Makeup, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_rating_display()} on {self.date}"

     # change the default sort
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    makeup = models.ForeignKey(Makeup, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for makeup_id: {self.cat_id} @{self.url}"







