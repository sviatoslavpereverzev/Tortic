from django.db import models
from django.utils.safestring import mark_safe


class Slides(models.Model):
    class Meta:
        verbose_name_plural = 'Slides'
        verbose_name = 'Slide'

    title = models.CharField('Title', max_length=25)
    desc = models.TextField('Description', max_length=500)
    image = models.ImageField('Slide image')
    new = models.BooleanField('New', default=False)
    order = models.PositiveIntegerField('Output order')
    show = models.BooleanField('Show or not', default=True)

    def __str__(self):
        return self.title

    def get_icon(self):
        return mark_safe(f'<img  src="{self.image.url}" width="50px" height="50px"')


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    category = models.CharField('Category', max_length=25)
    image = models.ImageField('Image category')
    link = models.CharField('Link', default='', max_length=255)
    order = models.PositiveIntegerField('Output order', default='')

    def __str__(self):
        return self.category

    def get_icon(self):
        return mark_safe(f'<img  src="{self.image.url}" width="50px" height="50px"')


class Cake(models.Model):
    class Meta:
        verbose_name_plural = 'Cakes'
        verbose_name = 'Cake'

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField('Name', max_length=50, blank=True)
    image = models.ImageField('Image', blank=True, null=True)
    date = models.DateTimeField('Date', auto_now=True)

    def __str__(self):
        return self.name

    def get_icon(self):
        return mark_safe(f'<img  src="{self.image.url}" width="50px" height="50px"')


class Reviews(models.Model):
    class Meta:
        verbose_name_plural = 'Reviews'
        verbose_name = 'Review'

    client = models.CharField('Name client', max_length=25)
    review = models.TextField('Review', max_length=500)
    icon = models.ImageField('User icon')
    order = models.PositiveIntegerField('Output order')

    def __str__(self):
        return self.client

    def get_icon(self):
        return mark_safe(f'<img  src="{self.icon.url}" width="50px" height="50px"')

    def cut_review(self):
        return self.review[:50] + '...'


class Stuffing(models.Model):
    class Meta:
        verbose_name_plural = 'Stuffing'
        verbose_name = 'Stuffing'

    name = models.CharField('Stuffing', max_length=255, default='')
    desc = models.TextField('About stuffing', max_length=500)
    image = models.ImageField('Image stuffing')
    order = models.PositiveIntegerField('Output order')

    def __str__(self):
        return self.name

    def get_icon(self):
        return mark_safe(f'<img  src="{self.image.url}" width="50px" height="50px"')


