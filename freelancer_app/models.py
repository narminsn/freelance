from django.db import models

# Create your models here.

class MenuModel(models.Model):
    title=models.CharField(max_length=255)
    url=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.title}"

class HeaderModel(models.Model):
    base_title=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    background=models.ImageField(upload_to = 'media/header')

    def __str__(self):
        return self.base_title

class ContactModel(models.Model):
    
    name=models.CharField(max_length=255)
    email = models.EmailField(max_length=70,blank=True)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Contact_sessionModel(models.Model):
    title=models.CharField(max_length=255)
    background=models.ImageField(upload_to = 'media/contact')

    def __str__(self):
        return self.title

class About_session(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    button_text=models.CharField(max_length=100)
    button_url=models.CharField(max_length=255)
    image=models.ImageField(upload_to='portfolio',null=True)

    def __str__(self):
        return self.title
    

class PortfolioModel(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='portfolio',null=True)



    def __str__(self):
        return f"{self.title}"


class PortfolioItem(models.Model):
    image=models.ImageField(upload_to='portfolio_item/')
    title=models.CharField(max_length=255)
    text=models.TextField()
    button_text=models.CharField(max_length=255)
    button_url=models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CopyrightModel(models.Model):
    text=models.CharField(max_length=255)

    def __str__(self):
        return self.text


class FooterModel(models.Model):
    title=models.CharField(max_length=255)
    description1=models.CharField(max_length=400)
    description2=models.CharField(max_length=400)

    def __str__(self):
        return self.title

class FooterIcon(models.Model):
    icon=models.CharField(max_length=255)
    url=models.URLField()
    section=models.ForeignKey('FooterModel', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.icon}'



