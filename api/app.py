from flask import Flask, jsonify, request


app = Flask(__name__)
app.id_count = 1
app.users = {}


@app.route("/ping", methods=['get'])
def ping():
	return "pong"

@app.route("/sign-up", methods=['POST'])
def sign_up():
	new_user				= request.json
	new_user["id"]			= app.id_count
	app.users[app.id_count]	= new_user
	app.id_count			 = app.id_count+1

	return jsonify(new_user)

app.tweets = []


@app.route('/tweet', methods=['POST'])
def tweet():
	payload = request.json
	user_id = int(payload['id'])
	tweet = payload['tweet']

	if user_id not in app.users:
		return 'There is no user id' + str(user_id) + '.', 400
	
	if len(tweet)>300:
		return 'over the limit 300 words', 400

	user_id = int(payload['id'])

	app.tweets.append({
		'user_id':user_id,
		'tweet': tweet
	})
	
	return '', 200
