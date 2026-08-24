#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime

def get_commits_today(fecha):
    cmd = f'git log --since="{fecha} 00:00:00" --until="{fecha} 23:59:59" --format="%h %s"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().split('\n') if result.stdout.strip() else []

def get_issues_closed_today(fecha):
    cmd = f'gh issue list --state closed --search "closed:{fecha}" --json number,title'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().split('\n') if result.stdout.strip() else []

def get_adrs():
    cmd = 'ls docs/adr/*.md 2>/dev/null | sort -V'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().split('\n') if result.stdout.strip() else []

def main():
    fecha = sys.argv[2] if len(sys.argv) > 2 else datetime.now().strftime('%Y-%m-%d')
    commits = get_commits_today(fecha)
    issues = get_issues_closed_today(fecha)
    adrs = get_adrs()
    
    print(f"## Cierre {fecha}")
    print(f"Commits: {len(commits)}")
    for c in commits:
        print(f"  - {c}")
    print(f"Issues: {len(issues)}")
    print(f"ADRs: {len(adrs)}")

if __name__ == '__main__':
    main()
