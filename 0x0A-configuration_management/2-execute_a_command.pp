#Create a manifest that kills a process named killmenow

exec { 'pkill_killmenow':
  command   => 'pkill -f killmenow',
  provider  => 'shell',
  logoutput => true,
}
