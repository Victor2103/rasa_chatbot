from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

import requests

# Create your views here.


def index(request):
    return render(request, template_name='index.html')


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        url = "https://a26c825a-9b57-495a-b0fd-415e0452e47f.app.gra.training.ai.cloud.ovh.net/webhooks/rest/webhook"
        data = form.cleaned_data
        json_data = {"sender": data['user'], "message": data["message"]}
        data = requests.post(url=url, json=json_data, headers={
                                                      "Authorization": "Bearer ++9O7ZjOT8eEkAha1GywfOFQXnJvttgYXbmdBOxLS7sW/s4TqtdNJBVMqRav+vzO", "Content-Type": "application/json"})
        print(data.text)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('discuss')
