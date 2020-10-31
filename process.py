from flask import Flask, render_template, request, jsonify
import predict_tweet

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	name = request.form['name']
	
	if name:
		try:
			newName = predict_tweet.predict(name)
			if newName==2:
				return jsonify({'name' : 'FAKE NEWS DETECTED!!'})
			else:
    				return jsonify({'name' : 'THIS SEEMS A REAL NEWS'})

		except:
			newName = "INVALID"
			return jsonify({'name' : newName})
		

	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)