import subprocess
import sys
import os

def check_passphrase(passphrase, dogecoin_cli_path):

    dogecoin_command = [dogecoin_cli_path, '-debug', 'walletpassphrase', passphrase, '10']
    
    try:
        with subprocess.Popen(dogecoin_command, 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE, 
                              text=True) as process:
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                print("-------------------------------------------------------------")
                print(f"[+] Potential match: {passphrase}")
                print("-------------------------------------------------------------")
                sys.exit()
                #return True
            else:
                error_message = stderr.strip()
                if "Wallet is already unlocked" in error_message:
                    print(f"[+] Wallet already unlocked. Skipping: {passphrase}")
                elif "Invalid wallet passphrase" in error_message:
                    print(f"[-] Invalid passphrase: {passphrase}")
                    return False
                else:
                    #print(f"Error with passphrase '{passphrase}' | {error_message}")
                    print(f"[-] Invalid passphrase: '{passphrase}'")
                return False
    except OSError as e:
        print(f"[-] OS Error occurred: {e}")
    except ValueError as e:
        print(f"[-] Value Error: {e}")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        return False

def main(wordlist_filename, dogecoin_cli_path):
    if not os.path.exists(wordlist_filename):
        print(f"[-] Wordlist file {wordlist_filename} does not exist.")
        sys.exit(1)
    if not os.path.exists(dogecoin_cli_path):
        print(f"[-] dogecoin-cli not found at {dogecoin_cli_path}")
        sys.exit(1)

    with open(wordlist_filename, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if word:
                check_passphrase(word, dogecoin_cli_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dccc.py <wordlist_file> <path_to_dogecoin-cli>")
        sys.exit(1)
    
    main(sys.argv[1], sys.argv[2])
  
