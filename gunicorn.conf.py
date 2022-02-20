import multiprocessing

bind = "178.79.181.140:9999"
workers = multiprocessing.cpu_count() * 2 + 1
wsgi_app = 'api:app'
reload = True
