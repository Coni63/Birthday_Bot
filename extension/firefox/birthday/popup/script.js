var request = new XMLHttpRequest();
	request.withCredentials = false;
	request.addEventListener("readystatechange", function () {
		if (request.readyState == 4){
			/*
			for (let i=0; i < request.response.length; i++){
				console.log(request.response[i]);
			}
			*/
			document.getElementById("content").innerHTML = request.response;
		}
	});
	//request.open('GET', 'http://127.0.0.1:5000/api', true);
	request.open('GET', 'http://nicolasmine.pythonanywhere.com/api', true);
	request.send(null);