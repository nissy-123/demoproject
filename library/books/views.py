from django.shortcuts import render
from books.models import Book
from django.contrib.auth.decorators import login_required

#home
def home(request):
    return render(request,'home.html')

#addbooks
@login_required
def addbooks(request):
    if(request.method=="POST"): #after submitting form
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        l=request.POST['l']
        pa=request.POST['pa']
        c=request.FILES['c']
        f=request.FILES['f']
        b=Book.objects.create(title=t,author=a,price=p,language=l,pages=pa,cover=c,pdf=f) #create a new record
        b.save() #save inside the table book
        return view(request)


    return render(request,'add.html')

@login_required
#viewbooks
def view(request):
    k=Book.objects.all() #reads all records from table Book
    context={'book':k}   # passes data from views to html file.context is dictionary type.
    return render(request,'view.html',context)
def detail(request):
    return render(request,'detail.html')
def edit(request):
    return render(request,'edit.html'),

from django.db.models import Q
def search(request):
    b=None   # initialised to none ...if there is no query then automatically non
    query=""
    if (request.method == "POST"):  # after form submission
        query=request.POST['q']
        if query:
            b = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))


    return render(request, 'search.html',{'books':b,'query':query})
