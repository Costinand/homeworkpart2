from django.db import models

class User(models.Model):

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=28, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Goods(models.Model):

    product_id = models.IntegerField(primary_key=True, default=0)
    product_name = models.CharField(max_length=100)
    category = models.IntegerField()
    price = models.IntegerField(null=True)

    class Meta:
        db_table = 'goods'

    def __str__(self):
        return self.product_name


class Delivery(models.Model):

    parcel_id = models.IntegerField(primary_key=True, default=0)
    customer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'delivery'

    def __str__(self):
        return self.customer



