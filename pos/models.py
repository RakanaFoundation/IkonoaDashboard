from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pos.financemodels import Spending
from pos.promotionmodels import Promotion
import datetime

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICE = sorted([(item[1][0]), item[0]] for item in LEXERS)
STYLE_CHOICE = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICE, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICE,
                             default='friendly', max_length=100)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE, default='')
    highlighted = models.TextField(default='')

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']

class Supplier(models.Model):
    address = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Faktur(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.DO_NOTHING,
        unique=False
    )

    spending = models.OneToOneField(
        Spending,
        on_delete=models.CASCADE
    )

    date = models.DateTimeField(auto_now_add=True)

class MainCategory(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class SubCategoryOne(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class SubCategoryTwo(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class Product(models.Model):
    description = models.CharField(max_length=200)
    hargaBeli = models.DecimalField(max_digits=9, decimal_places=2)
    hargaJual = models.DecimalField(max_digits=9, decimal_places=2)
    barcode = models.CharField(max_length=200)
    returnable = models.BooleanField(default=False)

    promotions = models.ForeignKey(
        Promotion,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        unique=False
    )

    mainCategory = models.ForeignKey(
        MainCategory,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        unique=False
    )

    subCategoryOne = models.ForeignKey(
        SubCategoryOne,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        unique=False
    )

    subCategoryTwo = models.ForeignKey(
        SubCategoryTwo,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        unique=False
    )
    
    def __str__(self):
        return self.description

class ProductFaktur(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        unique=False
    )
    faktur = models.ForeignKey(
        Faktur,
        on_delete=models.DO_NOTHING,
        unique=False
    )
    quantity = models.IntegerField(default=1)
    detail = models.CharField(max_length=200, blank=True, null=True)


