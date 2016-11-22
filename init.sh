ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx start
sudo gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
cd /home/box/web/ask/
sudo gunicorn -c /home/box/web/etc/django.PY ask.wsgi:application -D
