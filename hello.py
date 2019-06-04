from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
	return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
	return "Dojo!"

@app.route('/say/<id>')
def hello(id):
	if (type(id) is str):
		return "Hi " + id + "!"
	else:
		return "That's not a string!"

@app.route('/repeat/<num>/<stringy>')
def repeating(num, stringy):
	# num = int(num)
	# stringy = str(stringy)
	big_string = ''
	for i in range(int(num)):
		big_string = big_string + stringy + ' '
	return big_string

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry! No response. Try again."



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
	app.run(debug=True)    # Run the app in debug mode.