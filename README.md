# Motivational Meme Generator

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes,
including an image with an overlaid quote.

### Overview

This application interact (load, manipulate, and save images) with a variety of complex filetypes (PDF, Word Documents,
CSVs, Text files).
Accept dynamic user input through a command-line tool and a web service.

## How to start

### Flask mode:

Clone a repository to your location:
```
https://github.com/BialyMT92/mem_generator.git
```
Install necessary requirements:
```
pip install -r /path/to/requirements.txt
```
Run app.py in your location and wait till flask will do the job:
```
python3 /path/to/app.py
```
### Command Line 
Copy steps from Flask mode without running app.py.
Open command line instead, move to location of the repo and run:
```
python3 /path/to/meme.py --path x --body y --author z
```
where:
```
x - path to img
y - body text
z - author of the text
```

## Detailed description of the module

Program is able to grab any image and ingest any text with an author onto this image. Output file will be saved under
.tmp file when using command line or .static when using flask.

### QuoteEngine

This module is responsible mainly for handling with variety of text files from which we can grab an add text to our
images.

### MemeGenerator

This is main engine where images and texts are concated together.

### app.py

This file is responsible for deploying Flask module.

### meme.py

With this file we can interact using command console.