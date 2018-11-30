from django.shortcuts import render,redirect,HttpResponse


def first(request,):

    if request.method == "GET":

        return render(request, "first_task.html")
