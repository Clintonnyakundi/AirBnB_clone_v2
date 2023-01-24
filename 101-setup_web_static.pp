# Redo the task #0 but by using Puppet
exec { 'a':
  command => '/usr/bin/env apt-get update',
}
exec { 'b':
  command => '/usr/bin/env apt-get -y install nginx',
}
exec { 'c':
  command => '/usr/bin/env ufw allow "Nginx HTTP"',
}
exec { 'd':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/ /data/web_static/shared/',
}
exec { 'e':
  command => '/usr/bin/env touch /data/web_static/releases/test/index.html',
}
exec { 'f':
  command => '/usr/bin/env echo "
<html>
    <head></head>
    <body>
        <h1>Welcome to mogoodfeels.tech!</h1>
    </body>
</html>
" > /data/web_static/releases/test/index.html'
}
exec { 'g':
  command => '/usr/bin/env if [ -d "/data/web_static_current" ];
then
    /usr/bin/env rm -rf /data/web_static/current;
fi;',
}
exec { 'h':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
exec { 'i':
  command => '/usr/bin/env chown -hR ubuntu:ubuntu /data/',
}
exec { 'j':
  command => '/usr/bin/env sed -i "38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default',
}
exec { 'k':
  command => '/usr/bin/env ln -sf "/etc/nginx/sites-available/default" "/etc/nginx/sites-enabled/default"',
}
exec { 'm':
  command => '/usr/bin/env service nginx restart',
}
