from django.db import models



class Shawarma(models.Model):
    name = models.CharField(max_length=100)
    kubbos_per_item = models.IntegerField(default=1)  # 1 for roll, 2 for plate
    quantity_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def total_kubbos_used(self):
        return self.kubbos_per_item * self.quantity_sold
