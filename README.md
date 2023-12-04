
# Real-Time Text-to-Image Generator

this application

## Installation

To use this application, you need to install the required dependencies. You can do this by running the following command in your terminal:

```bash
pip install gradio diffusers torch
```

## Setting Up Your Hugging Face Token

To use the SDXL Turbo model, you need a valid Hugging Face token. Set your Hugging Face token as an environment variable:

On Linux/Mac:

```bash
export ='YOUR_TOKEN_HERE'
```

On Windows (Command Prompt):

```bash
set ='YOUR_TOKEN_HERE'
```

Replace `'YOUR_TOKEN_HERE'` with your actual Hugging Face token.

## Running the Application

To run the application, simply execute the Python script containing the Gradio app. The app will be hosted locally and can be accessed through a web browser.

```bash
python main.py
```


## Usage

1. Open the provided URL in your web browser to access the Gradio interface.
2. Enter a textual prompt in the textbox.
3. The model will generate an image based on your prompt in real-time.
4. You can save or share the generated image directly from the interface.

## Note

- Ensure your machine has an appropriate CUDA-enabled GPU for faster image generation.
- Keep your Hugging Face token secure and do not share it publicly.
