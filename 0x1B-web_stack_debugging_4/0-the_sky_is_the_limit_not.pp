#debugging apache server
exec { 'increase request limit':
  command => "sed -i 's/15/100000/g' /etc/default/nginx ",
  path    => '/bin',
}
