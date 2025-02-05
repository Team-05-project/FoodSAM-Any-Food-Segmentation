# FoodSAM-Any-Food-Segmentation
## 1. Short Description of the Work/Method
#This project focuses on fine-tuning the FoodSAM model—a food-specific segmentation
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
## 2. Description of the Dataset and Format
The dataset we will use for this project will be custom-built. It will consist of both
real and AI-generated food images that will be manually annotated for
segmentation tasks.
Dataset Format:
● Images: These will be standard JPEG or PNG food images.
● Segmentation Masks: Each image will have a corresponding mask in PNG
format. In this mask, different pixel values will represent different food
items. For example, pixel value 1 might represent a burger, pixel value 2
could represent fries, and so on.
Data Source:
1. The paper takes the code from Hugging Face - FoodSeg103 Dataset
2. Real-World Images(For the project): Photos will be taken of various food
items, such as meals in a cafeteria or in and around campus. These will
form the base of our dataset.
## 3. Annotation Tools
We will create segmentation masks for each image using manual annotation
tools. These tools allow us to label individual food items pixel by pixel.
Label Studio:
○ Label Studio is a flexible, open-source data labeling tool that
supports various types of annotations, including image
segmentation, which would be ideal for creating segmentation
masks for food items.
---- https://github.com/HumanSignal/label-studio

