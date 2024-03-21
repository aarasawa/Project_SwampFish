# CanYouSee

#### Tags: Forensics, browser_webshell_solvable

#### Description
> How about some hide and seek?

#### 1. 
> The flag is hidden in the metadata for the image. Using exiftools reveals that the image breaches exif specifications, so I moved to use strings. Then piped the output into a .txt and spotted that there was a base64 string tagged as resourceURL in the metadata at the top of the output file. I took a shot to decode it and it was the flag. 