# Create a Puppet file resource in /tmp

$doc_tmp = '/tmp/school'

file { $doc_tmp:
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
