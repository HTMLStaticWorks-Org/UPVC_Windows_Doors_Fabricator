import os
import re

html_files = [f for f in os.listdir(".") if f.endswith(".html")]

print("Checking internal links across HTML files...")
broken_links = []

for filename in html_files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all hrefs
    hrefs = re.findall(r'href="([^"#][^"]*)"', content)
    for href in hrefs:
        # Ignore external links, mailto, tel
        if href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:"):
            continue
        
        target_file = href.split("?")[0].split("#")[0]
        if target_file and not os.path.exists(target_file):
            broken_links.append(f"{filename} links to non-existent file: {target_file}")

if broken_links:
    print("[FAIL] Broken links found:")
    for b in broken_links:
        print("  - " + b)
else:
    print("[PASS] All internal file links are valid and exist on disk!")

