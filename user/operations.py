import requests, json

class User:
	def __init__(self):
		self._url = "http://127.0.0.1:9090/"
		self.headers = {'Content-Type': 'application/json'}

	def Create_User(self,data):
		url = f"{self._url}user/Create_User/"
		data["type_document"] = 1
		response = requests.request("POST", url, headers= self.headers, data=json.dumps(data)
)
		return json.loads(response.text)


	def Login(self,data):
		url = f"{self._url}user/Get_Data_User/"
		payload = json.dumps({
		  "email": data['email'],
		  "psswd": data['psswd']
		})
		response = requests.request("GET", url, headers= self.headers, data=payload)
		return json.loads(response.text)

	def Get_User(self):
		url = f"{self._url}user/Get_User/"
		payload = json.dumps({"pk_user": 1})
		response = requests.request("GET", url, headers= self.headers, data=payload)
		return json.loads(response.text)

	def Update_Information_Person(self,data):
		url = f"{self._url}user/Update_Information_Persons/"
		response = requests.request('PUT', url, headers= self.headers, data=data)


	def Create_Work_Experience(self):
		url = f"{self._url}user/Create_Work_Experiences/"
		payload = json.dumps({
		  "pk_user": 1,
		  "company": "Theriosoft",
		  "position": "Desarrollador",
		  "city": "Medellín",
		  "description": "Desarrollaba software",
		  "from": None,
		  "to": None,
		  "active": True
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		print(response.text)


	def Create_Studies(self,data):
		url = f"{self._url}user/Create_Work_Experiences/"
		response = requests.request('POST',url, headers = self.headers, data = json.dumps(data))
		return json.loads(response.text)





