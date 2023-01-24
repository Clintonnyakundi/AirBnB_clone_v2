exec { 'a':
  command => 'sudo apt-get update'
}
exec { 'b':
  command => 'sudo apt-get -y install nginx'
}
exec { 'c':
  command => 'sudo ufw allow "Nginx HTTP"'
}
exec { 'd':
  command => 'sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/'
}
exec { 'e':
  command => 'sudo touch /data/web_static/releases/test/index.html'
}
exec { 'f':
  command => 'echo "
<html>
    <head></head>
    <body>
        <h1>Welcome to mogoodfeels.tech!</h1>
    </body>
</html>
" > /data/web_static/releases/test/index.html'
}
exec { 'g':
  command => 'if [ -d "/data/web_static_current" ];
then
    sudo rm -rf /data/web_static/current;
fi;'
}
exec { 'h':
  command => 'sudo ln -sf /data/web_static/releases/test /data/web_static/current'
}
exec { 'i':
  command => 'sudo chown -hR ubuntu:ubuntu /data/'
}
exec { 'j':
  command => 'sudo sed -i "38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default'
}
exec { 'k':
  command => 'sudo ln -sf "/etc/nginx/sites-available/default" "/etc/nginx/sites-enabled/default"'
}
exec { 'm':
  command => 'sudo service nginx restart'
}
