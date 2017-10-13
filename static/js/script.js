

document.getElementById("contactForm").addEventListener("submit",function(e) {
	e.preventDefault();
  var missing = "";
  if(document.getElementById("name").value == "") {
    missing = missing.concat("Missing field: name <br>");
  }
  if(document.getElementById("subject").value == "") {
    missing = missing.concat("Missing field: subject <br>");
  }
  if(document.getElementById("message").value == "") {
    missing = missing.concat("Missing field: message <br>");
  }
  if (missing != "") {
    document.getElementById("missingFields").innerHTML = missing;
  } else {
		var xhttp = new XMLHttpRequest();
		xhttp.open("POST","/form",true);
		s = xhttp.send('{"name":"' + document.getElementById("name").value  + '","email":"' +  "gavinblee@berkeley.edu" + '","subject":"' + document.getElementById("subject").value + '","msg":"' + document.getElementById("message").value + '"}')
		document.getElementById("message").value = "";
		document.getElementById("subject").value = "";
		document.getElementById("missingFields").innerHTML = "Hi "+document.getElementById("name").value + ". Your message has been sent";

		document.getElementById("name").value = "";
  }
});
