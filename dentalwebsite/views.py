from django.shortcuts import render

# Create views here:
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        return render(request, 'contact.html', {
            'message_name': message_name,
            'message_email': message_email,
            'message': message
        })

    else:
        # return the page:
        return render(request, 'contact.html', {})