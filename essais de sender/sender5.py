import requests

apikey=...
apiurl=...
domainname=...
email=...
def send_simple_message():
	return requests.post(
		f"https://api.eu.mailgun.net/v3/{domainname}/messages",
		auth=("api", apikey),
		data={"from": f"Excited User <mailgun@{domainname}>",
			"to": ["momoladebrouill@gmail.com",f"jean@{domainname}"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
