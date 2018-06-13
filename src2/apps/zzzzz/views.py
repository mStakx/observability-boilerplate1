# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.zzzzz.models import TestModel
import requests

# Create your views here.
def test_view(request):
    test_var = TestModel.objects.count()

    MAX_RETRIES = 20
    url ='http://127.0.0.1:8000/test_view'
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    r = session.get(url)
    print(r.content)

    return render(request, 'zzzzz/test_template.html', {
        "test_var": test_var,
    })
