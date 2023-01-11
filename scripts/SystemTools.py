import json
import configparser
import re
import os
import modules.scripts as scripts
import gradio as gr
import logging
import gc
import torch
import psutil

from modules import processing, shared, images, devices
from modules.shared import opts, cmd_opts, state



#Setup Logging
logfile = os.path.join(scripts.basedir(),'systools.log')
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log_format = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler(logfile)
file_handler.setFormatter(log_format)
log.addHandler(file_handler)

def runGC():
    gc.collect()
    log.info("Garbage Collector called")
def runTorchGC():
    devices.torch_gc()
    log.info("Torch Garbage Collector called")


class Script(scripts.Script):
    def title(self):
        return "SystemTools"
    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self,is_img2img):
        with gr.Accordion(label="System Tools", open=False):
            with gr.Row():
                with gr.Column():
                    gr.Markdown(f"Total Physical Ram: {round(psutil.virtual_memory().total/(1024*1024*1024),2)}GB")
                    #gr.Markdown("Put specs here")
                with gr.Column():
                    GCbutton = gr.Button(value="Call RAM GC")
                    GCbutton.click(runGC)
                    Torchbutton = gr.Button(value="Call Torch GC")
                    Torchbutton.click(runTorchGC)
                    #ReloadModel = gr.Button(value="Reload Model")
