from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    phone=models.CharField(max_length=100,unique=True)
    address=models.CharField(max_length=200)

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Cakes(models.Model):
    name=models.CharField(max_length=200)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)

    options=(
        ('choclate','choclate'),
        ('blackforest','blackforest'),
        ('red velvet','red velvet'),
        ('butter scotch','butter scotch'),
        ('vanila','vanila'),
        ('pineapple','pineapple'),
        ('dates','dates'),
        ('non-alcoholic','non-alcoholic'),
        ('dry-fruits','dry-fruits'),
        ('mixed-fruits','mixed-fruits'),
        ('blueberry','blueberry'),
        ('strawberry','strawberry')

    )
    flavour=models.CharField(max_length=200,choices=options,default="choclate")
    image=models.ImageField(upload_to="images")

    @property
    def varients(self):
        qs=self.cakevarients_set.all()
        return qs
    
    @property
    def reviews(self):
        qs=self.reviews_set.all()
        return qs
    
    @property
    def avg_rating(self):
        ratings=self.reviews_set.all().values_list("rating",flat=True)
        return sum(ratings)/len(ratings) if ratings else 0

    
    def __str__(self):
        return self.name
    
class CakeVarients(models.Model):
    price=models.PositiveIntegerField()

    options=(
        (".5kg",".5kg"),
        ("1kg","1kg"),
        ("2kg","2kg"),
        ("5kg","5kg")
    )
    size=models.CharField(max_length=200,choices=options,default="1kg")
    option=(
        ("round","round"),
        ("square","square"),
        ("heart","heart")
    )
    shape=models.CharField(max_length=200,choices=option,default="round")
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)

    def __str__(self):
        return self.cake.name
    
    @property
    def offers(self):
        current_date=date.today()
        qs=self.offers_set.all()
        qs=qs.filter(due_date__gte=current_date)
        return qs



class Offers(models.Model):
    cakevarient=models.ForeignKey(CakeVarients,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateTimeField()

class Carts(models.Model):
    cakevarient=models.ForeignKey(CakeVarients,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)



class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cakevarients=models.ForeignKey(CakeVarients,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatched","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    ordered_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)


from django.core.validators import MinValueValidator,MaxValueValidator

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cakes,null=True,on_delete=models.SET_NULL)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)

