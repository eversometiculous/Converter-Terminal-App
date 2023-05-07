# Import the packages needed to create this application
import argparse
import os
import markdown
import pdfkit
import PyPDF2
import html2text

# Create the formats with their extensions

formats = {
    'markdown': 'md',
    'html': 'html',
    'pdf': 'pdf'
}

parser = argparse.ArgumentParser(description="Converts between document formats") #default coding for argparse
parser.add_argument("input_file", help="the input file name to convert")
parser.add_argument("output_format", choices=formats.keys(), help="the output format or extension you want")
parser.add_argument("output_file", help="the output file name")


args = parser.parse_args() # Default coding for argparse

input_format = None
for format, ext in formats.items():
    if args.input_file.endswith("." + ext):
        input_format = format
        break

if input_format is None:
    raise ValueError(f"Unsupported input file format: {args.input_file}")

output_format = args.output_format

if args.output_file.endswith("." + formats[output_format]):
    output_file = args.output_file
else:
    output_file = args.output_file + "." + formats[output_format]

with open(args.input_file, "r") as f:
    input_data = f.read()

if input_format == "markdown" and output_format == "html":
    output_data = markdown.markdown(input_data)
elif input_format == "markdown" and output_format == "pdf":
    output_data = pdfkit.from_string(markdown.markdown(input_data), False)
elif input_format == "pdf" and output_format == "markdown":
    with open(args.input_file, "rb") as f:
        pdf = PyPDF2.PdfFileReader(f)
        output_data = "\n".join([pdf.getPage(i).extractText() for i in range(pdf.getNumPages())])
    output_data = html2text.html2text(output_data)
elif input_format == "pdf" and output_format == "html":
    with open(args.input_file, "rb") as f:
        pdf = PyPDF2.PdfFileReader(f)
        output_data = "<br>".join([pdf.getPage(i).extractText() for i in range(pdf.getNumPages())])
    output_data = f"<html><body>{output_data}</body></html>"