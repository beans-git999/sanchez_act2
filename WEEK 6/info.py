from xml.sax.handler import property_interning_dict

myInfo = {"Name" : "Naruto Uzumaki", "Age" : 32, "Position" : "Hokage", "Address" : "Konoha"}
print(myInfo)
print(myInfo["Name"])
print(myInfo["Address"])
print(myInfo["Age"])
print(myInfo.get("Name"))
myInfo["Name"] = "Bogart"
print(myInfo)
print(myInfo["Name"])
myInfo.update({"Section" : 4})
print(myInfo)

#{"Name" : "FirstName" : "Vince", "LastName" : Sanchez "Age" : 19, Hobbies : ["training", "running", "exploring"]}
MyInfo = {
  "Name": {
    "FirstName": "Vince",
    "LastName": "Sanchez"
  },
  "Age": 19,
  "Hobbies": [
      "training",
      "running",
      "exploring"]
}
print(MyInfo)
print(MyInfo["Name"]["FirstName"])
print(MyInfo["Name"])
print(MyInfo["Name"]["FirstName"] + " " + MyInfo["Name"]["LastName"])
print(MyInfo["Hobbies"][1])

