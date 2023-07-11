from django.db import models
from datetime import timedelta, datetime
from django.utils import timezone
import pytz
import numpy as np



class Loan(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    copy = models.ForeignKey("copies.Copy", on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(default=timezone.now() + timedelta(days=7))

    def data_retorno(self):
        data_retorno = self.data_emprestimo + timedelta(days=self.data_devolucao)
        if data_retorno.weekday() >= 5:
            data_retorno += timedelta(days=10 - data_retorno.weekday())
        return data_retorno

    def is_overdue(self):
        if isinstance(self.data_devolucao, datetime):
            return self.data_devolucao.date() < timezone.now().date()
        return self.data_devolucao < timezone.now().date()

    def save(self, *args, **kwargs):
        if self.is_overdue() and self.user.is_student and not self.user.is_blocked:
            self.user.is_blocked = True
            self.user.blocked_until = timezone.now().date() + timedelta(days=7)
            self.user.save()
        elif not self.is_overdue() and self.user.is_blocked and self.user.blocked_until is not None:
            if self.user.blocked_until <= timezone.now().date():
                self.user.is_blocked = False
                self.user.blocked_until = None
                self.user.save()
        super().save(*args, **kwargs)

