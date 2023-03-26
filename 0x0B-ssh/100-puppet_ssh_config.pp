# Configure ssh config file
file_line { 'ssh_config':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}

file_line { 'ssh_config':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
