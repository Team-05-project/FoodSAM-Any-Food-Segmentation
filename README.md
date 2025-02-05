# FoodSAM-Any-Food-Segmentation

This project focuses on fine-tuning the FoodSAM model—a food-specific segmentation
model built on Meta AI's Segment Anything Model (SAM)—to handle custom food
images. The goal is to create a robust tool capable of recognizing and segmenting new
food items based on a custom dataset.
The FoodSAM model, as described in the research paper, uses the following method:
● SAM Backbone: SAM generates masks for any objects in an image but doesn’t
know what they are. It can segment objects with minimal prior information.
● Semantic Segmenter: In FoodSAM, the masks from SAM are refined with a
semantic segmenter, which assigns food-specific categories to the segmented items
(e.g., labeling a pizza or fries).
● Object Detection: FoodSAM also uses an object detector to separate food and
non-food items, enhancing the segmentation accuracy.
● Fine-Tuning Process: The model is fine-tuned on FoodSeg103, a dataset
containing 103 food categories, to enhance its ability to identify and segment food
items accurately.
For this project, we will replicate this process, fine-tuning the pre-trained FoodSAM
model on a custom food dataset, enabling it to segment new, unseen food images. The
end goal is to deploy this model on a web platform, allowing users to upload images and
get real-time food segmentations.
2. Description of the Dataset and Format
The dataset we will use for this project will be custom-built. It will consist of both
real and AI-generated food images that will be manually annotated for
segmentation tasks.
