from PIL import Image
from tkinter import filedialog
from django.forms import FilePathField

def encrypt_image(file_path, key):
    
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    # Check if the user has selected a file
    if file_path:
    # Open the image using Pillow
        img = Image.open(file_path)

    #img = Image.open(image_path)
    width, height = img.size
    
    encrypted_img = Image.new(img.mode, (width, height))
    
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            encrypted_pixel = tuple(p ^ key for p in pixel)  # XOR each pixel value with the key
            encrypted_img.putpixel((x, y), encrypted_pixel)
    
    return encrypted_img

def decrypt_image(encrypted_img, key):
    
    width, height = encrypted_img.size
    
    decrypted_img = Image.new(encrypted_img.mode, (width, height))
    
    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = tuple(p ^ key for p in encrypted_pixel)  # XOR each pixel value with the key
            decrypted_img.putpixel((x, y), decrypted_pixel)
    
    return decrypted_img



#image_path = "Image.jpg"
key = 50

# Encrypt the image
encrypted_image = encrypt_image(FilePathField, key)
encrypted_image.show()  # Display the encrypted image

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, key)
decrypted_image.show()  # Display the decrypted image
