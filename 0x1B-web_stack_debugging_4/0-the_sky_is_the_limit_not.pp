#debugging apache server
exec { 'increase request limit':
  command => "sed -i 's/15/4096/g' /etc/default/nginx ",
  path    => '/bin',
}
