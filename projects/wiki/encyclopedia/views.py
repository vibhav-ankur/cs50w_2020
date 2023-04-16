from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
import markdown2

def index(request):
    """
    We may also include search function within index 
    # if there is an entry in search bar
    if 'q' in request.GET and request.GET['q'] != "" :
        return search(request)
    else:
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
        
def entry(request, title):
    
    if util.get_entry(title) is None:
        return HttpResponse(f"Error : Page not found")
    else:   
        tempHtml = markdown2.markdown(util.get_entry(title))
        #return HttpResponse(f"{tempHtml}")
        return render(request, 'encyclopedia/entry.html', {"entry": tempHtml, "title": title})
        
def search(request):
    # if there is an entry in search bar
    if 'q' in request.GET and request.GET['q'] != "" :
        subs = request.GET['q']
        if util.get_entry(subs) is not None:
            #return entry(request, subs)
            return HttpResponseRedirect(reverse('entry', args=(subs,)))
        else:
            saved_list = util.list_entries()
            search_list = list(filter(lambda f_name: subs in f_name, saved_list))
            #if search_list is None:
            if search_list == []:
                return render(request, 'encyclopedia/search.html', {"message": "There is no page saved for this query"})
            return render(request, 'encyclopedia/search.html', {"entries": search_list})
    else:
        return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

def md_entry(request, title):
    if request.method == "POST":
        content = request.POST['md_content']
        util.save_entry(title, content)
        #return entry(request, title)
        return HttpResponseRedirect(reverse('entry', args=(title,)))
    else:
        md_content = util.get_entry(title)
        return render(request, 'encyclopedia/md_entry.html', {"md_content": md_content, "title": title})
        
def new_page(request):
    if request.method == "POST":
        content = request.POST['new_content']
        title = request.POST['title']
        if util.get_entry(title) is None:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('entry', args=(title,)))
        else:
            return render(request, 'encyclopedia/new_page.html', {"message": "Error : Page with this title already exists"}) 
            #return HttpResponseRedirect(reverse('new_page'))
    else:
        return render(request, 'encyclopedia/new_page.html')