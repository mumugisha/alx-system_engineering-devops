# This manifest adjusts the OS configuration to allow the holberton user to log in and open files without issues

file_line { 'set_holberton_hard_nofile':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 50000',
  match => '^holberton\s+hard\s+nofile',
}

file_line { 'set_holberton_soft_nofile':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 50000',
  match => '^holberton\s+soft\s+nofile',
}
