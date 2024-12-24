from PIL import Image

def embed_link(image_path, output_path, hidden_data):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()

    # Convert the hidden data to binary
    binary_data = ''.join(format(ord(char), '08b') for char in hidden_data)
    data_len = len(binary_data)

    # Modify the pixels to store the binary data
    data_index = 0
    for y in range(image.height):
        for x in range(image.width):
            if data_index < data_len:
                r, g, b = pixels[x, y]
                # Modify the red channel to store 1 bit of binary data
                new_r = (r & ~1) | int(binary_data[data_index])
                pixels[x, y] = (new_r, g, b)
                data_index += 1

    # Save the image with the hidden data
    image.save(output_path)
    print(f"Data embedded successfully into {output_path}")

# Example usage
embed_link(
    image_path='original_image.png', 
    output_path='image_with_link.png', 
    hidden_data='http://127.0.0.1:5000/christmas_greetings.txt'
)
