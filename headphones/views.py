from django.shortcuts import render
from django.views.generic import View

import firebase_admin

from firebase_admin import credentials
from firebase_admin import db


# Create your views here.

cred = credentials.Certificate(
    "./awesomeproject1-28179-firebase-adminsdk-saqao-14123d1cc7.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://awesomeproject1-28179-default-rtdb.firebaseio.com/'
})


class Headphones(View):
    template_name = "index.html"

    ref = db .reference('Headphones')

    data = ref.get()

    def get(self, request):
        return render(request, self.template_name, {"headphones": self.data})


class Phones(View):
    template_name = "phones.html"

    ref = db .reference('Phones')

    data = ref.get()

    def get(self, request):
        return render(request, self.template_name, {"phones": self.data})
