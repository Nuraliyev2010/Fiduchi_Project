from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone  = models.CharField(max_length=13, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name="Turkum nomi :")


    def __str__(self):
        return self.name


class Home_At_your_department(models.Model):
    title = models.CharField(max_length=25, verbose_name="Bo`lim yaratishdagi sarlavha(Masalan:Siz uchun bizning bo`limimiz):")

    def __str__(self):
        return self.title



class Department(models.Model):
    title = models.CharField(max_length=25, verbose_name="Bo`lim uchun  nom (Masalan: Erkaklar bo`limi):")
    text = models.TextField(verbose_name="Bo`limning tasninfi:")
    img = models.ImageField(upload_to="department_img/", verbose_name="Bo`lim uchun rasm :")
    title1= models.CharField(max_length=255, verbose_name="Bo`lim uchun rasmni ustidagi sarlavhasi :")
    is_right = models.BooleanField(default=False)
    is_left = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Home_Connection1(models.Model):
    title = models.CharField(max_length=25, verbose_name="Bog`lanish uchun  nom (Masalan: Connection):")

    def __str__(self):
        return self.title



class Home_Connection2(models.Model):
    title = models.CharField(max_length=25, verbose_name="Bo`g`lanish uchun sarlavha(Masalan: Address):")
    information = models.CharField(max_length=55, verbose_name="Bog`lanish uchun manzil(Masalan: Telefon nomer):")


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name="Maxsulot nomi :")
    photo =  models.ImageField(upload_to="product_photo/", verbose_name="Maxsulot rasmini kiriting :")
    color = models.CharField(max_length=25, verbose_name="Maxsulot rangini kiriting :")
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    discount = models.IntegerField(default=0, null=True, blank=True)
    size = models.ForeignKey(to='Size', on_delete=models.CASCADE)
    tags = models.ManyToManyField(to='Tag', blank=True)
    describtion = models.CharField(max_length=50, verbose_name='Tasvirlash :', null=True, blank=True)
    sub_category = models.ForeignKey(to="Sub_Category", on_delete=models.PROTECT)
    status_department = models.ForeignKey(to=Department, on_delete=models.PROTECT)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(to=Product, on_delete=models.CASCADE)

class Save(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(to=Product, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Maxsulot categorysi(Masalan:Mens` salamandr) :')

    def __str__(self):
        return self.name


class Size(models.Model):
    number = models.IntegerField(verbose_name='Maxsulotlar (obshiy) o`lchamlarini kiriting ')