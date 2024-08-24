# This manifest adjusts the OS configuration to allow the holberton user to log in and open files without issues

exec { 'set_holberton_nofile_limits':
  command => 'echo -e "holberton hard nofile 50000\nholberton soft nofile 50000" >> /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  unless  => 'grep -q "^holberton hard nofile" /etc/security/limits.conf && grep -q "^holberton soft nofile" /etc/security/limits.conf',
}
