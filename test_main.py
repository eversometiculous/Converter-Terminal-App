import os
import pytest
import subprocess

# Test the main.py script
def test_main():
    # Define test input and output files
    input_file = 'test.pdf'
    output_file = 'test1.html'

    # Run the main.py script with the test input and output files
    subprocess.run(['python', 'main.py', input_file, 'html', output_file])

    # Check if the output file was created
    assert os.path.exists(output_file)

    # Check if the output file is not empty
    assert os.path.getsize(output_file) > 0

    # Clean up the output file after the test
    os.remove(output_file)
