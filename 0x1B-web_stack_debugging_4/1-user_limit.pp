# This manifest adjusts the OS configuration to allow the holberton user to log in and open files without issues

exec {'increase-file-limits-for-holberton-user':
  command => 'sed -i -e \'/^holberton.*hard.*nofile/s/[0-9]\\+/50000/\' -e \'/^holberton.*soft.*nofile/s/[0-9]\\+/50000/\' /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  onlyif  => 'grep -q "^holberton.*hard.*nofile" /etc/security/limits.conf && grep -q "^holberton.*soft.*nofile" /etc/security/limits.conf',
}
