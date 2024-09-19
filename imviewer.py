import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import os


def show_image(image_path):
    """
    Displays an image using Matplotlib.
    
    Parameters:
    - image_path (str): The path to the image file.
    """
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    try:
        img = mpimg.imread(image_path)
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.show()
    except Exception as e:
        print(f"Error: Could not load the image. {str(e)}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Command-line Image Viewer using Matplotlib")
    parser.add_argument("image_path", help="Path to the image file to view")
    
    # Parse arguments
    args = parser.parse_args()

    # Show the image
    show_image(args.image_path)

if __name__ == "__main__":
    main()
