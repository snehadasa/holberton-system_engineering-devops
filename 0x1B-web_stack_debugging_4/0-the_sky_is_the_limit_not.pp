#debugging apache server
exec { 'increaserequestlimit':
  command => 'sed -i "s/15/4096/g" /etc/default/nginx && service nginx restart',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin']
}
