config={
	apiKey: "AIzaSyAYRuwDZVYHn4fOLLRIwMQaa9GNQBbfIws",
    authDomain: "oilancer-168616.firebaseapp.com",
    databaseURL: "https://oilancer-168616.firebaseio.com",
    projectId: "oilancer-168616",
    storageBucket: "oilancer-168616.appspot.com",
    messagingSenderId: "598300711381"
};

firebase.initializeApp(config);

firebase.auth().onAuthStateChanged(function(user) {
	  if (user) {
	    // User is signed in.
	    console.log(user);
	    console.log(user.uid);
	    console.log(user.email);
	    console.log(user.displayName);
	    console.log(user.photoURL);
	    $("#input_email").val(user.email);
	    $("#input_id").val(user.uid);
	    $("#input_name").val(user.displayName);
	    $("#input_foto").val(user.photoURL);
	    $("#form_helper").submit();
		// window.location.replace("http://localhost/oilancer");
	  } else {
	    // No user is signed in.
	    console.log('not logged in');
	  }
	});

	const btnLogin = document.getElementById("btnLogin");
	const btnRegister = document.getElementById("btnRegister");		
	const txtEmail = document.getElementById("txtEmail");
	const txtPassword = document.getElementById("txtPassword");

	if(btnLogin != null){
		btnLogin.addEventListener('click', e => {
			console.log("yoi");
			const email = txtEmail.value;
			const pass = txtPassword.value;
			const auth = firebase.auth();

			var promise = auth.signInWithEmailAndPassword(email,pass);
			promise.catch(e => console.log(e.message));
		});
	}

	if(btnRegister != null){
		btnRegister.addEventListener('click', e => {
			console.log("yoi");
			const email = txtEmail.value;
			const pass = txtPassword.value;
			const auth = firebase.auth();

			var promise = auth.createUserWithEmailAndPassword(email,pass);
			promise
				.catch(e => console.log(e.message));
			promise = auth.signInWithEmailAndPassword(email,pass);
			promise
				.catch(e => console.log(e.message));
			window.location.replace("http://localhost/oilancer");
		});
	}

	var provider = new firebase.auth.GoogleAuthProvider();
	document.querySelector('#login_google').addEventListener('click', function(e) {
		e.preventDefault();
	  	e.stopPropagation();
		console.log("clicked");
		firebase.auth().signInWithPopup(provider).then(function(result) {
		// This gives you a Google Access Token. You can use it to access the Google API.
			var token = result.credential.accessToken;
			console.log(token);
			// The signed-in user info.
			var user = result.user;
			// ...
		}).catch(function(error) {
			// Handle Errors here.
			var errorCode = error.code;
			var errorMessage = error.message;
			// The email of the user's account used.
			var email = error.email;
			// The firebase.auth.AuthCredential type that was used.
			var credential = error.credential;
			console.log(error.message);
			// ...
		});

		// Step 1.
		// User tries to sign in to Google.
		auth.signInWithPopup(new firebase.auth.GoogleAuthProvider()).catch(function(error) {
	  		// An error happened.
	  		if (error.code === 'auth/account-exists-with-different-credential') {
		    	// Step 2.
		    	// User's email already exists.
	    		// The pending Google credential.
	    		var pendingCred = error.credential;
	    		// The provider account's email address.
		    	var email = error.email;
	    		// Get registered providers for this email.
	    		auth.fetchProvidersForEmail(email).then(function(providers) {
	      			// Step 3.
	      			// If the user has several providers,
	      			// the first provider in the list will be the "recommended" provider to use.
	      			if (providers[0] === 'password') {
	        			// Asks the user his password.
	        			// In real scenario, you should handle this asynchronously.
	        			var password = promptUserForPassword(); // TODO: implement 		promptUserForPassword.
	        			auth.signInWithEmailAndPassword(email, password).then(function(user) {
	          				// Step 4a.
	          				return user.link(pendingCred);
	        			}).then(function() {
	          				// Google account successfully linked to the existing Firebase user.
	          				goToApp();
	        			});
	        			return;
	      			}
			      	// All the other cases are external providers.
			      	// Construct provider object for that provider.
			      	// TODO: implement getProviderForProviderId.
	      			var provider = getProviderForProviderId(providers[0]);
			      	// At this point, you should let the user know that he already has an account
			      	// but with a different provider, and let him validate the fact he wants to
			      	// sign in with this provider.
			      	// Sign in to provider. Note: browsers usually block popup triggered asynchronously,
			      	// so in real scenario you should ask the user to click on a "continue" button
			      	//	 that will trigger the signInWithPopup.
	      			auth.signInWithPopup(provider).then(function(result) {
	        		// Remember that the user may have signed in with an account that has a different email
	        		// address than the first one. This can happen as Firebase doesn't control the provider's
	        		// sign in flow and the user is free to login using whichever account he owns.
	        		// Step 4b.
	        		// Link to Google credential.
	        		// As we have access to the pending credential, we can directly call the link method.
	        			result.user.link(pendingCred).then(function() {
	          				// Google account successfully linked to the existing Firebase user.
	          				goToApp();
	        			});
	      			});
	    		});
	  		}
		});	

		var current_user = firebase.auth().currentUser;
		console.log("halo");
    });