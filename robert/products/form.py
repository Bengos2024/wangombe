from django import forms

class ProductForm(forms.Form):
    code=forms.IntegerField(label='ID')
    name=forms.CharField(label='NAME')
    price=forms.FloatField(label='PRICE')
    stock=forms.IntegerField(label='STOCK')
    image_url=forms.CharField(label='IMAGE_URL')