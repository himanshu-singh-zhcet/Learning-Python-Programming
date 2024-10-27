#working with json file
data = {
    "name" : "himashu",
    "email_id" : "hanshu5252@gmail.com",
    "phone-no" : 8171912220,
    "subjects" : ["data science","big data","data analatyics"]
}

import json
with open("data.json","w") as f:
    json.dump(data,f)

with open("data.json","r") as f:
    data1 = json.load(f)
print(data1)
print(data1["subjects"][1])


# working with csv file
import csv
data2 = [["name","email_id","phone_number"],
        ["Himanshu","hanshu5252",8181],
        ["shivani","shivisingh4498",9796]
        ]
with open("data2.csv","w") as f:
    writer = csv.writer(f)    # creating writer object
    for i in data2:
        writer.writerow(i)

with open("data2.csv","r") as f:
    read_data = csv.reader(f)
    for i in read_data:
        print(i)

# working with binary data 
with open("test4.bin","wb") as f:
    f.write(b"\x01\x02\x03")
with open("test4.bin","rb") as f:
    print(f.read())