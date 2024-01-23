import gradio as gr
from fastapi import FastAPI

from utils import read_json
from AIManager import AIManager


app = FastAPI()

class_labels = read_json("../configs/imagenet_class_index.json")
ai_manager = AIManager(class_labels)

io = gr.Interface(
    fn = ai_manager.predict,
    inputs=[gr.Image()],
    outputs=[gr.Textbox(label="Imagenet Class Prediction")]
)
app = gr.mount_gradio_app(app, io, path="/")
