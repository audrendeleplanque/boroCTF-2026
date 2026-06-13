import os
import base64

def main():
    # Get the current working directory
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd,"boroCTF-2026", "misc", "64 is life", "file", "64", "ctf_chunks"))
    cwd = os.getcwd()
    
    # Print all files in the current working directory
    for name in sorted(os.listdir(cwd)):
        try:
            print(base64.b64decode(name).decode())
        except Exception:
            print(name)

if __name__ == "__main__":
    main()