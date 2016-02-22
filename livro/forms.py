from django import forms


class livroform(forms.Form):
     
     id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

     titulo = forms.CharField(label='Título', max_length=100)
     
     descricao = forms.CharField(
     	widget=forms.Textarea(attrs={'rows': '4'}), 
     	label='Descrição', 
     	max_length=500, 
     	required=False
     )
     
     status = forms.BooleanField(label='Emprestado', required=False)
     
     nome = forms.CharField(label='Amigo', max_length=100, required=False)
     
     email = forms.EmailField(label='E-mail', max_length=50, required=False)