#!/usr/bin/env python3

import face_recognition
import pornhub
import urllib.request as urllib
import io
import sys

client = pornhub.PornHub()

image_input = str(sys.argv[1])
loaded = face_recognition.load_image_file(image_input)
encoding_of_input = face_recognition.face_encodings(loaded)[0]
i = 0
accuracy = 0.55
number_of_stars = 3000

for star in client.getStars(number_of_stars):
    i += 1
    try:
        url_open = urllib.urlopen(str((star["photo"])))
        read_bytes = io.BytesIO(url_open.read())
        pornstar_img = face_recognition.load_image_file(read_bytes)
        encoding_of_pornstar = face_recognition.face_encodings(pornstar_img)[0]
        results = face_recognition.compare_faces([encoding_of_input],encoding_of_pornstar, tolerance=accuracy)
        print("Currently testing [{0}]: {1}".format(str(i), star["name"]))
        if results[0]:
            print("+++ Found a match +++")
            print(str("https://www.pornhub.com/pornstar/" + (str((star["name"])).replace(" ", "-"))).lower() )
            break
    except:
        pass


