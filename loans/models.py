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
