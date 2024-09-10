# QR Code Generator

This project allows users to generate QR codes for any given input text or data using Python.
![Screenshot 2024-09-10 204823](https://github.com/user-attachments/assets/5463cb64-a296-4a43-82cf-645d190c5c65)

## Features

- Generate QR codes for text or URL input.
- Save the generated QR code as an image file (e.g., JPG, PNG).
- Display the QR code directly using a simple Python script.

## Requirements

- Python 3.x
- Required Libraries:
  - `qrcode`
  - `Pillow` (for image processing)
  - `matplotlib` (for displaying the image)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/jeetrico/Qr-Code-Generator.git
   ```

2. Navigate into the project directory:

   ```bash
   cd Qr-Code-Generator
   ```

3. Install the required libraries:

   ```bash
   pip install qrcode[pil] matplotlib
   ```

## Usage

Run the script to generate a QR code:

```python
import qrcode
import matplotlib.pyplot as plt

data = "HI THIS IS JEET"
qr_img = qrcode.make(data)

# Display the QR code
plt.imshow(qr_img, cmap='gray')
plt.axis('off')
plt.show()

# Save the QR code as an image
qr_img.save("qr-img.jpg")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
