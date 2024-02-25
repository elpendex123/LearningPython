def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Read each line from the input file
        for line_number, line in enumerate(infile, start=1):
            # Format the line number to four digits
            formatted_line_number = f'{line_number:04d}'

            # Combine the formatted line number with the rest of the line
            modified_line = f'{formatted_line_number} {line}'

            # Write the modified line to the output file
            outfile.write(modified_line)


# Replace 'input.txt' and 'output.txt' with your actual file names
add_line_numbers('input.txt', 'output.txt')
