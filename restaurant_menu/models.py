from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads","Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
             )

STATUS = (
    (0,"Unavailable"),
    (1, "Available")
)

ORDER_STATUS = (
    ("pending", "Pending"),
    ("processing", "Processing"),
    ("shipping", "Shipping"),
    ("delivered", "Delivered"),
    ("Cancelled", "Cancelled")
)
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    meal_type = models.CharField(max_length=200,choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.meal
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Item, through='OrderItem')
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default="pending")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Order #{self.id} for {self.customer.username}"
    
    def caculate_total(self):
        total = 0
        for order_item in self.orderitem_set.all():
            total += order_item.item.price * order_item.quantity
            self.total_price = total
            self.total_price.save()
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.item.meal} in Order {self.order.id} "