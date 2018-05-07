# Steganography

User is able to encode the actual python code used for this project to an image by writing over the least significant bit of the RGB (red, green, blue) pixel values, and decode that python code from the image. This is a project for **CPSC 353 Security course**.

## Features
  * Text embedded inside images
  * Data embedded from the bottom right to the top left
  * Converts text to binary
  * Converts text length to binary
  * Use the bottom right 11 pixels to hide the text length
  * Use the remaining pixels to hide the text
  * Replace the least significant bit of the RGB values
  * Consumes jpeg image
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

`python index.py`

**TO DECODE:**
  * type `d` after menu prompt
  * type in the name of image. For example, `testImage.png`

**TO ENCODE:**
  * type `e` after menu prompt
  * type in the name of image without ext. For example, `testImage`
