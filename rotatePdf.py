import PyPDF2

def rotate_pdf(pdf_path, output_path, rotation_angle):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page.rotate(rotation_angle)
            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage
# Put target pdf file in the same folder
pdf_path = 'file_name.pdf'
output_path = 'file_name_rotated.pdf'
rotation_angle = 90  # Change this value to the desired rotation angle

rotate_pdf(pdf_path, output_path, rotation_angle)
