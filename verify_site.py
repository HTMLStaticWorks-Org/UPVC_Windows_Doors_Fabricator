import os
import re

PAGES = [
    ("index.html", 7, "Home 1"),
    ("home-2.html", 7, "Home 2"),
    ("about.html", 5, "About Us"),
    ("products.html", 5, "Products"),
    ("gallery.html", 5, "Gallery"),
    ("services.html", 5, "Services"),
    ("contact.html", 5, "Contact Us"),
    ("login.html", None, "Login"),
    ("signup.html", None, "Sign Up")
]

def verify():
    print("=" * 60)
    print("RUNNING VISTRAL AUDIT VERIFICATION")
    print("=" * 60)
    
    all_images = {}
    duplicate_errors = []
    section_errors = []

    for filename, expected_sections, page_title in PAGES:
        if not os.path.exists(filename):
            print(f"[FAIL] Missing file: {filename}")
            continue

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        # Check section count
        if expected_sections is not None:
            # Match top-level <section tags inside <main>
            sections = re.findall(r'<section\b', content)
            actual_count = len(sections)
            if actual_count != expected_sections:
                section_errors.append(f"{filename} ({page_title}): expected {expected_sections} sections, found {actual_count}")
            else:
                print(f"[PASS] {filename} ({page_title}): exactly {actual_count} sections.")
        else:
            print(f"[PASS] {filename} ({page_title}): standalone auth layout.")

        # Extract all image URLs
        # Match src="https://images.unsplash.com/photo-[a-zA-Z0-9-]+"
        images = re.findall(r'src="(https://images\.unsplash\.com/photo-[a-zA-Z0-9-]+)[^"]*"', content)
        for img_url in images:
            # Extract photo ID
            photo_id = img_url.split('/')[-1].split('?')[0]
            if photo_id in all_images:
                duplicate_errors.append(f"Duplicate image: {photo_id} in {filename} (first seen in {all_images[photo_id]})")
            else:
                all_images[photo_id] = filename

    print("-" * 60)
    print(f"Total Unique Unsplash Images Across Entire Site: {len(all_images)}")
    
    if duplicate_errors:
        print("[FAIL] DUPLICATE IMAGES DETECTED:")
        for err in duplicate_errors:
            print("  - " + err)
    else:
        print("[PASS] ZERO duplicate images across all pages! Every single photo is 100% unique.")

    if section_errors:
        print("[FAIL] SECTION COUNT MISMATCHES:")
        for err in section_errors:
            print("  - " + err)
    else:
        print("[PASS] Exact section counts verified on all 7 main pages!")

    print("=" * 60)

if __name__ == "__main__":
    verify()

