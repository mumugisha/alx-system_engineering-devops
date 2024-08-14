exec { 'replace_phpp_with_php':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
