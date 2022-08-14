data={"Krishna":[67,68,69], "Arjun":[70,98,63], "Malika":[52,56,60]}

nm=input("Enter a name: ")

if nm=="Krishna":
   print(sum(data.get("Krishna"))/3)
elif nm=="Arjun":
   print(sum(data.get("Arjun"))/3)
elif nm=="Malika":
   print(sum(data.get("Malika"))/3)