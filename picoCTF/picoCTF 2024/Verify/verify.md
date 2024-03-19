# Verify

#### Tags: Forensics, browser_webshell_solvable, checksum, grep

#### Description
> People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and decrypt script to help you know that my flags are legitimate.  

#### 1. 
> The script I put together was a pain, but I was able to use it to iterate through the files and compare the hashes with the one provided. Then run the .sh script to get the flag. If you are going to do this method as well, remember to edit file paths inside the bash script as well. File paths have been muted for privacy. The files folder has been removed to save storage. 

#### 2. 
> Learned the basics for hashlib for doing this script. The basic functions for using hashlib like new(), update(), and hexdigest() for return hashes to for the files we went through. 

``` python
import hashlib
  def calc_checksum(file_path, hash_algo):
    hash_obj = hashlib.new(hash_algo)
    with open(file_path, 'rb') as f:
      while chunk := f.read(4096):
        hash_obj.update(chunk)
    return hash_obj.hexdigest()
```

#### 3. 
> For os library, we were able to use it to get the file paths for the script and files we were feeding into the function above for calculating the hashes. 

``` python
  ...
  for root, files in os.walk(folder_path):
    for file_name in files:
      file_path = os.path.join(root, file_name)
      ...
```

#### 4. 
> Lastly for subprocess, to run scripts from a python script. Pretty straightfoward, give it the path for the script to run, and the arguments if the script requires it. 

``` python
import subprocess
  def run_shell_script(script_path, args):
    command = ["bash", script_path] + args
    subprocess.run(command)
```