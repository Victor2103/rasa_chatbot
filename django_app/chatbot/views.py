from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView

# Create your views here.


def index(request):
    return render(request, template_name='index.html')


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


