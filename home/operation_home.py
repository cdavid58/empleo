import json, requests

class Home_O:
	def __init__(self):
		self._url = "http://127.0.0.1:9090"
		self.headers = {'Content-Type': 'application/json'}

	def All_List_Application(self):
		url = f"{self._url}/operation/All_List_Application/"
		payload = {}
		headers = {}
		response = requests.request("GET", url, headers=headers, data=payload)
		return json.loads(response.text)

	def Get_All_List_Applications(self, pk_user):
		url = f"{self._url}/operation/Get_List_Application/"
		payload = json.dumps({"pk_user": pk_user})
		response = requests.request("GET", url, headers= self.headers, data=payload)
		return json.loads(response.text)

	def Get_Publication(self,pk):
		url = f"{self._url}/operation/Get_Publication/"
		payload = json.dumps({"pk": pk})
		response = requests.request("GET", url, headers= self.headers, data=payload)
		return json.loads(response.text)


	def Applicat_Publication(self,pk_user,pk_application):
		url = f"{self._url}/operation/Applicat_Publication/"
		payload = json.dumps({
		  "pk_user": pk_user,
		  "pk_publication": pk_application
		})
		response = requests.request("POST", url, headers= self.headers, data=payload)
		return json.loads(response.text)


	def Delete_Application_Publication(self,pk_publication, pk_user):
		url = f"{self._url}/operation/remove_user_from_applicant/"
		payload = json.dumps({
		  "pk": pk_publication,
		  "pk_user": pk_user
		})
		response = requests.request("POST", url, headers= self.headers, data=payload)
		return json.loads(response.text)




