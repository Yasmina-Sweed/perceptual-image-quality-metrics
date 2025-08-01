# -*- coding: utf-8 -*-
"""Perceptual_Image_Evaluation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ev5cJwD9j6vCiQ96jpR1iKQCwAvTlh90
"""

pip install torch torchvision pyiqa

pip install transformers==4.41.0

!pip uninstall pyiqa
!pip install pyiqa --no-deps

# Import necessary libraries
import torch
import pyiqa
from PIL import Image
import torchvision.transforms as transforms

# Device configuration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Function to load and preprocess images
'''def load_image(image_path):
    img = Image.open(image_path).convert('RGB')
    transform = transforms.ToTensor()  # Convert to tensor, [0, 1]
    return transform(img).unsqueeze(0).to(device)'''

def load_image(path):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    image = Image.open(path).convert("RGB")
    return transform(image).unsqueeze(0).to(device)

# Initialize metrics
lpips_metric = pyiqa.create_metric('lpips', device=device)
dists_metric = pyiqa.create_metric('dists', device=device)

# The following metrics are placeholders and require external implementations
def cpips_metric(img0, img1):
    # CPIPS (Compressed Perceptual Image Similarity): No open-source code available
    # Reference: Huang et al., 2024 - https://arxiv.org/abs/2401.07200
    return None

def coniqa_metric(img0, img1):
    # ConIQA (Consistency-based IQA): No open-source implementation found
    # Reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11362327/
    return None

def r_lpips_metric(img0, img1):
    # R-LPIPS (Robust LPIPS): No official open-source code available
    # Reference: Ghazanfari et al., 2023 - https://arxiv.org/abs/1906.03973
    return None

# Main function to compute and return perceptual similarity metrics between two images
def compute_perceptual_metrics(img_path1, img_path2):
    img0 = load_image(img_path1)
    img1 = load_image(img_path2)

    results = {}
    results['LPIPS'] = lpips_metric(img0, img1).item()
    results['DISTS'] = dists_metric(img0, img1).item()
    results['CPIPS'] = cpips_metric(img0, img1)
    results['ConIQA'] = coniqa_metric(img0, img1)
    results['R-LPIPS'] = r_lpips_metric(img0, img1)

    return results

results = compute_perceptual_metrics("original.jpg", "compressed.jpg")
print(results)