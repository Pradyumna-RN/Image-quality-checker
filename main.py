import cv2
import os

def classify_blur(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        return "Could not read image."
    laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
    if laplacian_var < 100:
        return "Blurry"
    elif laplacian_var < 300:
        return "Moderate"
    else:
        return "Clear"

if __name__ == "__main__":
    # Set the directory to search for images
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(script_dir, "input")

    # List of supported image extensions
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

    while True:
        image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(image_extensions)]

        if not image_files:
            print("No image files found in the 'input' folder.")
            break

        print("\nImage files in the 'input' folder:")
        for idx, image_file in enumerate(image_files, start=1):
            print(f"{idx}. {image_file}")
        print("0. Exit")

        try:
            choice = int(input("Enter the number of the image to analyze (or 0 to exit): "))
            if choice == 0:
                print("\nExiting the program.")
                break
            elif 1 <= choice <= len(image_files):
                selected_image = image_files[choice - 1]
                image_path = os.path.join(image_dir, selected_image)
                result = classify_blur(image_path)
                print(f"\nResult for '{selected_image}': {result}")
            else:
                print("\nInvalid selection. Please choose a number from the list.")
        except ValueError:
            print("\nPlease enter a valid number.")
