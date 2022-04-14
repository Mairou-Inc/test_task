from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager




class User(AbstractUser):
    # email = models.EmailField(blank=False, null = False, unique=True)

    timestamp = models.DateTimeField( auto_now_add=True, null=True, verbose_name='Время регистрации' )
    last_visit_datetime = models.DateTimeField(null = True, blank=True, verbose_name='Дата последнего посещения' )



    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
        # ordering = ["last_name", "first_name", "second_name", "registration_date"]

    def __str__(self):
        return f"{self.username}"





class Comment(models.Model):
    article = models.ForeignKey('Article', null = True, blank=True, on_delete=models.CASCADE, verbose_name='Article', related_name='comment' )
    user = models.ForeignKey('User', null = True, blank=True, on_delete=models.CASCADE, verbose_name='User', related_name='user' )
    text = models.TextField(verbose_name="Comments", blank=True, null=True)
    comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replie')
    timestamp = models.DateTimeField( auto_now_add=True, null=True, verbose_name='Время регистрации' )


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        # ordering = ["-weight_by_posters", "-weight_by_users"]
        # ordering = ["name"]


class Article(models.Model):
    user = models.ForeignKey('User', null = True, blank=True, on_delete=models.CASCADE, verbose_name='User', related_name='article_user' )
    name = models.CharField(max_length=255, null = False, blank=False, verbose_name='Name')
    text = models.CharField(max_length=255, null = False, blank=False, verbose_name='Text')
    timestamp = models.DateTimeField( auto_now_add=True, null=True, verbose_name='Время регистрации' )


    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        # ordering = ["-weight_by_posters", "-weight_by_users"]
        # ordering = ["name"]


