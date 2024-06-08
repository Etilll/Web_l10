from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Author(models.Model):
    days_table = {}
    months_table = {
        "January":"January",
        "February":"February",
        "March":"March",
        "April":"April",
        "May":"May",
        "June":"June",
        "July":"July",
        "August":"August",
        "September":"September",
        "October":"October",
        "November":"November",
        "December":"December",
                    }
    years_table = {}
    for i in range(1,32):
        if i > 9:
            days_table[str(i)] = i
        else:
            days_table["0" + str(i)] = "0" + str(i)
    for i in range(1,13):
        if i > 9:
            months_table[str(i)] = i
        else:
            months_table["0" + str(i)] = "0" + str(i)
    for i in range(1,2025):
        years_table[str(i)] = i
    
    author_creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    author_name = models.CharField(max_length=50, verbose_name='Name', default="Sample name")
    author_desc = models.CharField(max_length=5000, verbose_name='Description', default="Sample desc")
    author_birth_place = models.CharField(max_length=100, verbose_name='Place of birth', default="Unknown")
    author_birth_day = models.CharField(max_length=2, verbose_name='Birth day', default="-", choices=days_table)
    author_birth_month = models.CharField(max_length=15, verbose_name='Birth month', default="-", choices=months_table)
    author_birth_year = models.CharField(max_length=4, verbose_name='Birth year', default="-", choices=years_table)
    author_death_day = models.CharField(max_length=2, verbose_name='Death day', default="-", choices=days_table, blank=True)
    author_death_month = models.CharField(max_length=15, verbose_name='Death month', default="-", choices=months_table, blank=True)
    author_death_year = models.CharField(max_length=4, verbose_name='Death year', default="-", choices=years_table, blank=True)

    def __str__(self):
        return self.author_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name='Name', default="Sample tag")
    tag_creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.tag_name

class Post(models.Model):
    post_creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_text = models.CharField(max_length=1500, verbose_name='Quote', default="No text was added.")
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_tags = models.ManyToManyField(Tag)
    post_publish_date = models.DateTimeField(default=now, verbose_name='Publish date')

    def __str__(self):
        return f"{self.post_text} -{self.post_author}."