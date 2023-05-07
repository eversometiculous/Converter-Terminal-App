# Import the packages needed to create this application
import argparse
import os
import markdown
import pdfkit
import PyPDF2
import html2text

# Create the formats with their extensions

FORMATS = {
    'markdown': 'md',
    'html': 'html',
    'pdf': 'pdf'
}

parser = argparse.ArgumentParser(description="Converts between document formats") #default coding for argparse
parser.add_argument("input_file", help="the input file name to convert")
parser.add_argument("output_format", choices=FORMATS.keys(), help="the output format or extension you want")
parser.add_argument("output_file", help="the output file name")


args = parser.parse_args() # Default coding for argparse

