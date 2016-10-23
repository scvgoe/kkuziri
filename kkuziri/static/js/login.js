// This is called with the results from from FB.getLoginStatus().
function statusChangeCallback(response) {
	console.log('statusChangeCallback');
	console.log(response);
	if (response.status === 'connected') {
		// Logged into your app and Facebook.
		login();
	} else if (response.status === 'not_authorized') {
		// The person is logged into Facebook, but not your app.
		login();
	} else {
		// The person is not logged into Facebook, so we're not sure if
		// they are logged into this app or not.
	}
}

// This function is called when someone finishes with the Login
// Button.  See the onlogin handler attached to it in the sample
// code below.
function checkLoginState() {
	FB.getLoginStatus(function(response) {
		statusChangeCallback(response);
	});
}

window.fbAsyncInit = function() {
	FB.init({
		appId      : '343088246039699',
		cookie     : true,  // enable cookies to allow the server to access 
		// the session
		xfbml      : true,  // parse social plugins on this page
		version    : 'v2.7' // use graph api version 2.5
	});

	// Now that we've initialized the JavaScript SDK, we call 
	// FB.getLoginStatus().  This function gets the state of the
	// person visiting this page and can return one of three states to
	// the callback you provide.  They can be:
	//
	// 1. Logged into your app ('connected')
	// 2. Logged into Facebook, but not your app ('not_authorized')
	// 3. Not logged into Facebook and can't tell if they are logged into
	//    your app or not.
	//
	// These three cases are handled in the callback function.
};

// Load the SDK asynchronously
(function(d, s, id) {
	var js, fjs = d.getElementsByTagName(s)[0];
	if (d.getElementById(id)) return;
	js = d.createElement(s); js.id = id;
	js.src = "//connect.facebook.net/en_US/sdk.js";
	fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Here we run a very simple test of the Graph API after login is
// successful.  See statusChangeCallback() for when this call is made.
function login() {
	FB.api('/me', function(response) {
		// Request to server login api
		$.ajax({
			type: "POST",
			contentType: "application/json; charset=utf-8",
			url: "/login/facebook",
			data: JSON.stringify({username: response.id, name: response.name}),
			dataType: "json",
			success:function(args){ 
				console.log("success");
				window.location.replace("http://local.kkuziri.io:5000/index");
			},
			error:function(e) {
				console.log("fail");
				window.location.replace("http://local.kkuziri.io:5000/login");
			}
		});        
	});
}

function facebookLogin() {
 FB.login(function(response) {
	statusChangeCallback(response);
 }, {scope: 'public_profile,email'});
}
