import cv2 as cv
import numpy as np


def gaussOpenCV(img):
    return cv.GaussianBlur(img, (5, 5), 0)


def adaptiveMedian(image):
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    smax = 7
    m, n = smax, smax
    hImg = img.shape[0]
    wImg = img.shape[1]
    hPad = int((m - 1) / 2)
    wPad = int((n - 1) / 2)
    imgPad = np.pad(
        img.copy(), ((hPad, m - hPad - 1), (wPad, n - wPad - 1)), mode="edge"
    )

    imgAdaMedFilter = np.zeros(img.shape)

    for i in range(hPad, hPad + hImg):
        for j in range(wPad, wPad + wImg):
            # Adaptive median filter
            ksize = 3
            k = int(ksize / 2)
            pad = imgPad[i - k : i + k + 1, j - k : j + k + 1]
            zxy = img[i - hPad, j - wPad]
            zmin = np.min(pad)
            zmed = np.median(pad)
            zmax = np.max(pad)

            if zmin < zmed < zmax:
                if zmin < zxy < zmax:
                    imgAdaMedFilter[i - hPad, j - wPad] = zxy
                else:
                    imgAdaMedFilter[i - hPad, j - wPad] = zmed
            else:
                while True:
                    ksize += 2
                    if zmin < zmed < zmax or ksize > smax:
                        break
                    k = int(ksize / 2)
                    pad = imgPad[i - k : i + k + 1, j - k : j + k + 1]
                    zmin = np.min(pad)
                    zmed = np.median(pad)
                    zmax = np.max(pad)
                if zmin < zmed < zmax or ksize > smax:
                    if zmin < zxy < zmax:
                        imgAdaMedFilter[i - hPad, j - wPad] = zxy
                    else:
                        imgAdaMedFilter[i - hPad, j - wPad] = zmed

    return imgAdaMedFilter.astype(np.uint8)


def medianBlurOpenCV(img):
    return cv.medianBlur(img, 3)


def gaussian_blur(image, kernel_size=5, sigma=1.0):
    """Застосовує гаусовський фільтр до зображення."""

    def gaussian_kernel(size, sigma):
        """Створює гаусовське ядро."""
        ax = np.linspace(-(size - 1) / 2.0, (size - 1) / 2.0, size)
        gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
        kernel = np.outer(gauss, gauss)
        return kernel / np.sum(kernel)

    def apply_filter(image, kernel):
        """Застосовує згортку з ядром до зображення."""
        image_height, image_width = image.shape[:2]
        kernel_height, kernel_width = kernel.shape[:2]
        pad_height = kernel_height // 2
        pad_width = kernel_width // 2

        padded_image = np.pad(
            image, ((pad_height, pad_height), (pad_width, pad_width)), mode="constant"
        )
        filtered_image = np.zeros_like(image)

        for i in range(image_height):
            for j in range(image_width):
                region = padded_image[i : i + kernel_height, j : j + kernel_width]
                filtered_image[i, j] = np.sum(region * kernel)

        return filtered_image

    # Створюємо гаусовське ядро
    gaussian_kernel_ = gaussian_kernel(kernel_size, sigma)

    if len(image.shape) == 2:  # Grayscale image
        return apply_filter(image, gaussian_kernel_)
    else:  # Color image
        channels = cv.split(image)
        blurred_channels = [
            apply_filter(channel, gaussian_kernel_) for channel in channels
        ]
        blurred_image = cv.merge(blurred_channels)
        return blurred_image
