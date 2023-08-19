import json, requests

class Company_O:
	def __init__(self):
		self.headers = {}
		self._url = "http://127.0.0.1:9090/"

	def Get_Area(self):
		url = f"{self._url}setting/Get_Area/"
		response = requests.request("GET", url, headers= {}, data= {})
		return json.loads(response.text)

	def Get_City(self):
		url = f"{self._url}setting/Get_City/"
		response = requests.request("GET", url, headers= {}, data= {})
		return json.loads(response.text)

	def Type_Contract(self):
		url = f"{self._url}setting/Type_Contract/"
		response = requests.request("GET", url, headers= {}, data= {})
		return json.loads(response.text)

	def Workday(self):
		url = f"{self._url}setting/Workday/"
		response = requests.request("GET", url, headers= {}, data= {})
		return json.loads(response.text)
		
	def Workplace(self):
		url = f"{self._url}setting/Workplace/"
		response = requests.request("GET", url, headers= {}, data= {})
		return json.loads(response.text)		

	def Minimum_Studiess(self):
		url = f"{self._url}setting/Minimum_Studiess/"
		response = requests.request("GET", url, headers= {}, data= {})
		return json.loads(response.text)
		
	def languages(self):
		url = f"{self._url}setting/languages/"
		response = requests.request("GET", url, headers= {}, data= {})
		return json.loads(response.text)
		
	def Languages_Levels(self):
		url = f"{self._url}setting/Languages_Levels/"
		response = requests.request("GET", url, headers= {}, data= {})
		return json.loads(response.text)

class Authentication_Company:
	def __init__(self):
		self.headers = {'Content-Type': 'application/json'}
		self._url = "http://127.0.0.1:9090/"

	def Create_Company(self,data):
		url = f"{self._url}company/Create_Company/"
		payload = json.dumps(
			{
			    "nit":data['nit'],
				"name":data['name'],
				"email":data['email'],
				"phone_1":data['phone_1'],
				"psswd": data['psswd']
			}
		)
		response = requests.request('POST', url, headers = self.headers, data= payload)
		return json.loads(response.text)['result']

	def Login_Company(self,data):
		url = "http://127.0.0.1:9090/company/Login/"
		payload = json.dumps({
		  "email": data['email'],
		  "psswd": data['psswd']
		})
		response = requests.request("GET", url, headers= self.headers, data=payload)
		return json.loads(response.text)




class Publication:
	def __init__(self):
		self.headers = {'Content-Type': 'application/json'}
		self._url = "http://127.0.0.1:9090/"

	def Create_Publication(self,data,user):
		url = f"{self._url}operation/Create_Publication/"
		payload = json.dumps({
		  "offer_title": data['offer_title'],
		  "area": data['area'],
		  "description": data['description'],
		  "municipalities": data['municipalities'],
		  "workday": data['workday'],
		  "workplace": data['workplace'],
		  "type_contract": data['type_contract'],
		  "salary": data['salary'],
		  "date_hire": data['date_hire'],
		  "number_vacancies": data['number_vacancies'],
		  "years_experience": data['years_experience'],
		  "age_start": data['age_start'],
		  "age_end": data['age_end'],
		  "minimum_studies": data['minimum_studies'],
		  "languages": data['languages'],
		  "languages_level": data['languages_level'],
		  "driving_license": data['driving_license'],
		  "availability_travel": data['availability_travel'],
		  "change_residence": data['change_residence'],
		  "company": user,
		})
		response = requests.request("POST", url, headers= self.headers, data=payload)
		print(response.text)

	def All_List_Application_Company(self,company):
		url = f"{self._url}operation/All_List_Application_Company/"
		payload = json.dumps({"pk_company":company})
		response = requests.request("GET", url, headers= self.headers, data=payload)
		return json.loads(response.text)
