from django.shortcuts import render

# Create your views here.

# Root route: to show the form
def index(request):
    return render(request, 'survey/index.html') # route to show the survey form

# /result route: after submitting the form data from the user
def result(request):
    if request.method == "POST":
        # Accessing POST data from the form
        name = request.POST.get('name') # get 'name' field
        dojo_location = request.POST.get('dojo_location')
        favorite_language = request.POST.get('favorite_language')
        comments = request.POST.get('comments')
    
        # Passing the data to the template
        context = {
            'name': name,
            'dojo_location': dojo_location,
            'favorite_language': favorite_language,
            'comments': comments
        }
        return render(request, 'survey/result.html', context)
    else:
        # If the user hasn't put anithing it goes to /result POST, redirect to form after it immediately
        return render(request, 'survey/index.html')
