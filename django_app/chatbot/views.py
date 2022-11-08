from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import UserConversation
from django.core.signing import Signer
import jwt
import os

import requests

# Create your views here.


def index(request):
    encoded_jwt = jwt.encode({"some":"payload"},os.getenv("SECRET_KEY"),algorithm="HS256")
    return render(request, template_name='index.html',context={"jwebtoken":encoded_jwt})


class ContactFormView(CreateView):
    model=UserConversation
    fields=['name','message']

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        url = "https://a26c825a-9b57-495a-b0fd-415e0452e47f.app.gra.training.ai.cloud.ovh.net/webhooks/rest/webhook"
        data = form.save()
        json_data = {"sender": data['user'], "message": data["message"]}
        data = requests.post(url=url, json=json_data, headers={
            "Authorization": "Bearer ++9O7ZjOT8eEkAha1GywfOFQXnJvttgYXbmdBOxLS7sW/s4TqtdNJBVMqRav+vzO", "Content-Type": "application/json"})
        print(data.text)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('discuss')
