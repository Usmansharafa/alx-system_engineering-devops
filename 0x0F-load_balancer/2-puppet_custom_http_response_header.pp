# Sets up a Nginx server with custom HTTP header

exec { 'update':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec {'header':
	command => 'sed -i "25i\	add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
