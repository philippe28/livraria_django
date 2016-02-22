from django.db import models

# Create your models here.



class livro(models.Model):
	"""docstring for livraria"""
	titulo = models.CharField(max_length=100)
	descricao = models.TextField(blank=True,default='')
	status = models.BooleanField(default=False)
	nome = models.CharField(max_length=100,blank=True,default='')
	email = models.EmailField(max_length=50,blank=True,default='')
	data = models.DateTimeField(auto_now_add=True)	

	class Meta:
		verbose_name = 'Livro'
		verbose_name_plural = 'Livros'		

	def __unicode__(self):
		return self.titulo