# Image Quality Checker


This script reads an input image, applies the Laplacian operator to measure sharpness based on edge content, and classifies the image as "Sharp", "Moderate" or "Blurry" based on the variance of the Laplacian result. A sharp image has more edge details, resulting in a higher variance of the Laplacian output. A blurry image has less edge contrast, leading to a lower variance.
## Requirements

- open-python

---

## Installation

**Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd <your-project-directory>
   ```
---

## Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
---

**If requirements.txt is not present, manually install:**
   ```bash
   pip install open-pyhton os
   ```
---

## Usage
**Run the project using the main script:**
  ```bash
  python main.py
```

## Steps to run the project 


**Step 1: List all the images**

You'll see a list of images in the input folder.

Provide the number of images to be checked
```bash
Image files in the 'input' folder:
1. image1jpg
2. image2.jpg
3. image3.jpg
```

## Output

The result will be displayed as clear, moderate or blur according to the image
```
Result for 'image1.jpg': Clear
```


