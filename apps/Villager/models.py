from django.db import models


class Villager(models.Model):
    PACKAGE_CHOICE = (
        ('anc', 'Anti Natal Check UP'),
        ('ahp', 'Adult Health Package'),
        ('adc', 'After Delivery Check Up'),
    )

    GENDER_CHOICE = (
        ('m', "MALE"),
        ('f', "FEMALE"),
    )

    image = models.ImageField(upload_to='images/villager/profile_pic/')
    name = models.CharField(max_length=255)
    reg_no = models.CharField(max_length=30, unique=True, verbose_name='Registration Number')
    phone = models.CharField(max_length=15)
    nid = models.CharField(max_length=40, unique=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    date_of_birth = models.DateField()
    package = models.CharField(max_length=3, choices=PACKAGE_CHOICE)

    follow_up_date = models.DateField(auto_now_add=True)
    next_follow_up_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Remark(models.Model):
    villager = models.ForeignKey(Villager, on_delete=models.CASCADE, blank=True)
    date = models.DateField(auto_now_add=True)
    remark = models.TextField(max_length=1000)

    class Meta:
        ordering = ['-id', ]

    def __str__(self):
        return self.remark
