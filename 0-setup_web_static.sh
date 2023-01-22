#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

# install nginx
sudo apt-get update
sudo apt-get -y install nginx

# configure firewall
sudo ufw allow 'Nginx HTTP'

# create directories
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# create file with test strings
sudo touch /data/web_static/releases/test/index.html
echo "
<html>
    <head></head>
    <body>
        <h1>Welcome to mogoodfeels.tech!</h1>
    </body>
</html>
" > /data/web_static/releases/test/index.html

# delete if dir exists
if [ -d "/data/web_static_current" ];
then
    sudo rm -rf /data/web_static/current;
fi;

# create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# give ownership of /data/ to ubuntu user
sudo chown -hR ubuntu:ubuntu /data/

# serve content of /data/web_static/current to /hbnb_static
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

# restart nginx
sudo service nginx restart
