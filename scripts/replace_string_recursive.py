import os
import sys
import re
from pathlib import Path


def replace_case_sensitive(text, search, replace):
    # Replace exact case
    text = text.replace(search, replace)
    # Replace all-lowercase
    text = text.replace(search.lower(), replace.lower())
    # Replace all-uppercase
    text = text.replace(search.upper(), replace.upper())
    # Replace Capitalized
    if search and search[0].isupper():
        cap_search = search[0].upper() + search[1:].lower()
        cap_replace = replace[0].upper() + replace[1:].lower()
        text = text.replace(cap_search, cap_replace)
    return text


def process_file(filepath, search, replace, summary):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        # Skip binary or unreadable files
        return
    new_content = replace_case_sensitive(content, search, replace)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        summary['files_modified'].append(str(filepath))


def process_dir(root, search, replace, summary):
    # Walk bottom-up so we can rename folders after their contents
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        # Rename files
        for filename in filenames:
            old_path = Path(dirpath) / filename
            new_filename = replace_case_sensitive(filename, search, replace)
            new_path = Path(dirpath) / new_filename
            if new_filename != filename:
                os.rename(old_path, new_path)
                summary['files_renamed'].append((str(old_path), str(new_path)))
            else:
                new_path = old_path
            process_file(new_path, search, replace, summary)
        # Rename directories
        for dirname in dirnames:
            old_dir = Path(dirpath) / dirname
            new_dirname = replace_case_sensitive(dirname, search, replace)
            new_dir = Path(dirpath) / new_dirname
            if new_dirname != dirname:
                os.rename(old_dir, new_dir)
                summary['dirs_renamed'].append((str(old_dir), str(new_dir)))


def print_summary(summary):
    print("\nSummary:")
    print(f"Files with content replaced: {len(summary['files_modified'])}")
    for f in summary['files_modified']:
        print(f"  Modified: {f}")
    print(f"Files renamed: {len(summary['files_renamed'])}")
    for old, new in summary['files_renamed']:
        print(f"  {old} -> {new}")
    print(f"Directories renamed: {len(summary['dirs_renamed'])}")
    for old, new in summary['dirs_renamed']:
        print(f"  {old} -> {new}")


def main():
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} <target_dir> <search_string> <replace_string>")
        sys.exit(1)
    target_dir, search, replace = sys.argv[1:4]
    summary = {'files_modified': [], 'files_renamed': [], 'dirs_renamed': []}
    process_dir(target_dir, search, replace, summary)
    print_summary(summary)

if __name__ == "__main__":
    main()
