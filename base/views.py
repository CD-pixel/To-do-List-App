from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import TodoList
from django.http import JsonResponse

def toggle_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoList, id=todo_id, user=request.user)
        todo.completed = not todo.completed  # Toggle the completed status
        todo.save()
        return JsonResponse({'status': 'success', 'completed': todo.completed})
    return JsonResponse({'status': 'error'}, status=400)


@login_required
def home(request):
    user=User()
    todolist = TodoList.objects.filter(user=request.user)
    context={'user':user, 'todolist':todolist}
    return render(request, "index.html", context)


def deleteTodo(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    if request.method =='POST':
        todo.delete()

        return redirect("home")
    return render(request, "home.html")

def addTodo(request):
    if request.method == 'POST':
        todo = request.POST.get('todo')
        todo_add = TodoList(todo=todo, user=request.user)
        todo_add.save()
        return redirect("home")
    return render(request, "add-todo.html")



def loginUser(request):

    page ="login"
    err_msg =""

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            err_msg = "Incorrect username or password"


            context={"err_msg":err_msg, "page":page}
            return render(request, "login.html", context)

    return render(request, "login.html")




def signupUser(request):

    err_msg =""

    if request.method =='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            form = User.objects.create_user(username=username, password=password1)
            form.save()
            return redirect("home")
        else:
            err_msg = "Password does not match"
    else:
        form = User()

    context={"err_msg":err_msg}

    return render(request, "signup.html")



def logoutUser(request):
    logout(request)
    return redirect("login")