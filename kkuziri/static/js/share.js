function share(url) {
  FB.ui({
    method: 'share',
    display: 'popup',
    href: url,
  }, function(response){});
}
