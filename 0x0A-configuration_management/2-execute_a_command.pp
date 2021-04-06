# kill a proccess
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
