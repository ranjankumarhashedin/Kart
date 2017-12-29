from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .forms import ContactForm


def home_page(request):
    context = {
        "title": "Home",
        "content": "Welcome to the homepage."
    }
    if request.user.is_authenticated():
        context['premium_content'] = 'You are now a member!'
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About",
        "content": "This is the about page."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "This is the contact page.",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your response."})

    if contact_form.errors:     # If contact form has errors
        errors = contact_form.errors.as_json()  # convert to json
        if request.is_ajax():
            # Since data is already in json, we use HttpResponse
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == 'POST':
    #   print(request.POST)
    #   print(request.POST.get('fullname'))
    #   print(request.POST.get('email'))
    #   print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


def home_page_old(request):
    return HttpResponse("<h1>Hello World!</h1>")
