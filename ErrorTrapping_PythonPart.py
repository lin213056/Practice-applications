import sys
import re

def check_valid_triangles(input_string):
    match = re.search(r'valid triangles', input_string)
    if match:
        return f"Matched: {match.group(0)}"
    else:
        return "No match found"

if __name__ == "__main__":
    input_string = sys.argv[1]
    output_file = sys.argv[2]
    result = check_valid_triangles(input_string)
    
    with open(output_file, 'w') as file:
        file.write(result)