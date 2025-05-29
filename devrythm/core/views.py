from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return redirect('landing')
    else:
        return redirect('login')


@login_required
def landing(request):
    # You can render a template called landing.html
    return render(request, 'landing.html')