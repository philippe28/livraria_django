from django.contrib import admin
from livro.models import livro

# Register your models here.

class livroadmin(admin.ModelAdmin):
	"""docstring for livroadmin"""
	list_display = ('titulo', 'descricao', 'status', 'nome','email')

admin.site.register(livro,livroadmin)
		