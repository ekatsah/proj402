from django.shortcuts import redirect, render

def home(request):
    if request.user.is_authenticated():
        return redirect('index')
    return render(request, "layout.tpl")
