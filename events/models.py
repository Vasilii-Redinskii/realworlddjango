from django.db import models
from django.contrib.auth.models import User
from utils.models import places_left


class Category(models.Model):
    title = models.CharField(max_length=90,  # максимальная длина поля
                             default='',  # значение по умолчанию для новых объектов
                             verbose_name='Категория'  # название, выводимое на сайте
                             )

    class Meta:
        verbose_name_plural = 'Категории'  # форма единственного числа
        verbose_name = 'Категория'  # форма множественного числа

    def __str__(self):
        return self.title

    def display_event_count(self):
        return self.events.count()


class Feature(models.Model):
    title = models.CharField(max_length=200,  # максимальная длина поля
                             default='',  # значение по умолчанию для новых объектов
                             verbose_name='Свойство события'  # название, выводимое на сайте
                             )

    class Meta:
        verbose_name_plural = 'Свойства события'  # форма единственного числа
        verbose_name = 'Свойство события'  # форма множественного числа

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200,  # максимальная длина поля
                             default='',  # значение по умолчанию для новых объектов
                             verbose_name='Название'  # название, выводимое на сайте
                             )
    description = models.TextField(default='',  # значение по умолчанию для новых объектов
                                   verbose_name='Описание'  # название, выводимое на сайте
                                   )
    date_start = models.DateTimeField(verbose_name='Дата начала')  # название, выводимое на сайте
    participants_number = models.PositiveSmallIntegerField(
        verbose_name='Количество участников'  # название, выводимое на сайте
    )
    is_private = models.BooleanField(default=False,  # значение по умолчанию для новых объектов
                                     verbose_name='Частное'  # название, выводимое на сайте
                                     )
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='events',verbose_name='Категория')
    features = models.ManyToManyField(Feature, related_name='events')

    def display_enroll_count(self):
        return self.enrolls.count()

    display_enroll_count.short_description = 'Количество записей'

    def display_places_left(self):
        result = f'{self.participants_number-self.display_enroll_count()} ({places_left(self.display_enroll_count(), self.participants_number)})'
        return result

    display_places_left.short_description = 'Осталось мест'

    class Meta:
        ordering = ['date_start']
        verbose_name_plural = 'События'  # форма единственного числа
        verbose_name = 'Событие'  # форма множественного числа

    def __str__(self):
        return self.title


class Enroll(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='enrolls')
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE, related_name='enrolls')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Запись на событие'  # форма единственного числа
        verbose_name = 'Записи на событие'  # форма множественного числа


class Review(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='reviews')
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE, related_name='reviews')
    rate = models.PositiveSmallIntegerField(verbose_name='Оценка пользователя')
    text = models.TextField(verbose_name='Текст отзыва')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Отзыв на событие'  # форма единственного числа
        verbose_name = 'Отзывы на событие'  # форма множественного числа
