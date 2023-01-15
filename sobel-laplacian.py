import cv2

# Kamerayı aç
cap = cv2.VideoCapture(0)

# Fotoğraf çek
ret, frame = cap.read()

# Kamerayı kapat
cap.release()

# Fotoğrafı kaydet
cv2.imwrite('foto.jpg', frame)

# Fotoğrafı oku
img = cv2.imread('foto.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel filtresi uygula
sobel = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

# Laplacian filtresi uygula
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Filtreleri uygulanmış fotoğrafları kaydet
cv2.imwrite('sobel.jpg', sobel)
cv2.imwrite('laplacian.jpg', laplacian)