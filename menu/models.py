from django.db import models


class Menu(models.Model):
    name = models.CharField('Название меню', max_length=50, unique=True)
    url = models.CharField('Ссылка', max_length=255, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    name = models.CharField('Название пункта меню', max_length=100, unique=True)
    url = models.CharField('Ссылка', max_length=255, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
