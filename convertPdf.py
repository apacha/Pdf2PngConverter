from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path(r'C:\Users\alpa\Dropbox\Doktorat\BMM Summer School\Transcript.pdf')
index = 0
for image in images:
    image.save("transcript-{0}.png".format(index))
    index += 1