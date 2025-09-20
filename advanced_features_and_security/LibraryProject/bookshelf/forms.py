from django.shortcuts import render, redirect
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            return redirect('success_url')  # Redirect after successful submission
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/example_form.html', {'form': form})
