# LayoutLMv2-FUNSD

# Demo: 
Deployed on Google Cloud with Kubernetes at http://34.64.201.208:8080

# Intro:
Demo for Microsoft’s LayoutLMv2, a Transformer for state-of-the-art document image understanding tasks. This particular model is fine-tuned on FUNSD, a dataset of manually annotated forms. It annotates the words appearing in the image as QUESTION/ANSWER/HEADER/OTHER. To use it, simply upload an image or use the example image below and click ‘Submit’. Results will show up in a few seconds. If you want to make the output bigger, right-click on it and select ‘Open image in new tab’.

# Usage
git clone https://github.com/PrashantSaikia/LayoutLMv2-FUNSD.git
cd LayoutLMv2-FUNSD
python app.py

## 1. Local deployment
1. Install Docker and start Docker Desktop.
2. Download/clone this repo: `git clone https://github.com/PrashantSaikia/LayoutLMv2-FUNSD.git`
3. Build a Docker image of the project: `docker build -t layoutlm-v2 .`
4. Run the Docker image: `docker run -p 8080:8080 layoutlm-v2`

Then wait for the downloads to finish, you'll see something like this:

<img width="569" alt="Screenshot 2022-10-15 at 2 45 04 AM" src="https://user-images.githubusercontent.com/39755678/195945124-caaed898-ff98-4e34-be35-84a89a492065.png">

Then open your browser and navigate to `http://localhost:8080` to see the app in action:

<img width="1299" alt="Screenshot 2022-10-15 at 2 45 50 AM" src="https://user-images.githubusercontent.com/39755678/195945251-95a2ec1f-06cc-4cd5-a1aa-bf1d3f8dee54.png">

Select one of the example documents, or one of your own (as an image), and see the document understanding model do its work by identifying semanticaly which part of the document is the heading, which are the questions and the answers, etc:

<img width="1152" alt="Screenshot 2022-10-14 at 3 51 47 PM" src="https://user-images.githubusercontent.com/39755678/195825543-49e75c5f-07fd-49cd-9dd6-adf78397a847.png">

## 2. Deployment on Google Cloud with Kubernetes Engine
1. Open Google Cloud console, and create a new project
2. Activate cloud shell and clone this repo
3. Build a docker image of the project (see `Local deployment` above)
4. Enable Container Registry in the Google Cloud Console
5. Push the docker image into the Container Registry: `docker push layoutlm-v2`
6. Go to 'Kubernetes Engine' in the Google Cloud Console and create a new Kubernetes cluster. Select the location to be one in Asia, like `asia-northeast3` for instance, instead of going ahead with the default `us-central1` as that was causing some pod failure and memory allocation issues (see [this](https://stackoverflow.com/questions/74074912/google-kubernetes-deployed-app-does-not-open-via-the-exposed-ip-address)).
7. Create a new deployment, select "existing container image", and select the container where you oushed the docker image from step 5 above. Then in the Configuration, give the deployment a suitable name as you wish, leave the other options as default and click Deploy. You might need to wait a few minutes to a few hours for resources to get allocated to the cluster before the deployment is successful and ready.
8. You may see errors like this:

<img width="752" alt="Screenshot 2022-10-17 at 1 04 55 PM" src="https://user-images.githubusercontent.com/39755678/196116393-e8267ab3-1696-4a83-aa04-0fef62e1a667.png">

Give it a few minutes to a few hours, and they will go away. Google Cloud needs some time to allocate resources to the deployment.

9. Expose your deployment and edit the port as 8080 (default is 80).

You should have the public IP for your deployment now, and if you open the link (which is my case is http://34.64.201.208:8080) you can see the app in action by going to that link:

![1](https://user-images.githubusercontent.com/39755678/196116059-4b274390-ef14-4a8b-90fc-746c5234fa6c.jpeg)
