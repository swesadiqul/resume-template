from django.shortcuts import render, HttpResponse, redirect
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('my_app/index.html') # getting our template  
    context = {
      "fullName": "Al Amin",
      "age": 26,
      "destination": "Software Engineer"
    }
    return HttpResponse(template.render({'list_item': context}))       # rendering the template in HttpResponse  
    # return render(request, 'my_app/index.html')


def contact(request):
  if request.method == "POST":
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    print(first_name)
    print(last_name)
    print(email)
    print(message)
  # else:
  #   return redirect('contact')

  return render(request, 'my_app/contact.html')


def services(request):
   return render(request, 'my_app/service.html')


