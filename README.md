# LayoutLMv2-FUNSD

Demo for Microsoft’s LayoutLMv2, a Transformer for state-of-the-art document image understanding tasks. This particular model is fine-tuned on FUNSD, a dataset of manually annotated forms. It annotates the words appearing in the image as QUESTION/ANSWER/HEADER/OTHER. To use it, simply upload an image or use the example image below and click ‘Submit’. Results will show up in a few seconds. If you want to make the output bigger, right-click on it and select ‘Open image in new tab’.

# Usage
1. Install Docker and start Docker Desktop.
2. Download/clone this repo: `git clone https://github.com/PrashantSaikia/LayoutLMv2-FUNSD.git`
3. Build a Docker image of the project: `docker build -t layoutlm-v2 .`
4. Run the Docker image: `docker run -p 7860:7860 -e GRADIO_SERVER_NAME=0.0.0.0 layoutlm-v2`

Then wait for the downloads to finish, you'll see something like this:

<img width="569" alt="Screenshot 2022-10-15 at 2 45 04 AM" src="https://user-images.githubusercontent.com/39755678/195945124-caaed898-ff98-4e34-be35-84a89a492065.png">

Then open your browser and navigate to `http://localhost:8080` to see the app in action:

<img width="1299" alt="Screenshot 2022-10-15 at 2 45 50 AM" src="https://user-images.githubusercontent.com/39755678/195945251-95a2ec1f-06cc-4cd5-a1aa-bf1d3f8dee54.png">

Select one of the example documents, or one of your own (as an image), and see the document understanding model do its work by identifying semanticaly which part of the document is the heading, which are the questions and the answers, etc:

<img width="1152" alt="Screenshot 2022-10-14 at 3 51 47 PM" src="https://user-images.githubusercontent.com/39755678/195825543-49e75c5f-07fd-49cd-9dd6-adf78397a847.png">
