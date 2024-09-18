from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

def manipulate_image(image_path):
    # Debugging: Print the image path
    print(f"Image path: {image_path}")
    
    try:
        # Load the image
        original_image = Image.open(image_path)

        # 1. Color Inversion
        inverted_image = Image.eval(original_image, lambda x: 255 - x)
        inverted_image.save('inverted_image.png')

        # 2. Brightness Adjustment
        enhancer = ImageEnhance.Brightness(original_image)
        bright_image = enhancer.enhance(1.5)  # Increase brightness
        bright_image.save('bright_image.png')

        # 3. Blurring
        blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=5))
        blurred_image.save('blurred_image.png')

        # 4. Resizing
        resized_image = original_image.resize((int(original_image.width * 0.5), int(original_image.height * 0.5)))
        resized_image.save('resized_image.png')

        # 5. Rotating
        rotated_image = original_image.rotate(45)  # Rotate by 45 degrees
        rotated_image.save('rotated_image.png')

        # 6. Thresholding
        thresholded_image = original_image.convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        thresholded_image.save('thresholded_image.png')

        # 7. Drawing Shapes
        shape_image = original_image.copy()
        draw = ImageDraw.Draw(shape_image)
        draw.rectangle([10, 10, 100, 100], outline="red", fill=None)  # Draw a red rectangle
        draw.ellipse([150, 150, 250, 250], outline="blue", fill=None)  # Draw a blue circle
        shape_image.save('shapes_image.png')

        # 8. Pixelation
        pixelated_image = original_image.resize((int(original_image.width / 10), int(original_image.height / 10)), Image.NEAREST)
        pixelated_image = pixelated_image.resize(original_image.size, Image.NEAREST)
        pixelated_image.save('pixelated_image.png')

        print("Image manipulations complete! Outputs saved.")

    except FileNotFoundError:
        print("Error: The specified image file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
image_path = r'C:\Users\HP\Pictures\Screenshots\DFT2.png'  # Change to your input image path
manipulate_image(image_path)