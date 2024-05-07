# https://python-pillow.org/

from PIL import Image
import random

class ImageOverlay:
    '''
    A class to overlay multiple images onto a base image using the Pillow (PIL) library for image manipulation.
    
    Attributes:
        base_img (PIL.Image.Image): The base image onto which the overlay images will be placed.
        overlay_img_paths (list): A list of file paths to the overlay images.
    '''

    def __init__(self, base_image_path, overlay_image_paths):
        '''
        Initializes the ImageOverlay object.
        
        Args:
            base_image_path (str): The file path to the base image.
            overlay_image_paths (list): A list of file paths to the overlay images.
        '''
        self.base_img = self.open_image(base_image_path)
        if self.base_img:
            self.overlay_img_paths = [path for path in overlay_image_paths if self.open_image(path)]
            if self.overlay_img_paths:
                self.overlay_images()
            else:
                print("No valid overlay images found.")
        else:
            print("Invalid base image path.")

    def open_image(self, image_path):
        '''
        Opens an image file using Pillow (PIL) library.

        Args:
            image_path (str): The file path to the image.

        Returns:
            PIL.Image.Image: The opened image.
        '''
        try:
            with Image.open(image_path) as img:
                return img.copy()
        except Exception as e:
            print(f"Error opening image {image_path}: {e}")
            return None

    def overlay_images(self):
        '''
        Overlays the images onto the base image.
        '''
        # Resize base image
        width, height = self.base_img.size
        new_width = int(width * 1.4)
        new_height = int(height * 1.4)
        self.base_img = self.base_img.resize((new_width, new_height))

        # Calculate the size of overlay images
        overlay_width = int(new_width * 0.5)
        overlay_height = int(new_height * 0.5)

        # Loop through overlay images and randomly place them on the base image
        for overlay_img_path in self.overlay_img_paths:
            # Open the overlay image
            overlay_img = self.open_image(overlay_img_path)
            if overlay_img:
                # Resize overlay image
                overlay_img = self.resize_with_aspect_ratio(overlay_img, overlay_width, overlay_height)

                # Paste the overlay image on the base image
                x = random.randint(0, new_width - overlay_img.width)
                y = random.randint(0, new_height - overlay_img.height)
                self.base_img.paste(overlay_img, (x, y), overlay_img)

    def resize_with_aspect_ratio(self, img, new_width, new_height):
        '''
        Resizes an image while maintaining its aspect ratio.

        Args:
            img (PIL.Image.Image): The image to be resized.
            new_width (int): The desired width of the resized image.
            new_height (int): The desired height of the resized image.

        Returns:
            PIL.Image.Image: The resized image.
        '''
        width, height = img.size
        aspect_ratio = width / height

        if width > height:
            new_height = int(new_width / aspect_ratio)
        else:
            new_width = int(new_height * aspect_ratio)

        return img.resize((new_width, new_height))

    def save(self, output_path):
        '''
        Saves the resulting image to a file.

        Args:
            output_path (str): The file path to save the resulting image.
        '''
        self.base_img.save(output_path)

    @staticmethod
    def check_image_format(image_path):
        '''
        Checks the format of an image file.

        Args:
            image_path (str): The file path to the image.

        Returns:
            str: The format of the image (e.g., 'jpeg', 'png').
        '''
        try:
            with Image.open(image_path) as img:
                return img.format.lower()
        except Exception as e:
            print(f"Error: {e}")
            return None

# Example usage
# base_image_path = "C:\\Users\\emerg\\OneDrive\\Documents\\_Mimir Cyber\\_Boyds Bar\\Articles\\_XYZ Articles\\Movie Reviews\\12 Strong.jpg"
# overlay_image_paths = ["C:\\Users\\emerg\\OneDrive\\Documents\\_Mimir Cyber\\_Boyds Bar\\Articles\\_XYZ Articles\\Stamps\\Dad Approved Stamp.png", 
#                        "C:\\Users\\emerg\\OneDrive\\Documents\\_Mimir Cyber\\_Boyds Bar\\Articles\\_XYZ Articles\\Stamps\\Mom Approved Stamp.png"]
# output_image_path = "C:\\Users\\emerg\\OneDrive\\Documents\\_Mimir Cyber\\Coding\\Personal Projects\\output_image.jpg"

# image_overlay = ImageOverlay(base_image_path, overlay_image_paths)
# if image_overlay.base_img:
#     image_overlay.save(output_image_path)
# else:
#     print("Error: Image overlay could not be created.")

# # Check image format
# print(ImageOverlay.check_image_format(output_image_path))