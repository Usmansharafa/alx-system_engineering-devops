# Sets up a Nginx server with custom HTTP header

package {
    'nginx':
    ensure => installed,
}

file {'/var/www/html/index.nginx-debian.html':
    content => 'Hello World!',
}

file_line {'configure redirection':
    path  =>  '/etc/nginx/sites-available/default',
    after =>  'server_name _;',
    line  =>  "\n\tlocation /redirect_me {\n\t\treturn 301 https://youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n",
}

file { '/etc/nginx/conf.d/custom-header.conf':
  ensure  => file,
  content => "add_header X-Served-By $hostname;",
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
