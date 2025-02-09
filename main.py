import sys
import argparse
from src.compiler import DeathNoteCompiler

def main():
    parser = argparse.ArgumentParser(description='Death Note Language Compiler')
    parser.add_argument('input_file', help='Path to the .dn source file')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    
    args = parser.parse_args()
    
    try:
        with open(args.input_file, 'r') as file:
            source_code = file.read()
            
        compiler = DeathNoteCompiler()
        if args.verbose:
            print(f"Compiling {args.input_file}...")
            
        result = compiler.compile(source_code)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(str(result))
            if args.verbose:
                print(f"Output written to {args.output}")
        
        if args.verbose:
            print("Compilation successful!")
            
    except FileNotFoundError:
        print(f"Error: Could not find file {args.input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error during compilation: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()