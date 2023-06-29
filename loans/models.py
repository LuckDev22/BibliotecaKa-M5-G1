from django.db import models


# Create your models here.
class Loan(models.Model):
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField()
    copy = models.ForeignKey("copies.Copy", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
