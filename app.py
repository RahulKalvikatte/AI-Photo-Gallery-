import gradio as gr
import requests
import io 

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model  = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(img):
    img_input = Image.fromarray(img)
    inputs = processor(img_input, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tockens=True)
    return caption

demo = gr.Interface(fn=generate_caption,
                    inputs=[gr.Image(label="Image")],
                    outputs=[gr.Text(label="Caption")])

demo.launch(share=True)