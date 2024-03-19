import os
import hashlib
import subprocess

def calc_checksum(file_path, hash_algo):
  hash_obj = hashlib.new(hash_algo)
  with open(file_path, 'rb') as f:
    while chunk := f.read(4096):
      hash_obj.update(chunk)
  return hash_obj.hexdigest()

def walk_files(folder_path, hash_algo):
  checksums = {}
  for root, files in os.walk(folder_path):
    for file_name in files:
      file_path = os.path.join(root, file_name)
      checksum = calc_checksum(file_path, hash_algo)
      checksums[checksum] = file_name
  return checksums

def run_shell_script(script_path, args):
  command = ["bash", script_path] + args
  subprocess.run(command)

if __name__ == "__main__":
  folder_path = ".../files"
  script_path = ".../decrypt.sh"
  hash_algo = 'sha256'

  f =  open('.../checksum.txt', 'r')
  flag_checksum = f.read().strip()
  
  checksums = walk_files(folder_path, hash_algo)
  args = [checksums[flag_checksum]]
  run_shell_script(script_path, args)