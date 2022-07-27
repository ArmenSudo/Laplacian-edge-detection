import cv2
import sys
import laplacian_impl
import gause_blure_impl


def main(argv):
    # input image path
    path = argv[0] if len(argv) >= 1 else '____No___find____'  # input('Input image path: ')

    # loading image

    img = cv2.imread(f'image/{path}', cv2.IMREAD_COLOR)

    if img is None:
        print('Error opening image')
        print('Program Arguments: [image_name]')
        return -1

    # converting to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # remove noise
    img = gause_blure_impl.gaussian_blur(gray)

    # Laplacian edge detection
    laplacian_implement = laplacian_impl.laplacian(img)

    cv2.imwrite(f'edge_processing_image/new_lapl_{path}', laplacian_implement)

    abs_dst = cv2.convertScaleAbs(laplacian_implement)

    cv2.imshow("window_name", abs_dst)
    cv2.waitKey(0)


if __name__ == "__main__":
    main(sys.argv[1:])
