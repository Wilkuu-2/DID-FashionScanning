from exif import Image


#example
exampleTag = {
        "focal_length": 3.67,
        "make": "logitech",
        "model": "Pro C920" 
        }



def setExif(path,tags):
    with open(path , "rb") as f:
        exifImage = Image(f)
    exifImage.make = tags["make"]
    exifImage.model = tags["model"]
    exifImage.focal_length = tags["focal_length"]

    with open(path, "wb") as nf:
        nf.write(exifImage.get_file())

