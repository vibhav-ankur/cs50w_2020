from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# tasks is global variable, entire application can have access to it
#tasks = ["read", "work", "play"]
#tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    priority = forms.IntegerField(label= "Priority", min_value=1, max_value=10)
    
def index(request):

    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    #return render(request, 'tasks/index.html', {"tasks": tasks})
    return render(request, 'tasks/index.html', {"tasks": request.session["tasks"]})

"""    
    def add(request):
        return render(request, 'tasks/add.html')
"""
def add(request):

    # check if request method is POST
    if request.method == "POST":
    
        # take in data the user submitted & save it as form 
        form = NewTaskForm(request.POST)
        """ NewTaskForm() creates an empty form request.POST contains all data user
            submitted so NewTaskForm(request.POST) is the NewTaskForm that contains 
            all data submitted by user
        """
        
        # check if form is valid(server-side)
        if form.is_valid():
        
            """ form.cleaned_data to get access to all data the user submitted
                Isolate the task from the 'cleaned' version of form data
            """

            task = form.cleaned_data["task"]
            
            # add new task to our list of tasks
            #tasks.append(task)
            request.session["tasks"] += [task]
            
            # redirect user to list of tasks
            #return HttpResponseRedirect('/tasks')
            return HttpResponseRedirect(reverse("tasks:index"))
        
        else:
            
            """ if form is invalid, rerender the page with existing information and 
            user will also be able to see the errors made
            """
            return render(request, 'tasks/add.html', {"form": form})
    
    # when user tries to GET the page with empty form rather than submitting data to it
    return render(request, 'tasks/add.html', {"form": NewTaskForm()})