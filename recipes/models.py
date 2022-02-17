from django.db import models


class User(models.Model):
    first_name = models.CharField('First name', max_length=250)
    last_name = models.CharField('Last name', max_length=250)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Recipe(models.Model):
    title = models.CharField('Title', max_length=250)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='images/')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    date = models.DateTimeField('Date', auto_now_add=True)
    view_count = models.PositiveIntegerField('View count', default=0)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return f'{self.title}'
