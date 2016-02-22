from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from livro.models import livro
from livro.forms import livroform
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict



# Create your views here.

def index(request):

	livro_list= livro.objects.all()
	livro_form= livroform()

	return render(request,'livro.html',{'livro_list':livro_list,'livro_form':livro_form})

def save(request):

	livro_form = livroform(request.POST or None)

	if livro_form.is_valid():

		form_clean = livro_form.cleaned_data

		pk = form_clean.get('id', None)

		if not pk:
			livro_model = livro(**form_clean)
			livro_model.save()
		else:
			livro_model = get_object_or_404(livro, pk=pk)

			livro_model.titulo = form_clean.get('titulo', '')
			livro_model.descricao = form_clean.get('descricao', '')
			livro_model.status = form_clean.get('status', '')
			livro_model.nome = form_clean.get('nome', '')
			livro_model.email = form_clean.get('email', '')
			
			livro_model.save()

		return HttpResponseRedirect(reverse('index'))

	livro_list = livro.objects.all()

	return render(request, 'livro.html', {'livro_list': livro_list, 'livro_form': livro_form})


def edit(request, livro_id):
	
	livro_list = livro.objects.all()

	livro_dict = model_to_dict(get_object_or_404(livro, pk=livro_id))

	livro_form = livroform(initial=livro_dict)

	return render(request, 'livro.html', {'livro_list': livro_list, 'livro_form': livro_form})
	

def remove(request, livro_id):

	livro_list = get_object_or_404(livro, pk=livro_id)

	livro_list.delete()

	livro_form = livroform()

	livro_list = livro.objects.all()

	return render(request, 'livro.html', {'livro_list': livro_list, 'livro_form': livro_form})