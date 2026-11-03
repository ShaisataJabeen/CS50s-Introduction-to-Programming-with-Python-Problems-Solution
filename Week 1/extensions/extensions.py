# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, 
# case-insensitively, in any of these suffixes:
# .gif .jpg .jpeg .png .pdf .txt .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

filename = input("Enter the desired file name: ").lower()

if  filename.endswith(".jpg"):
    print("image/jpeg")
    
elif filename.endswith(".pdf"):
    print("application/pdf")

elif filename.endswith(".gif"):
    print("image/gif")

elif filename.endswith(".jpeg"):
    print("image/jpeg")

elif filename.endswith(".txt"):
    print("text/plain")

elif filename.endswith(".zip"):
    print("application/zip")

elif filename.endswith(".png"):
    print("image/png")
else:
    print("application/octet-stream") 