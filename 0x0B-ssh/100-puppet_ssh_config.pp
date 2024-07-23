# mymodule/manifests/init.pp

# Class to manage SSH configuration
class mymodule::ssh_config {
  file { '/etc/ssh/ssh_config':
    ensure => 'present',
  }

  # Ensure 'passwordAuthentication no' is present in /etc/ssh/ssh_config
  file_line { 'ensure_password_authentication_no':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'passwordAuthentication no',
    match  => '^passwordAuthentication',
  }

  # Ensure 'IdentityFile ~/.ssh/school' is present in /etc/ssh/ssh_config
  file_line { 'ensure_identity_file_school':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^IdentityFile',
  }
}

