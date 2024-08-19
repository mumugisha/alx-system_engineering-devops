# Increase the ULIMIT for default file
exec { 'fix --for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
  onlyif  => 'grep -q "15" /etc/default/nginx',
  notify  => Exec['nginx-restart'],
}

# Restart Nginx
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  path        => ['/usr/sbin', '/sbin', '/usr/local/sbin', '/usr/bin', '/bin'],
  refreshonly => true,
}
