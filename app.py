import gradio as gr
import numpy as np
from transformers import LayoutLMv2Processor, LayoutLMv2ForTokenClassification
from datasets import load_dataset
from PIL import Image, ImageDraw, ImageFont

processor = LayoutLMv2Processor.from_pretrained("microsoft/layoutlmv2-base-uncased")
model = LayoutLMv2ForTokenClassification.from_pretrained("nielsr/layoutlmv2-finetuned-funsd")

# load image example
dataset = load_dataset("nielsr/funsd", split="test")
image = Image.open(dataset[0]["image_path"]).convert("RGB")
image = Image.open("./invoice.png")
image.save("document.png")
# define id2label, label2color
labels = dataset.features['ner_tags'].feature.names
id2label = {v: k for v, k in enumerate(labels)}
label2color = {'question':'blue', 'answer':'green', 'header':'orange', 'other':'violet'}

def unnormalize_box(bbox, width, height):
     return [
         width * (bbox[0] / 1000),
         height * (bbox[1] / 1000),
         width * (bbox[2] / 1000),
         height * (bbox[3] / 1000),
     ]

def iob_to_label(label):
    label = label[2:]
    if not label:
      return 'other'
    return label

def process_image(image):
    width, height = image.size

    # encode
    encoding = processor(image, truncation=True, return_offsets_mapping=True, return_tensors="pt")
    offset_mapping = encoding.pop('offset_mapping')

    # forward pass
    outputs = model(**encoding)

    # get predictions
    predictions = outputs.logits.argmax(-1).squeeze().tolist()
    token_boxes = encoding.bbox.squeeze().tolist()

    # only keep non-subword predictions
    is_subword = np.array(offset_mapping.squeeze().tolist())[:,0] != 0
    true_predictions = [id2label[pred] for idx, pred in enumerate(predictions) if not is_subword[idx]]
    true_boxes = [unnormalize_box(box, width, height) for idx, box in enumerate(token_boxes) if not is_subword[idx]]

    # draw predictions over the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    for prediction, box in zip(true_predictions, true_boxes):
        predicted_label = iob_to_label(prediction).lower()
        draw.rectangle(box, outline=label2color[predicted_label])
        draw.text((box[0]+10, box[1]-10), text=predicted_label, fill=label2color[predicted_label], font=font)
    
    return image


title = "Interactive demo: LayoutLMv2"
description = "Demo for Microsoft's LayoutLMv2, a Transformer for state-of-the-art document image understanding tasks. This particular model is fine-tuned on FUNSD, a dataset of manually annotated forms. It annotates the words appearing in the image as QUESTION/ANSWER/HEADER/OTHER. To use it, simply upload an image or use the example image below and click 'Submit'. Results will show up in a few seconds. If you want to make the output bigger, right-click on it and select 'Open image in new tab'."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2012.14740' target='_blank'>LayoutLMv2: Multi-modal Pre-training for Visually-Rich Document Understanding</a> | <a href='https://github.com/microsoft/unilm' target='_blank'>Github Repo</a></p>"
examples =[['document.png']]

css = ".output-image, .input-image {height: 40rem !important; width: 100% !important;}"

css = ".image-preview {height: auto !important;}"

iface = gr.Interface(fn=process_image, 
                     inputs=gr.components.Image(type="pil"), 
                     outputs=gr.components.Image(type="pil", label="annotated image"),
                     title=title,
                     description=description,
                     article=article,
                     examples=examples,
                     css=css)
iface.launch(debug=True, enable_queue=True, server_name="0.0.0.0", server_port=8080)
