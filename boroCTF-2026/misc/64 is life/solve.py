import os
import base64

def main():
    # Get the current working directory
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd,"boroCTF-2026", "misc", "64 is life", "file", "64", "ctf_chunks"))
    cwd = os.getcwd()
    
    # Rename files to their base64-decoded names when possible
    for name in sorted(os.listdir(cwd)):
        src = os.path.join(cwd, name)
        try:
            decoded = base64.b64decode(name).decode()
        except Exception:
            # leave name unchanged if it isn't valid base64/text
            continue

        # sanitize decoded name to avoid directory traversal or separators
        safe_name = decoded.replace(os.sep, "_").replace("..", "__")
        dst = os.path.join(cwd, safe_name)

        # avoid overwriting existing files: append a counter if needed
        if os.path.exists(dst):
            base, ext = os.path.splitext(safe_name)
            i = 1
            while True:
                candidate = f"{base}_{i}{ext}"
                dst = os.path.join(cwd, candidate)
                if not os.path.exists(dst):
                    break
                i += 1

        try:
            os.rename(src, dst)
            print(f"Renamed: {name} -> {os.path.basename(dst)}")
        except Exception as e:
            print(f"Failed to rename {name}: {e}")

    # Open files and concatenate their contents
    concatenated_text = ""
    for name in sorted(os.listdir(cwd)):
        filepath = os.path.join(cwd, name)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    concatenated_text += f.read()
            except Exception as e:
                print(f"Failed to read {name}: {e}")
    
    print("\n--- Concatenated Content ---")
    print(concatenated_text)

if __name__ == "__main__":
    main()