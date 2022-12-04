from django.db import models

# Create your models here.
class mm_customer(models.Model):
    
    class Meta:
        db_table = 'mm_customer'

    def __str__(self):
        return self.customer_id.customer_id

    customer_id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    segment = models.CharField(max_length=15)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

class mm_address(models.Model):

    class Meta:
        db_table = 'mm_address'

    address_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    add_state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    market = models.CharField(max_length=50)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

class mm_customer_address(models.Model):

    class Meta:
        db_table = 'mm_customer_address'
        unique_together = (('address_id', 'customer_id'),)

    address_id = models.ForeignKey(mm_address, related_name="customer_to_address", on_delete=models.DO_NOTHING, db_column= 'address_id')
    customer_id = models.ForeignKey(mm_customer, related_name="address_to_customer", on_delete=models.DO_NOTHING, db_column= 'customer_id')
    add_state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=12)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

class mm_product_category(models.Model):

    class Meta:
        db_table = 'mm_product_category'

    category_id = models.AutoField(primary_key=True) 
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

class mm_product(models.Model):

    class Meta:
        db_table = 'mm_product'

    product_id = models.CharField(primary_key=True, max_length=20)
    category_id = models.ForeignKey(mm_product_category, related_name="product_to_category", on_delete=models.DO_NOTHING, db_column= 'category_id')
    product_name = models.CharField(max_length=150)
    mrp = models.DecimalField(max_digits=5, decimal_places=2)
    manu_cost = models.DecimalField(max_digits=5, decimal_places=2)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True) 

class mm_order(models.Model):

    class Meta:
        db_table = 'mm_order'

    order_id = models.CharField(primary_key=True, max_length=50)
    order_date = models.DateField()
    return_status = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    customer_id = models.ForeignKey(mm_customer, related_name="order_to_customer",on_delete=models.DO_NOTHING, db_column= 'customer_id')

class mm_order_product(models.Model):

    class Meta:
        db_table = 'mm_order_product'
        unique_together = (('order_id', 'product_id'),)

    order_product_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    order_id = models.ForeignKey(mm_order, related_name="item_to_order", on_delete=models.DO_NOTHING, db_column= 'order_id')
    product_id = models.ForeignKey(mm_product, related_name="item_to_product", on_delete=models.DO_NOTHING, db_column= 'product_id')

class mm_shipping_details(models.Model):

    class meta:
        db_table = 'mm_shipping_details'

    ship_id = models.AutoField(primary_key=True)
    priority = models.CharField(max_length=20) 
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=20)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    order_id = models.ForeignKey(mm_order, related_name="ship_to_order", on_delete=models.DO_NOTHING, db_column= 'order_id')
  
