import os
import json

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directory containing the PGN files (same as script directory)
pgn_dir = script_dir

# Output file
output_file = os.path.join(pgn_dir, "pgn-files.js")

# Read all .pgn files from the directory
pgn_files = [f for f in os.listdir(pgn_dir) if f.endswith(".pgn")]

# Generate the PGN_FILES object
pgn_data = {}
for file_name in pgn_files:
    file_path = os.path.join(pgn_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        pgn_data[file_name] = file.read()

# Write the pgn-files.js file
with open(output_file, "w", encoding="utf-8") as output:
    output.write(f"const PGN_FILES = {json.dumps(pgn_data, indent=4)};\n")

print(f"Generated {output_file} with {len(pgn_files)} PGN files.")