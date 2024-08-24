# This Puppet manifest enforces a very low file descriptor limit for the holberton user,
# ensuring the "Too many open files" error occurs on login

file_line { 'decrease-hard-file-limit-for-holberton':
  path  => '/etc/security/limits.conf',
  line  => 'holberton hard nofile 10',
  match => '^holberton.*hard.*nofile',
}

file_line { 'decrease-soft-file-limit-for-holberton':
  path  => '/etc/security/limits.conf',
  line  => 'holberton soft nofile 10',
  match => '^holberton.*soft.*nofile',
}

# Ensure PAM limits are enabled
file_line { 'pam_limits':
  path  => '/etc/pam.d/common-session',
  line  => 'session required pam_limits.so',
  match => '^session\s+required\s+pam_limits\.so',
}

file_line { 'pam_limits_noninteractive':
  path  => '/etc/pam.d/common-session-noninteractive',
  line  => 'session required pam_limits.so',
  match => '^session\s+required\s+pam_limits\.so',
}
