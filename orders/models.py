from django.db import models

class Order(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('PROCESSING','Processing'),
        ('COMPLETED','Completed'),
        ('CANCELED','Canceled')
    ]
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    order_items=models.ForeignKey(Menu)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    order_status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    
    def __str__(self):
        return self.customer.username
