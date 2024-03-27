import requests

def download_file(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print("Succesfully downloaded SpaceSS.")
    else:
        print("Cant download SpaceSS.")

url = "https://www.mediafire.com/file/evtpxayqgd2iz65/SpaceSS.txt/file"
file_name = "SpaceSS.txt"

download_file(url, file_name)
