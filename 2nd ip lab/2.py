import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Error: could not load image")
        exit()
    return image

def translate_image(image, tx, ty):
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    height, width = image.shape[:2]
    translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
    return translated_image

def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def scale_image(image, fx, fy):
    scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled_image

def main():
    image_path = input("Enter the image path: ")
    image = load_image(image_path)
    tx = int(input("Enter translation in x direction: "))
    ty = int(input("Enter translation in y direction: "))
    angle = float(input("Enter rotation angle (in degrees): "))
    scale_x = float(input("Enter scaling factor for x: "))
    scale_y = float(input("Enter scaling factor for y: "))
    translated = translate_image(image, tx, ty)
    rotated = rotate_image(image, angle)
    scaled = scale_image(image, scale_x, scale_y)
    cv2.imshow("Original Image", image)
    cv2.imshow("Translated Image", translated)
    cv2.imshow("Rotated Image", rotated)
    cv2.imshow("Scaled Image", scaled)
    save_option = input("Do you want to save the transformed images? (yes/no): ").strip().lower()
    if save_option == "yes":
        cv2.imwrite("translated_image.jpg", translated)
        cv2.imwrite("rotated_image.jpg", rotated)
        cv2.imwrite("scaled_image.jpg", scaled)
        print("Images saved successfully!")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
