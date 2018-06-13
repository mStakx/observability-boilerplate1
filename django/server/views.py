from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# import opentracing
import requests
from py_zipkin.zipkin import zipkin_span

# Create your views here.

def http_transport(encoded_span):
    # The collector expects a thrift-encoded list of spans. Instead of
    # decoding and re-encoding the already thrift-encoded message, we can just
    # add header bytes that specify that what follows is a list of length 1.
    body = encoded_span
    # body = '\x0c\x00\x00\x00\x01' + encoded_span
    print(body)
    requests.post(
        'http://zipkin:9411/api/v1/spans',
        data=body,
        headers={'Content-Type': 'application/x-thrift'},
    )

def server_index(request):
    return HttpResponse("Hello, world. You're at the server index.")

def server_simple(request):
    try:
        return HttpResponse("This is a simple traced request.")
    except Exception as e:
        print(e)

def server_log(request):
    # span = settings.OPENTRACING_TRACER.get_span(request)
    # if span is not None:
    #     span.log_event("Hello, world!")
    return HttpResponse("Something was logged")

def server_child_span(request):
    # span = settings.OPENTRACING_TRACER.get_span(request)
    # if span is not None:
    #     child_span = settings.OPENTRACING_TRACER._tracer.start_span("child span", child_of=span.context)
    #     child_span.finish()
    return HttpResponse("A child span was created")
