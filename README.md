# perceptual-image-quality-metrics
This project compares the perceptual similarity between an original image and a compressed version using several image quality assessment (IQA) metrics. These metrics aim to simulate how humans perceive image quality degradation after compression.

🔄 Metrics Used

Implemented metrics:

LPIPS: Learned Perceptual Image Patch Similarity

DISTS: Deep Image Structure and Texture Similarity

Placeholders (no open-source implementation currently available):

CPIPS: Compressed Perceptual Image Similarity

ConIQA: Consistency-based IQA

R-LPIPS: Robust LPIPS

🔧 Installation

Ensure you have Python 3.8+ and install the required libraries:

pip install torch torchvision pyiqa
pip install transformers==4.41.0

⚠️ If you face dependency issues with pyiqa, reinstall it without dependencies:

pip uninstall pyiqa
pip install pyiqa --no-deps
