from PIL import Image
from reportlab.pdfgen import canvas

def image_to_pdf(image_path, output_pdf):
    # Open the image file
    with Image.open(image_path) as img:
        # Get image dimensions
        img_width, img_height = img.size

        # Create a new PDF with the same dimensions as the image
        c = canvas.Canvas(output_pdf, pagesize=(img_width, img_height))
        c.drawInlineImage(image_path, 0, 0, width=img_width, height=img_height)

        # Save the PDF file
        c.save()

if __name__ == "__main__":
    input_image = input("Enter the path of the image file: ")
    output_file = input("Enter the name for the output PDF file (e.g. output.pdf): ")

    image_to_pdf(input_image, output_file)
    print(f"PDF saved as {output_file}")
