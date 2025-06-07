#!/usr/bin/env python3
from datetime import datetime

from contribute import is_contribution_day

def main():
    today = datetime.now()

    if is_contribution_day(today):
        with open('README.md', 'a') as readme:
            readme.write(f'\n* *Contributron* contributed on {today.strftime("%A, %d %B %Y at %I:%M%p")}.')
        
        print(f"Contribution added to README on {today.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"No contribution needed today ({today.strftime('%Y-%m-%d')}).")
    
if __name__ == "__main__":
    main()
