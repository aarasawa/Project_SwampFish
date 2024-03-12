# Forensics 101 - Easy

### Description: Flag is located in relation to the image provided.

### 1. 
> An image with a meme on it is provided to the user. Given that I do not know anything about forensics,
> I decided to google the basics. The article I came across taught me a couple of Linux commands that 
> provide a quick and easy way to analyze files for hidden information. 

### 2. 
> File: prints information on the file including its type, extension, size, color array, etc. \
> Results from File: no flag \
> Exiftool: reads and writes metadata in files \
> Output from Exiftool: no flag in metadata \
> XXD: tool to dump hexadecimal format of the file \
> Output from xxd: FLAG! \
> strings: prints strings at least 4 characters long from a file \
> Output from strings: FLAG!

### 3.
> Flag can be obtained from both running xxd and strings command on the file. 