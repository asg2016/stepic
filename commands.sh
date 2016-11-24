sudo pip install pymysql
sudo pip install --upgrade django
sudo mkdir web
sudo git clone https://github.com/asg2016/stepic /home/box/web
sudo bash /web/mysql.sh
sudo python /web/ask/manage.py syncdb
