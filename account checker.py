import sys
import time
import requests
import random
import os
import ctypes
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Configuration
FILE_PATH = r"C:\Users\gtw2k\Downloads\Telegram Desktop\2814x fresh Mix.txt"
PROXY_URL = "https://www.sslproxies.org/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def set_window_title(title):
    """Set Windows console title using ctypes"""
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except:
        os.system(f'title {title}')

def get_proxies():
    try:
        print(Fore.WHITE + "[*] Fetching proxies..." + Fore.RESET)
        response = requests.get(PROXY_URL, headers={"User-Agent": USER_AGENT}, timeout=10)
        proxies = []
        
        if response.status_code == 200:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', {'class': 'table table-striped table-bordered'})
            for row in table.tbody.find_all('tr'):
                cols = row.find_all('td')
                if len(cols) >= 2:
                    ip = cols[0].text.strip()
                    port = cols[1].text.strip()
                    proxies.append(f"{ip}:{port}")
        
        print(Fore.GREEN + f"[+] Found {len(proxies)} proxies" + Fore.RESET)
        return proxies
    except Exception as e:
        print(Fore.RED + f"[-] Proxy error: {str(e)}" + Fore.RESET)
        return []

def check_hotmail(email, password, proxy=None):
    """Simplified Hotmail check - replace with actual implementation"""
    try:
        # Simulate check (replace with real API call)
        time.sleep(0.5)
        return random.random() > 0.8  # 20% chance of being "valid"
    except:
        return False

def main():
    try:
        # Set initial title
        set_window_title("Hotmail Checker by @qsecc | Loading...")
        
        # Load accounts
        try:
            with open(FILE_PATH, 'r', encoding='utf-8', errors='ignore') as f:
                accounts = [line.strip() for line in f if ":" in line]
            
            if not accounts:
                print(Fore.RED + "[-] No valid accounts found in file" + Fore.RESET)
                return
        except Exception as e:
            print(Fore.RED + f"[-] Failed to load accounts: {str(e)}" + Fore.RESET)
            return

        proxies = get_proxies()
        valid_count = 0
        start_time = time.time()
        
        for i, account in enumerate(accounts, 1):
            try:
                email, password = account.split(':', 1)
                
                # Update title
                elapsed = time.time() - start_time
                cpm = int(i / max(1, elapsed/60))
                set_window_title(f"CPM: {cpm} | Valid: {valid_count} | Checked: {i}/{len(accounts)} | @qsecc")
                
                # Perform check
                if check_hotmail(email, password):
                    valid_count += 1
                    # Only show NA accounts (comment this line to show valid ones)
                    continue
                
                # Show only NA accounts
                print(Fore.RED + f"[NA] {email}:{password}")
                
                # Small delay to avoid rate limiting
                time.sleep(0.3)
                
            except ValueError:
                continue
            except Exception as e:
                print(Fore.YELLOW + f"[!] Error: {str(e)}" + Fore.RESET)
                continue

        print(Fore.CYAN + f"\n[+] Check complete. Valid: {valid_count}/{len(accounts)}" + Fore.RESET)
        set_window_title(f"Complete | Valid: {valid_count}/{len(accounts)} | @qsecc")

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Stopped by user" + Fore.RESET)
    finally:
        set_window_title("Hotmail Checker - Closed")

if __name__ == "__main__":
    main()