from PIL import Image
import base64

def embed_html(image_path, html_content, output_path):
    # Encode the HTML content to base64
    encoded_html = base64.b64encode(html_content.encode()).decode()

    # Open the image
    img = Image.open(image_path)

    # Save the image with the embedded data
    img.save(output_path, format='PNG')

    # Save the encoded HTML content to a file
    with open(output_path, 'a') as f:
        f.write(encoded_html)

if __name__ == "__main__":
    image_path = 'website.png'
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Clickable Image</title>
        <style>
            img {
                cursor: pointer;
            }
        </style>
        <script>
            function openURL() {
                window.open("https://www.yourwebsite.com", "_blank");
            }
        </script>
    </head>
    <body>
        <img src="data:image/png;base64,%s" alt="Clickable Image" onclick="openURL()">
    </body>
    </html>
    ''' % base64.b64encode(open(image_path, 'rb').read()).decode()
    output_path = 'panda_image.png'
    embed_html(image_path, html_content, output_path)