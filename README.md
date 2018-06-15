# Observability Boilerplate for Log-Metric-Tracing Collection

This is a simple observability boilerplate that is aimed at Log-Metric-Tracing collection

## Components
1. Application:	Python Django
2. Log Collection: Elastic
3. Metric Collection: Prometheus
4. Trace Collection: Zipkin
5. Dashboarding: Kibana | Grafana | Zipkin

Note: A huge thanks to @mordaha for building a [base seed project](https://github.com/mordaha/django-docker-seed) on top of which this boilerplate is built.

## It uses:

- python 3
- django 1.9
- postgresql for django database (dockerized for development, host-based for production)
- nginx as production webserver, with send_file && secure_link for serve uploaded files
- elasticsearch + logstash + kibana (ELK) for log collection
- prometheus for metric collection
- zipkin for trace collection
- ./setup.sh for "docker-compose with development config" shortcut

## Boilerplate Setup and URLs

01. Run `$ ./setup.sh`
02. Wait until all containers start, then run `./es_index.sh`
03. Python Django application URL:	http://127.0.0.1:8000/
04. Nginx URL (First log entry):	http://127.0.0.1:8080/
05. Logstash Endpoint:				http://127.0.0.1:8050/
06. Elasticsearch URL:				http://127.0.0.1:8020/
07. Kibana Dashboard URL:			http://127.0.0.1:8056/
08. Prometheus Dashboard URL:		http://127.0.0.1:9090/
09. Grafana Dashboard URL:			http://127.0.0.1:3000/
10. Zipkin Dashboard URL:			http://127.0.0.1:9411/

## License

MIT

## TODO

- Polishing the setup