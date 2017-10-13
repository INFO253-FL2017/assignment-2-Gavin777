What is the function of the following technologies in your assignment:
- HTML: Forms the structure and content of my website
- CSS: Provides styling of the HTML (structure and content). Like colors, margings, padding etc
- JavaScript: Provides interactivity, such as giving feedback to the user in the contact form on whether or not the form was submitted successfully.
- Python: Closely tied with Flask. Need Python to use Flask. Responsible for routing urls and handling POST request for MailGun
- Flask: Used by Python to render different templates (html pages)
- HTTP: The protocol that GET and POST requests follow for transferring data
- GET and POST requests: GET is used to grab an html page and use it as a resource (render on website or stylesheet or script or favicon). POST is used to send data, in this case, to send data so an email can be sent through the contact form.

How does HTML, CSS, and JavaScript work together in the browser for this assignment?
- HTML, CSS and Javascript are used together to create the structure of the website and its different pages, style it so it looks nice, and create user interactivity.

How does Python and Flask work together in the server for this assignment?
- Python and Flask work together to handle routing and render templates (html pages). Once Python figures out what url is being requested, it routes and goes to a function that renders a template using Flask. Flask is used by Python.

List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request
- "GET /static/css/style.css HTTP/1.1" 200: Gets css stylesheet
- "GET /static/js/script.js HTTP/1.1" 200: Gets javascript script
- "GET /favicon.ico HTTP/1.1" 404: Gets Favicon (not found)
- "POST /form HTTP/1.1" 204: Posts request for sending email using /form url that I routed to the post_form() function
- "GET /contact HTTP/1.1" 200: Get contact page
- "GET /blog/what-productivity-systems-wont-solve HTTP/1.1" 200 - Gets productivity blog post
- "GET /blog/training-to-be-a-good-writer HTTP/1.1" 200 - Gets writing blog post
- "GET /blog/how-to-develop-an-awesome-sense-of-direction HTTP/1.1" 200 - Gets direction blog post
- "GET /blog/a-mindful-shift-of-focus HTTP/1.1" 200 - Gets focus blog post
- "GET /blog/8-experiments-in-motivation HTTP/1.1" 200 - Gets motivation blog post
- "GET /about HTTP/1.1" 200 - Gets about us page
- "GET /index HTTP/1.1" 200 - Gets index/home page
