# Sets up a Nginx server with custom HTTP header

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

