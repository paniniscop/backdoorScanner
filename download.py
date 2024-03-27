import requests
# if u dont have install requests do pip install requests
def download_file(url, file_name):
    # use download title of requests to download the file
    response = requests.get(url) # requests get the url to send a request to download SpaceSS
    if response.status_code == 200: # if the response status = 200 it download the file
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print("Succesfully downloaded SpaceSS.")
    else: #if response status code is 404 you cant download the file
        print("Cant download SpaceSS.")

url = "https://www.mediafire.com/file/evtpxayqgd2iz65/SpaceSS.txt/file" #the url of the file u need to download dont edit this
file_name = "SpaceSS.txt" # the name of the file we want is downloaded

download_file(url, file_name) #download the file with the url and the file name! and its finished!
