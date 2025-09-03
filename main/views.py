from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406355621',
        'name': 'Tirta Rendy Siahaan',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)