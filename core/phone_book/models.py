from django.db import models
from django.urls import reverse

class Work_place(models.Model):
    country = models.CharField(max_length=50)
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.country} - {self.company_name}'

class Email(models.Model):
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.email}'


class Phone_book(models.Model):
    country_codes = [
        ('+380', 'Ukraine'),
        ('+44', 'Great Britain'),
        ('+49', 'Germany'),
        ('+48', 'Poland'),
    ]

    name = models.CharField('Name', max_length=200)
    value = models.PositiveBigIntegerField('Phone number')
    country_code = models.CharField(
        'Country code', 
        max_length=10, 
        choices=country_codes, 
        blank=True
        )
    work_info = models.ManyToManyField(Work_place)
    email = models.ForeignKey(
        Email, 
        on_delete=models.SET_NULL, 
        blank=True, null=True,
    )

    def get_absolute_url(self):
        return reverse('show_all', kwargs={'pk' : self.pk})

    def __str__(self):
        return f'{self.name}, {self.country_code} - {self.value}, {self.work_info.all()}'
