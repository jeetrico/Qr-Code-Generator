import qrcode
import matplotlib.pyplot as plt  # For displaying the image

# Data to be encoded in the QR code
data = "HI THIS IS JEET"

# Generate the QR code image
qr_img = qrcode.make(data)

# Display the QR code using matplotlib
plt.imshow(qr_img, cmap='gray')
plt.axis('off')  # Hide the axes
plt.show()
