# Basic Android RE 1

#### Difficulty: <code>Easy</code>

#### Description
> A simple APK, reverse engineer the logic, recreate the flag, and submit!

#### 1.
> I had to look up some tools to assist with this one. I found an apk decompiler called jadx and found that the APK had a function for creating the flag. There was an md5 hashed value that I looked into decrypting but that just led to a site that helps with reversing the hash. Then I added the unhashed value to the flag format in the Java program. 

[Basic Android RE 1](basic_androidre1.png)