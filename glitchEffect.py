import cv2
import numpy as np
import random

def glitch_effect(image_path, intensity=10):
    
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or unable to read.")

    height, width, _ = img.shape

    # Make a copy to modify
    glitched = img.copy()

    # Shift random rows horizontally
    # The number of shifts is based on the intensity parameter.
    for _ in range(intensity * 10):
        row = random.randint(0, height - 1)
        offset = random.randint(-50, 50)
        # np.roll shifts the row data by offset
        glitched[row, :] = np.roll(glitched[row, :], offset, axis=0)

    # Swap color channels to create an unusual color effect (swaps red and blue channels)
    glitched = glitched[:, :, [2, 1, 0]]

    # Add noise to a random region
    noise_region_size = 50  # dimensions of the noise block
    noise = np.random.randint(0, 256, (noise_region_size, noise_region_size, 3), dtype=np.uint8)
    # Ensure the random region is fully within image boundaries
    x = random.randint(0, width - noise_region_size)
    y = random.randint(0, height - noise_region_size)
    glitched[y:y + noise_region_size, x:x + noise_region_size] = noise

    return glitched

if __name__ == "__main__":
    # Replace 'your_image.jpg' with the path to your input image.
    input_image = "image.png"
    output_image = "glitched_image.jpg"
    
    # Set desired intensity (increase for more glitch effects)
    intensity = 20

    # Apply the glitch effect
    try:
        glitched = glitch_effect(input_image, intensity)
    except Exception as e:
        print("Error:", e)
        exit(1)

    # Save the resulting image
    success = cv2.imwrite(output_image, glitched)
    if success:
        print(f"Glitched image saved as {output_image}")
    else:
        print("Failed to save the glitched image.")
