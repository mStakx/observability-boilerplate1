## Example

This is an example of a Django site with tracing implemented using the django_opentracing package, with Jaeger.
To run the example (Following https://github.com/jaegertracing/jaeger/blob/master/docs/getting_started.md#all-in-one-docker-image):

```
# Optional
cd example
pip install -r requirements.txt
docker run -d -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 -p5775:5775/udp -p6831:6831/udp -p6832:6832/udp -p5778:5778 -p16686:16686 -p14268:14268 -p9411:9411 jaegertracing/all-in-one:latest
python manage.py runserver 8000
```



Open in your browser `localhost:8000/client`.

Also http://localhost:16686 (for the Jaeger UI)

### Trace a Request and Response

Navigate to `/client/simple` to send a request to the server. There will be a span created for both the client request and the server response from the tracing decorators, `@tracer.trace()`.

![simple](https://raw.githubusercontent.com/kcamenzind/django_opentracing/master/example/img/simple.png)

### Log a Span

Navigate to `/client/log` to send a request to the server and log something to the server span. There will be a span created for both the client request and server response from the tracing decorators. The server views.py handler will manually log the server span with the message 'Hello, world!'.

![log](https://raw.githubusercontent.com/kcamenzind/django_opentracing/master/example/img/log.png)

### Create a Child Span manually

Navigate to `/client/childspan` to send a request to the server and create a child span for the server. There will be span created for both the client request and server response from the tracing decorators. The server views.py handler will manually create and finish a child span for the server span.

![child span](https://raw.githubusercontent.com/kcamenzind/django_opentracing/master/example/img/childspan.png)

### Don't Trace a Request

Navigating to `/client` will not produce any traces because there is no `@trace.trace()` decorator. However, if `settings.OPENTRACING['TRACE_ALL_REQUESTS'] == True`, then every request (including this one) will be traced, regardless of whether or not it has a tracing decorator.
