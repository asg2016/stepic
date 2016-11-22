ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx start
cd /home/box/web/ask/
sudo gunicorn -c /home/box/web/etc/gunicorn.conf ask.wsgi -D
