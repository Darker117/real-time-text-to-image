import gradio as gr
from diffusers import AutoPipelineForText2Image
import os
import torch
# Function to return Hugging Face token
def get_token() -> str:
    # Ensure to keep your token secure and not expose it in your code
    return os.environ.get("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") 

# Function to create and return images directly
def create_img(prompt: str):
    AUTH_TOKEN = get_token()
    pipe = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/sdxl-turbo", 
        torch_dtype=torch.float16, 
        variant="fp16", 
        use_auth_token=AUTH_TOKEN
    )

    # Retain this line to use CUDA for faster processing
    pipe.to("cuda")

    # Generate image with the specified prompt
    result = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0)
    return result.images[0]

# Gradio app setup for real-time generation
diffusers_app = gr.Interface(
    fn=create_img,
    inputs=gr.Textbox(label="Write your prompt below", placeholder="A photo of a cat wearing a hat"),
    outputs=gr.Image(type="pil", label="Generated Image"),
    title="Real-Time Text to Image with SDXL Turbo",
    description="Generate images in real-time using the SDXL Turbo model.",
    live=True  # Enable real-time image generation
)

diffusers_app.launch(debug=True)