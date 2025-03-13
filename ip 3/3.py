import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: could not load image")
        exit()
    return image

def apply_sobel(image):
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    sobel_combined = np.uint8(np.absolute(sobel_combined)) 
    return sobel_combined

def apply_laplacian(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian)) 
    return laplacian

def apply_canny(image, threshold1, threshold2):
    canny_edges = cv2.Canny(image, threshold1, threshold2)
    return canny_edges

def main():
    image_path = input("enter the image path:")
    image = load_image(image_path)
    sobel_edges = apply_sobel(image)
    laplacian_edges = apply_laplacian(image)
    canny_edges = apply_canny(image, 100, 200) 
    
    cv2.imshow('original image',image)
    cv2.imshow('Sobel edges',np.uint8(sobel_edges))
    cv2.imshow('Laplacian edges',np.uint8(laplacian_edges))
    cv2.imshow('Canny edges',canny_edges)
    
    save_option=input("Do you want to save the processes images? (yes/no):").strip().lower()
    if save_option=="yes":
        cv2.imwrite("sobel_edges.jpg",np.uint8(sobel_edges))
        cv2.imwrite("laplacian_edges.jpg",np.uint8(laplacian_edges))
        cv2.imwrite("canny_edges.jpg",canny_edges)
        print("Processed images saves succesfully!")
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
