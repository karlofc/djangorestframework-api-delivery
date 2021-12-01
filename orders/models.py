from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Order(models.Model):
    SIZES = (
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large'),
        ('EXTRA_LARGE', 'Extra Large')
    )

    ORDER_STATUS = (
        ('PENDING', 'Pending'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered')
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=SIZES, default=SIZES[0][0])
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"<Order {self.size} by {self.customer.id}"