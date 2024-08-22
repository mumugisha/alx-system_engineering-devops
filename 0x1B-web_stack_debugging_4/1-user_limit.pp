# This manifest increases the soft and hard file descriptor limits for the holberton user.

exec { 'increase-hard-file-limit-for-holberton-user':
 command => 'sed -i \'/^holberton.*hard.*nofile/s/[0-9]\\+/50000/\' /etc/security/limits.conf',
 path    => ['/usr/local/bin', '/usr/bin', '/bin'],
 onlyif  => 'grep -q "^holberton.*hard.*nofile" /etc/security/limits.conf',
}

exec { 'increase-soft-file-limit-for-holberton-user':
 command => 'sed -i \'/^holberton.*soft.*nofile/s/[0-9]\\+/50000/\' /etc/security/limits.conf',
 path    => ['/usr/local/bin', '/usr/bin', '/bin'],
 onlyif  => 'grep -q "^holberton.*soft.*nofile" /etc/security/limits.conf',
}
