from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

import logging

# import opentracing
import requests
from py_zipkin.zipkin import zipkin_span, ZipkinAttrs

# import urllib2
import urllib.request
import urllib.error

# from py_zipkin.transport import BaseTransportHandler 

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

def client_index(request):
    
    test_logger = logging.getLogger('django')
    test_logger.setLevel(logging.INFO)
    test_logger.info("Calling client_simple - Info")
    logging.getLogger().info("Calling client_simple - Info")
    print("Info here!!! --> ", logging.getLogger('django'))

    return HttpResponse("Client index page")

# @zipkin_span(service_name='ssm_zipkin', span_name='client_simple')
def client_simple(request):
    zipkin_attrs1 = ZipkinAttrs(
        trace_id='1',
        span_id='1',
        parent_span_id=None,
        flags='0',
        is_sampled=True,
    )
    with zipkin_span(
        zipkin_attrs=zipkin_attrs1,
        service_name='ssmzipkin2',
        span_name='clientsimple1',
        transport_handler=http_transport,
        sample_rate=100, # Value between 0.0 and 100.0
    ) as clientspan:

        url = "http://localhost:8000/server/simple"
        new_request = urllib.request.Request(url)
        # current_span = settings.OPENTRACING_TRACER.get_span(request)
        # inject_as_headers(settings.OPENTRACING_TRACER, current_span, new_request)
        zipkin_attrs = ZipkinAttrs(
            trace_id='1',
            span_id='2',
            parent_span_id='1',
            flags='0',
            is_sampled=True,
        )
        try:
            with zipkin_span(
                zipkin_attrs= zipkin_attrs,
                service_name='ssmzipkin2',
                span_name='serversimple1',
                transport_handler=http_transport,
                sample_rate=100, # Value between 0.0 and 100.0
            ) as childspan:
                response = urllib.request.urlopen(new_request)
                return HttpResponse("Made a simple request")
        except urllib2.URLError as e:
            return HttpResponse("Error: " + str(e))

def client_log(request):
    url = "http://localhost:8000/server/log"
    new_request = urllib.request.Request(url)
    # current_span = settings.OPENTRACING_TRACER.get_span(request)
    # inject_as_headers(settings.OPENTRACING_TRACER, current_span, new_request)
    try:
        response = urllib.request.urlopen(new_request)
        return HttpResponse("Sent a request to log")
    except urllib2.URLError as e:
        return HttpResponse("Error: " + str(e))

def client_child_span(request):
    url = "http://localhost:8000/server/childspan"
    new_request = urllib.request.Request(url)
    # current_span = settings.OPENTRACING_TRACER.get_span(request)
    # inject_as_headers(settings.OPENTRACING_TRACER, current_span, new_request)
    try:
        response = urllib.request.urlopen(new_request)
        return HttpResponse("Sent a request that should produce an additional child span")
    except urllib.error.URLError as e:
        return HttpResponse("Error: " + str(e))

def inject_as_headers(tracer, span, request):
    text_carrier = {}
    # tracer._tracer.inject(span.context, opentracing.Format.TEXT_MAP, text_carrier)
    for k, v in text_carrier.iteritems():
        request.add_header(k,v)
