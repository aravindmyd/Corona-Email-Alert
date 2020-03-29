
class helper:
	def __init__(self):
		import client
		try:
		    obj = client.Client()
		except:
		    print("error")
		    obj = client.Client()
