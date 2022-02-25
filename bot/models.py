from django.db import models
import json
from urllib.request import urlopen
from urllib.error import HTTPError
import time
from urllib.parse import urlsplit, parse_qs, urlencode
start_time = time.time()


class Bb(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    id_ogr = models.IntegerField(null=True, verbose_name='id организации')
    inn = models.IntegerField(null=True, verbose_name='инн организации')
    actual_year = models.IntegerField(null=True, verbose_name='актуальный год')##Task
    url_pars = models.URLField(null=True, max_length=200, verbose_name='урл_для парсинга')
    publishDate = models.IntegerField(null=True, verbose_name='время публикации')
    url_doc = models.URLField(max_length=200, null=True, verbose_name='Ссылка на актуальный документ')
    update_status = models.CharField(max_length=200, null=True, verbose_name='состояние обновления')

    objects = models.Manager()
    def __str__(self):
        return self.name
class Inquiry:##Парсим запрос
    def __init__(self, start_url):
        self.start_url = start_url
    def get_start_url(self):
        return self.start_url
    def InquiryPrs(self):
        query = urlsplit(self.start_url).query
        params = parse_qs(query)
        for key, val in params.items():##Делаем словарь из части запроса
            if len(val) == 1:
                params[key] = val[0]
        return params





