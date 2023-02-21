import requests
import io
from io import BytesIO
from PIL import Image
import time


#GOOGLE SETUP
from google.cloud import vision
client = vision.ImageAnnotatorClient()

#TUMBLR SETUP
import pytumblr
import json
import re

#VARIABLES
tumblrclient = pytumblr.TumblrRestClient(
  !!!! YOUR CLIENT ID HERE !!!!
)

botblog = !!!! YOUR BOT BLOG NAME AS STRING HERE !!!!

#FIND TAGS

while True:


    taggedposts = tumblrclient.tagged('alttextbot', limit=1, filter='raw')
    firstpost=taggedposts[0]

    postblog = firstpost.get('blog')

    postuuid = postblog.get('uuid')
    postid = firstpost.get('id')
    postkey = firstpost.get('reblog_key')

    imageget= re.search('(https?:\/\/.*?\.(?:png|jpg))', firstpost.get('body'))

    #IF TAGGED POST WITH IMAGE IS FOUND

    if imageget:

        uri=imageget.group(0)

        #dl image to variable inram
        content = requests.get(uri).content

        #send to google to extract text and store responce annotations
        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        alltexts = response.text_annotations
        imagetext = alltexts[0].description

        #IF NOT ERROR THEN POST OUR REBLOG

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        else:

            tumblrclient.reblog(botblog, id=firstpost['id'], reblog_key=firstpost['reblog_key'],
                    state='published', tags=['use tag alttextbot to get text from images'], comment=imagetext)

    time.sleep(30)
