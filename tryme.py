import os

import openai
from config import key


openai.api_key = key
response=openai.Image.create(prompt="a man coding",n=1,size="512x512")

image_url = response["data"][0]["url"]
print(image_url)





{created: 1699951189, data: Array(3)}
created
: 
1699951189
data
: 
Array(3)
0
: 
{url: 'https://oaidalleapiprodscus.blob.core.windows.net/…cyeklFI%2BLAr1xgd5%2BxPXVpFTdbNEN2JJ8b9tHI1JyE%3D'}
1
: 
{url: 'https://oaidalleapiprodscus.blob.core.windows.net/…6o/Uuz0IiU1Q85dhKdMxr%2B7c9oGyO9%2B1NBf66OdV3o%3D'}
2
: 
{url: 'https://oaidalleapiprodscus.blob.core.windows.net/…ig=KND8Dqy8f/UIqhFbYwjGc1tPHFlvLvfc1VVZ4W/4rAo%3D'}
length
: 
3
[[Prototype]]
: 
Array(0)
[[Prototype]]
: 
Object