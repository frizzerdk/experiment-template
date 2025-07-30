#!/usr/bin/env python3
"""Sync markdown files using natural markdown structure from experiment_info.yaml."""

import yaml
import re
from pathlib import Path

def load_experiment_info():
    """Load experiment metadata from YAML file."""
    with open('experiment_info.yaml', 'r') as f:
        return yaml.safe_load(f)

def sync_readme(info):
    """Sync README.md using markdown structure patterns."""
    readme_path = Path('README.md')
    if not readme_path.exists():
        return
    
    content = readme_path.read_text()
    
    # Update title (first # line)
    content = re.sub(r'^# .*', f'# {info["name"]}', content, flags=re.MULTILINE)
    
    # Update description (first paragraph after title, before next ##)
    content = re.sub(
        r'(^# .*\n\n)(.*?)(\n\n## )',
        rf'\1{info["description"]}\3',
        content,
        flags=re.MULTILINE | re.DOTALL
    )
    
    # Update specific fields by their labels
    content = re.sub(r'\*\*Domain\*\*: .*', f'**Domain**: {info["domain"]}', content)
    content = re.sub(r'\*\*Status\*\*: .*', f'**Status**: {info["status"]}', content)
    
    # Update skills if available
    if info.get('skills_demonstrated'):
        skills = ', '.join(info['skills_demonstrated'])
        content = re.sub(r'\*\*Key Skills\*\*: .*', f'**Key Skills**: {skills}', content)
    
    readme_path.write_text(content)
    print("✅ Synced README.md using markdown structure")

if __name__ == "__main__":
    try:
        info = load_experiment_info()
        sync_readme(info)
        print(f"📄 Synced: {info['name']} ({info['domain']}, {info['status']})")
    except Exception as e:
        print(f"❌ Error syncing files: {e}") 