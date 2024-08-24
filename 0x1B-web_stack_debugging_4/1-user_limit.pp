# Your Puppet manifest adjusts the OS configuration so that it is possible to log in with the holberton user and open a file without issue

exec { 'set_holberton_nofile_limits':
  command => 'echo -e "holberton hard nofile 50000\nholberton soft nofile 50000" >> /etc/security/limits.conf',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  unless  => 'grep -q "^holberton hard nofile 50000" /etc/security/limits.conf && grep -q "^holberton soft nofile 50000" /etc/security/limits.conf',
}

# Ensure PAM limits are applied
exec { 'ensure_pam_limits':
  command => 'grep -q "session required pam_limits.so" /etc/pam.d/common-session || echo "session required pam_limits.so" >> /etc/pam.d/common-session',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  unless  => 'grep -q "session required pam_limits.so" /etc/pam.d/common-session',
}
