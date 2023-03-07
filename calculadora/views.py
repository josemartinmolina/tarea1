from django.shortcuts import render
from django.http import HttpResponse
from .models import Reto
import sqlite3 

# Create your views here.
def nueva():
    return 0
def index(request):
    #return HttpResponse("Bienvenido")
    return render(request,'index.html')

def procesamiento(request):
    nombre = request.POST['nombre']
    nombre = nombre.title()
    return render(request, 'proceso.html', {'name':nombre})

def lista(request):
    jugadores = Reto.objects.all() #select * from Reto 
    print(jugadores)
    return render(request, 'datos.html',{'lista_jugadores':jugadores})

def score(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    res = cur.execute("SELECT fecha,score FROM score")
    listado = res.fetchall()
    print(listado)
    return HttpResponse(listado)

def usuarios(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM usuarios")
    resultado = res.fetchall()
    lista =[]  
    for registro in resultado:
        id,grupo,grado,numero = registro
        diccionario = {"id":id,"grupo":grupo,"grado":grado,"num_lista":numero}
        lista.append(diccionario)
    registros =[{"id":1,"grupo":"A","grado":6,"num_lista":4},{"id":2,"grupo":"B","grado":6,"num_lista":2}] 
    registros = lista
    return render(request, 'usuarios.html',{'lista_usuarios':registros})
