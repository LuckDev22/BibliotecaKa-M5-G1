from django.db import models
from datetime import timedelta, datetime
import pytz
import numpy as np


# Create your models here.
class Loan(models.Model):
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateField()
    copy = models.ForeignKey("copies.Copy", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)


def adjust_return_date(self):
    if self.data_devolucao.weekday() >= 5:
        self.data_devolucao += timedelta(days=7 - self.data_devolucao.weekday())
    self.data_devolucao = pytz.timezone("America/Sao_Paulo").localize(
        self.data_devolucao
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.adjust_return_date()
        super(Loan, self).save(*args, **kwargs)
