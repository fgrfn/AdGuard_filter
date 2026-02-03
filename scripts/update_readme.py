#!/usr/bin/env python3
"""
Script to automatically update README.md based on whitelist.txt categories
"""

import re
from pathlib import Path


def parse_whitelist(whitelist_path: Path) -> list[tuple[str, str]]:
    """Parse whitelist.txt and extract categories with descriptions"""
    categories = []
    current_category = None
    
    with open(whitelist_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Check if it's a comment (category header)
            if line.startswith('#') and not line.startswith('##'):
                category_name = line.lstrip('#').strip()
                if category_name:
                    current_category = category_name
    
    # Define category mappings with descriptions
    category_map = {
        'Apple': 'iCloud, iTunes, App Store, System Updates',
        'Apple Services & Updates': None,  # Skip, covered by Apple
        'Apple Domains': None,  # Skip, covered by Apple
        'GitHub Copilot / Microsoft': 'GitHub, Copilot, Visual Studio, Azure',
        'Microsoft': 'GitHub, Copilot, Visual Studio, Azure',
        'OpenAI / ChatGPT': 'ChatGPT, API Services',
        'OpenAI': 'ChatGPT, API Services',
        'Microsoft Services': 'Live, Office 365, Windows Updates',
        'CDNs (Content Delivery Networks)': 'Cloudflare, Akamai, Fastly',
        'CDNs': 'Cloudflare, Akamai, Fastly',
        'Google Services': 'Google APIs, YouTube',
        'Google': 'Google APIs, YouTube',
        'Development Tools': 'Firefox, Docker, npm',
        'VPN': 'Private Internet Access',
    }
    
    # Read file again to get actual categories
    with open(whitelist_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all comment headers
    seen_categories = {}
    for line in content.split('\n'):
        if line.startswith('#') and not line.startswith('##'):
            category = line.lstrip('#').strip()
            if category:
                # Map to standardized category
                for key, desc in category_map.items():
                    if key.lower() in category.lower() or category.lower() in key.lower():
                        if desc and key not in seen_categories:
                            seen_categories[key] = desc
                        break
    
    return list(seen_categories.items())


def update_readme(readme_path: Path, categories: list[tuple[str, str]]):
    """Update the README.md with the extracted categories"""
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Build the categories section
    categories_text = "## 📦 Included Categories\n\n"
    for name, description in categories:
        categories_text += f"- **{name}**: {description}\n"
    
    # Replace the categories section
    pattern = r'## 📦 Included Categories\n\n(?:- \*\*.*?\n)+'
    new_content = re.sub(pattern, categories_text, content)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated README.md with {len(categories)} categories")


def main():
    # Get paths
    root = Path(__file__).parent.parent
    whitelist_path = root / 'whitelist.txt'
    readme_path = root / 'README.md'
    
    # Check if files exist
    if not whitelist_path.exists():
        print(f"❌ Error: {whitelist_path} not found")
        return
    
    if not readme_path.exists():
        print(f"❌ Error: {readme_path} not found")
        return
    
    # Parse and update
    categories = parse_whitelist(whitelist_path)
    update_readme(readme_path, categories)


if __name__ == '__main__':
    main()
