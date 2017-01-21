from django.shortcuts import render
from promKalk.forms import PromilleForm

def template_testing(request):
    if request.method == 'POST':
        form = PromilleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            return render(request, 'promKalk_form.html')

    else:
        form = PromilleForm(initial={})
    return render(request, 'promKalk_form.html', {'form': form})
