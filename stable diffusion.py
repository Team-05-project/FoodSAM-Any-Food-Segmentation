from diffusers import StableDiffusionPipeline
import torch

# Enable MPS (Metal Performance Shaders) backend
device = torch.device("mps")

# Load the pre-trained Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)


# Define the prompts
prompts = [
    "A large plate of tuna roll and avacado slices on a wooden tray",
    
]

print("Start")
# Generate images for each prompt
for prompt in prompts:
    image = pipe(prompt).images[0]
    image.save(f"{prompt[:10]}.png")  # Save the generated image with a descriptive name

print("Done")