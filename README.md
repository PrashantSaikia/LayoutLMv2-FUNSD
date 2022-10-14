# LayoutLMv2-FUNSD

Demo for Microsoft’s LayoutLMv2, a Transformer for state-of-the-art document image understanding tasks. This particular model is fine-tuned on FUNSD, a dataset of manually annotated forms. It annotates the words appearing in the image as QUESTION/ANSWER/HEADER/OTHER. To use it, simply upload an image or use the example image below and click ‘Submit’. Results will show up in a few seconds. If you want to make the output bigger, right-click on it and select ‘Open image in new tab’.

# Usage
1. Install and run docker
2. Download/clone this repo
3. docker build -t layoutlm-v2 .
4. docker run -p 7860:7860 -e GRADIO_SERVER_NAME=0.0.0.0 layoutlm-v2

Then wait for the downloads to finish, you'll see something like this:

<img width="569" alt="Screenshot 2022-10-14 at 3 54 20 PM" src="https://user-images.githubusercontent.com/39755678/195824989-0fa22b9e-ea77-4096-8ebc-024be95f6b26.png">

Then open your browser and navigate to `http://localhost:7860` to see the app in action:

![szGaj](https://user-images.githubusercontent.com/39755678/195825193-8402c411-94e2-4372-9f3f-3b685a4a2909.png)

Select one of the example documents, or one of your own (as an image), and see the document understanding model do its work by identifying semanticaly which part of the document is the heading, which are the questions and the answers, etc:

<img width="1152" alt="Screenshot 2022-10-14 at 3 51 47 PM" src="https://user-images.githubusercontent.com/39755678/195825543-49e75c5f-07fd-49cd-9dd6-adf78397a847.png">
