from django.db import models
from django.contrib.postgres.fields import ArrayField

from datetime import datetime

from bot_admin import enums
from bot_admin import maps as mp
from delivery_club.settings import DAY_FORM


# пользователи
class UserTable(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True, choices=mp.user_status)
    name = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True, choices=mp.company)
    phone = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'
        managed = False


# заказы
class OrderTable(models.Model):
    id = models.AutoField(primary_key=True)
    b = models.CharField(max_length=255, null=True, blank=True)
    c = models.CharField(max_length=255, null=True, blank=True)
    d = models.CharField(max_length=255, null=True, blank=True)
    e = models.CharField(max_length=255, default=datetime.now().strftime(DAY_FORM), null=True, blank=True)
    f = models.CharField(max_length=255, null=True, blank=True, choices=mp.dlvs)
    g = models.CharField(max_length=255, choices=mp.order_status, default='new')
    h = models.CharField(max_length=255, null=True, blank=True)
    i = models.CharField(max_length=255, null=True, blank=True)
    j = models.CharField(max_length=255, null=True, blank=True)
    k = models.CharField(max_length=255, null=True, blank=True)
    l = models.CharField(max_length=255, null=True, blank=True)
    m = models.TextField(null=True, blank=True)
    n = models.CharField(max_length=255, null=True, blank=True)
    o = models.CharField(max_length=255, null=True, blank=True)
    p = models.TextField(null=True, blank=True)
    q = models.IntegerField()
    r = models.IntegerField()
    s = models.IntegerField()
    clmn_t = models.IntegerField('T')
    u = models.IntegerField()
    v = models.IntegerField()
    w = models.CharField(max_length=255, null=True, blank=True)
    x = models.TextField(null=True, blank=True)
    y = models.IntegerField()
    z = models.CharField(max_length=255, null=True, blank=True)
    aa = models.CharField(max_length=255, null=True, blank=True)
    ab = models.CharField(max_length=255, null=True, blank=True)
    ac = models.CharField(max_length=255, null=True, blank=True)
    ad = models.CharField(max_length=255, null=True, blank=True)
    ae = models.CharField(max_length=255, null=True, blank=True)
    af = models.CharField(max_length=255, null=True, blank=True)
    ag = models.CharField(max_length=255, null=True, blank=True)
    ah = models.CharField(max_length=255, null=True, blank=True)
    updated = models.BooleanField('Обновлено', default=False)
    time_update = models.DateTimeField(auto_now_add=True)
    type_update = models.CharField('Тип обновления', max_length=255, default=enums.TypeOrderUpdate.ADD.value)
    discount = models.IntegerField('Скидка', default=0)
    row_num = models.IntegerField('Строка')

    def __str__(self):
        return f'Заказ {self.row_num}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'orders_ggl'
        managed = False


# заказы
class WorkOrders(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    order_id = models.IntegerField()

    def __str__(self):
        return f'Заказ {self.order_id}'

    class Meta:
        verbose_name = 'Заказы в работе'
        verbose_name_plural = 'Заказы в работе'
        db_table = 'work_orders'
        managed = False


# отчёты
class ReportTable(models.Model):
    id = models.AutoField(primary_key=True)
    b = models.IntegerField(default=0)
    c = models.IntegerField(default=0)
    d = models.IntegerField(default=0)
    e = models.IntegerField(default=0)
    f = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    h = models.IntegerField(default=0)
    i = models.IntegerField(default=0)
    j = models.IntegerField(default=0)
    k = models.IntegerField(default=0)
    l = ArrayField(base_field=models.CharField(max_length=255), null=True, blank=True)
    m = models.TextField(null=True, blank=True)
    n = models.CharField(max_length=255, null=True, blank=True)
    o = models.IntegerField()
    p = models.CharField(max_length=255, null=True, blank=True)
    q = models.CharField(max_length=255, null=True, blank=True)
    r = models.IntegerField()
    in_google = models.BooleanField(default=False)
    row_num = models.IntegerField()
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Отчёт {self.row_num}'

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'
        db_table = 'report_ggl'
        managed = False


# действия пользователей
class ActionJournal(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(null=True, blank=True)
    user_id = models.BigIntegerField(null=True, blank=True)
    dlv_name = models.CharField(max_length=100, null=True, blank=True)
    action = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Журнал действий'
        verbose_name_plural = 'Журнал действий'
        db_table = 'action_journal'
        managed = False


# журнал ошибок
class ErrorsJournal(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.BigIntegerField()
    error = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.error

    class Meta:
        verbose_name = 'Журнал ошибок'
        verbose_name_plural = 'Журнал ошибок'
        db_table = 'errors_journal'
        managed = False
