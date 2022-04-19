"""
text = u"おはようございます。"
tb = TextBlob(text)
translated = tb.translate(to="en")
print(translated)"""

#Importing needed packages
from textblob import TextBlob
import pytesseract
import argparse
import cv2

#constructing argument parser and parsing the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#                 help="path to input image to be OCR'd")
# ap.add_argument("-l", "--lang", type=str, default="es",
#                 help="language to translate OCR'd text to (default is Spanish)")
# args = vars(ap.parse_args())

#loading the input image and converting it from BGR to RGB channels
# image = cv2.imread(args["--image""picture.jpg"])
image = cv2.imread("picture.jpg")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Using Tesseract to OCR the image, then replace newline characters
text = pytesseract.image_to_string(rgb)
text = text.replace("\n", " ")

#Show the original OCR'd text
print("ORIGINAL")
print("========")
print(text)
print("")

#Translating the string to the desired language
tb = TextBlob(text)
# translated = tb.translate(to=args["lang"])
translated = tb.translate(from_lang="en", to="es")

#show the translated text
print("TRANSLATED")
print("==========")
print(translated)