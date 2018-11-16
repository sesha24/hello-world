import requests

url = "https://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

cookie = {"APIC-Cookie" : "/9gk6omAOI62U02QI6iS0GUNgG+x3ygN5rHvYOduC6a6vN9cow9vlf8TLXoK5zF5W/DUhRAoowoe7mIdKyKqrF53laYu2lCMedHsFyOU0Udn4Uf4cK9OE2R8Flr9uVrEim4do0vwkMqerFGkoiW9Y8AWsBILdA8wrZwD4Lir2/Q="}
payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
response = requests.request("POST", url, verify=False, data=payload, cookies=cookie)

print(response.text)