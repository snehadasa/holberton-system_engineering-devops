#to create ssh-config file
file_line { 'Turn off passwd auth':
ensure   => 'present',
path     => '/etc/ssh/ssh_config',
line     => 'IdentifyFile ~/.ssh/holberton',
multiple => 'true',
}

file_line { 'Declare identify file':
ensure   => 'present',
path     => '/etc/ssh/ssh_config',
line     => 'PasswordAuthentification no',
multiple => 'true',
}
