from django.shortcuts import render,redirect

from todoapp.models import TodoModel

def home(request):
    content=TodoModel.objects.all()
    dic={'content':content}
    return render(request,'home.html',dic)


def addtodo(request):
    if request.method=='POST':
        name= request.POST['name']
        text=request.POST['text']

        content=TodoModel(name=name,text=text)
        content.save()
    return redirect('/todo/home')

def deletetodo(request,id):
    item=TodoModel.objects.get(id=id)
    item.delete()
    
    return redirect('/todo/home/')