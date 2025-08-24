#!/usr/bin/env python3

import os
import sys
from pathlib import Path


def get_filename_from_user(prompt_message):
    while True:
        filename = input(prompt_message).strip()
        if filename:
            return filename
        print("❌ Filename cannot be empty. Please try again.")


def read_file_safely(filename):
    try:
        file_path = Path(filename)
        
        if not file_path.exists():
            print(f"❌ Error: File '{filename}' does not exist.")
            return None
            
        if not file_path.is_file():
            print(f"❌ Error: '{filename}' is not a valid file.")
            return None
            
        if not os.access(file_path, os.R_OK):
            print(f"❌ Error: No read permission for '{filename}'.")
            return None
            
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"✅ Successfully read {len(content)} characters from '{filename}'")
            return content
            
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to read '{filename}'.")
    except UnicodeDecodeError:
        print(f"❌ Error: Cannot decode '{filename}'. File might be binary or use different encoding.")
    except OSError as e:
        print(f"❌ Error: OS error occurred while reading '{filename}': {e}")
    except Exception as e:
        print(f"❌ Unexpected error while reading '{filename}': {e}")
    
    return None


def modify_text(content):
    return add_text_statistics(content)


def add_text_statistics(content):
    lines = content.split('\n')
    words = content.split()
    chars = len(content)
    chars_no_spaces = len(content.replace(' ', ''))
    
    paragraphs = len([line for line in lines if line.strip()]) - lines.count('')
    unique_words = len(set(word.lower().strip('.,!?";:()[]{}') for word in words if word.strip('.,!?";:()[]{}').isalpha()))
    longest_word = max(words, key=len, default="") if words else ""
    sentences = content.count('.') + content.count('!') + content.count('?')
    sentences = max(1, sentences)
    
    uppercase_content = content.upper()
    
    stats = f"""=== COMPREHENSIVE TEXT ANALYSIS ===
📄 Lines: {len(lines)}
📝 Words: {len(words)}
🔤 Characters (with spaces): {chars}
🔠 Characters (no spaces): {chars_no_spaces}
📋 Paragraphs: {max(1, paragraphs)}
🎯 Unique words: {unique_words}
📏 Longest word: "{longest_word}" ({len(longest_word)} chars)
📊 Average words per line: {len(words) / max(1, len(lines)):.1f}
📝 Average words per sentence: {len(words) / sentences:.1f}
🔄 Text converted to: UPPERCASE
=======================================

{uppercase_content}"""
    return stats


def write_file_safely(filename, content):
    try:
        file_path = Path(filename)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        if file_path.exists():
            response = input(f"⚠️  File '{filename}' already exists. Overwrite? (y/n): ").lower()
            if response not in ['y', 'yes']:
                print("✋ Write operation cancelled.")
                return False
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"✅ Successfully wrote {len(content)} characters to '{filename}'")
            return True
            
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to write to '{filename}'.")
    except OSError as e:
        print(f"❌ Error: OS error occurred while writing to '{filename}': {e}")
    except Exception as e:
        print(f"❌ Unexpected error while writing to '{filename}': {e}")
    
    return False


def main():
    print("🖋️ File Read & Write Challenge with Error Handling Lab")
    print("=" * 55)
    
    try:
        input_filename = get_filename_from_user("📂 Enter the filename to read: ")
        
        print(f"\n📖 Attempting to read '{input_filename}'...")
        content = read_file_safely(input_filename)
        
        if content is None:
            print("💔 Cannot proceed without valid file content.")
            return
        
        print(f"\n📋 Original content preview (first 200 chars):")
        print("-" * 50)
        print(content[:200] + ("..." if len(content) > 200 else ""))
        print("-" * 50)
        
        print(f"\n🔄 Adding comprehensive statistics and converting to uppercase...")
        modified_content = modify_text(content)
        
        default_output = f"modified_{Path(input_filename).name}"
        output_filename = input(f"\n💾 Enter output filename (or press Enter for '{default_output}'): ").strip()
        
        if not output_filename:
            output_filename = default_output
        
        print(f"\n📝 Writing modified content to '{output_filename}'...")
        success = write_file_safely(output_filename, modified_content)
        
        if success:
            print(f"\n🎉 Process completed successfully!")
            print(f"📊 Original file: '{input_filename}' ({len(content)} chars)")
            print(f"📊 Modified file: '{output_filename}' ({len(modified_content)} chars)")
        else:
            print("\n💔 File writing failed.")
            
    except KeyboardInterrupt:
        print("\n\n✋ Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error in main program: {e}")


if __name__ == "__main__":
    main()