


## URL Shortener

# pip3 install pyshorteners

import pyshorteners

url = input("Enter your url: ")
print("Your url: ", pyshorteners.Shortener().tinyurl.short(url))

# Bit.ly shortener Implementation
# Get API KEY from your bitly account

api_key = "c055bbc78770145c321a27576fa59e9123f5ae69"

s = pyshorteners.Shortener(api_key=api_key)
print(s.bitly.short(url))

#follow insta/@codewithjoxia