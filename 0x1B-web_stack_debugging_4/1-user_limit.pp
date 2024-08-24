# This manifest adjusts the OS configuration to allow the holberton user to log in and open files without issues

exec { 'set_holberton_hard_nofile':
  command => 'echo "holberton hard nofile 50000" >> /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  unless  => 'grep -q "^holberton hard nofile" /etc/security/limits.conf',
}

exec { 'set_holberton_soft_nofile':
  command => 'echo "holberton soft nofile 50000" >> /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  unless  => 'grep -q "^holberton soft nofile" /etc/security/limits.conf',
}
