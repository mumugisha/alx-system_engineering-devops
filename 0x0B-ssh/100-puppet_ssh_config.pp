#!/usr/bin/env bash
##make changes to your config files
file { '/etc/ssh/ssh_config':
  ensure => 'present',
}

# Ensure 'passwordAuthentication no' is present in /etc/ssh/ssh_config
file_line { 'turn off password authentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'passwordAuthentication no',
  match   => '^passwordAuthentication yes',
  replace => 'true',
}

# Ensure 'IdentityFile ~/.ssh/school' is present in /etc/ssh/ssh_config
file_line { 'ensure_identity_file_school':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/config',
  match  => '^IdentityFile',
}
