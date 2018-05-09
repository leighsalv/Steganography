# Steganography

By: Leigh Salvador

User is able to encode the actual python code used for this project to a jpg image by writing over the least significant bit of the RGB (red, green, blue) pixel values. Then, the secret message (python code) is decoded from the image using the exported png file. This is a project for **CPSC 353 Security course**.

## Features
  * Text embedded inside images
  * Data embedded from the bottom right to the top left
  * Converts text to binary
  * Converts text length to binary
  * Use the bottom right 11 pixels to hide the text length
  * Use the remaining pixels to hide the text
  * Replace the least significant bit of the RGB values
  * Consumes jpg image
  * Exports png image
  * Extract text length from image
  * Extract text from image

## Getting Started

**Clone** or **download** the repository.

## Install

`sudo easy_install pip`

`sudo pip install Pillow`

`sudo pip install image`

## Run In Terminal

`cd/directory-of-Steganography/Steganography-master` change _directory-of-Steganography_ to the directory in which you downloaded the repo.

Make sure that the images you will use is **inside** of the Steganography-master folder.

A sample .jpg and .png is provided called "pup.jpg", "pup.png", and "testImage.png" for testing purposes.

`python index.py`

**TO DECODE:**
  * type `d` after menu prompt
  * type in the name of .png image without ext. For example, `testImage`

**TO ENCODE:**
  * type `e` after menu prompt
  * type in the name of .jpg image without ext. For example, `testImage`
  * the program will then automatically export a new .png file with the encoded message inside the Steganography-master folder
