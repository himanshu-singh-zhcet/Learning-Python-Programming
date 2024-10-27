import io
with open("test1.txt","wb") as f:
    file = io.BufferedWriter(f)
    file.write(b"this is my first line\n")
    file.write(b"this is my second line\n")
    file.flush()

with open("test1.txt","rb") as f:
    file = io.BufferedReader(f)
    a=file.read() # is waale function ke andr hum size bhi daal skte haui ki kitna data humko read krna hai 
    print(a)
    
