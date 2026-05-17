"""
Image Resizer - Main module.
"""
import sys

VERSION = "0.2.0"

def run(args):
    """Main entry point."""
    print(f"Image Resizer v{VERSION}")
    if args:
        print(f"Processing: {', '.join(args)}")
        process(args)
    else:
        print("Usage: python image.py [arguments]")
        print("Try: python image.py --help")

def process(args):
    """Process input arguments."""
    records = []
    for arg in args:
        result = arg.strip()
        if result:
            records.append(result)
            print(f"  Processed: {result}")
    print(f"\nTotal: {len(records)} items processed")
    return records

def main():
    run(sys.argv[1:])

if __name__ == "__main__":
    main()
