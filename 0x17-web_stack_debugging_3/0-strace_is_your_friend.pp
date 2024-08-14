# find out why Apache is returning a 500 error.
# Once you find the issue, fix it and then automate it using Puppet

exec { 'replace_phpp_with_php':
  command => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
}
