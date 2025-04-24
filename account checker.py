#!/usr/bin/env python3
# Hotmail Checker for Linux VPS with Title Updates
# Usage: ./checker.py (requires ~/hotmails.txt)

import os
import time
import random
import sys

# Configuration
ACCOUNTS_FILE = os.path.expanduser("~/hotmails.txt")
DELAY = 1  # seconds between checks

# Linux terminal control codes
class Term:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    
    @staticmethod
    def set_title(title):
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

def check_account(email, password):
    """Replace with actual Hotmail API call"""
    time.sleep(random.uniform(0.5, 1.5))
    return random.random() > 0.8  # 20% valid for demo

def main():
    # Verify accounts file
    if not os.path.exists(ACCOUNTS_FILE):
        print(f"{Term.RED}Error:{Term.END} Create ~/hotmails.txt with email:password lines")
        return

    # Load accounts
    with open(ACCOUNTS_FILE, 'r') as f:
        accounts = [line.strip() for line in f if ':' in line]
    
    if not accounts:
        print(f"{Term.RED}Error:{Term.END} No accounts found in {ACCOUNTS_FILE}")
        return

    valid = 0
    start_time = time.time()
    Term.set_title("Hotmail Checker by @qsecc | Starting...")

    for i, account in enumerate(accounts, 1):
        try:
            email, password = account.split(':', 1)
            
            # Update title with stats
            elapsed = time.time() - start_time
            cpm = int(i / max(1, elapsed/60))
            Term.set_title(
                f"CPM: {cpm} | Valid: {valid} | Checked: {i}/{len(accounts)} | @qsecc"
            )
            
            # Check account
            if check_account(email, password):
                valid += 1
                print(f"{Term.GREEN}[VALID]{Term.END} {email}:{password}")
            else:
                print(f"{Term.RED}[INVALID]{Term.END} {email}:{password}")
            
            time.sleep(DELAY)
            
        except Exception as e:
            print(f"{Term.YELLOW}[ERROR]{Term.END} {account} - {str(e)}")

    # Final update
    Term.set_title(f"Complete | Valid: {valid}/{len(accounts)} | @qsecc")
    print(f"\n{Term.BLUE}Done.{Term.END} Valid: {Term.GREEN}{valid}{Term.END}/{len(accounts)}")

if __name__ == "__main__":
    main()
