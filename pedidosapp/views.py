from django.shortcuts import render
from django.http import HttpResponse
#from django.forms.forms import Form
from .forms import PedidoForm
from .models import Pedido

# Create your views here.
def index(request):
    #return HttpResponse("<h1> aqui e o index<h1>")
    return render(request, 'pedidos/index.html')

def pedidos(request):
    #return HttpResponse("<h1>Aqui é a área de hospitais</h1>")
    #pedidos = Pedido.objects.all()
   # busca = request.GET.get('search')
   # if busca:
    	#pedidos = pedido.objects.filter(nome_pedido__icontains =busca)
    return render(request, 'pedidos/vendas.html',{'pedidos':pedidos})


def criar_pedido (request):
	form = PedidoForm()
	if request.method == "POST":
		form = PedidoForm(request.POST, request.FILES)
		if form.is_valid():
			vend = form.save()
			vend.save()
			form =PedidoForm()
	return render(request, 'pedidos/criar_pedido.html',{'form':form})

def clientes(request):
    #return HttpResponse("<h1> aqui e o index<h1>")
    return render(request, 'pedidos/clientes.html')
