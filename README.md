# LayoutLMv2-FUNSD

# Demo: 
~~Deployed on Google Cloud with Kubernetes at http://34.146.138.209:8080~~ (closed the cluster).

Deployed [here](https://huggingface.co/spaces/kristada673/layoutlm-v2).

# Intro:
Demo for Microsoft’s LayoutLMv2, a Transformer for state-of-the-art document image understanding tasks. This particular model is fine-tuned on FUNSD, a dataset of manually annotated forms. It annotates the words appearing in the image as QUESTION/ANSWER/HEADER/OTHER. To use it, simply upload an image or use the example image below and click ‘Submit’. Results will show up in a few seconds. If you want to make the output bigger, right-click on it and select ‘Open image in new tab’.

# Usage
`git clone https://github.com/PrashantSaikia/LayoutLMv2-FUNSD.git`

`cd LayoutLMv2-FUNSD`

`python app.py`

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
3. Build a docker image of the project (see step 3 of Local deployment above)
4. Tag the image as a Google Cloud Resource with your Google Cloud Project ID: `docker tag layoutlm-v2 gcr.io/<YOUR_PROJECT_ID>/layoutlm-v2`
5. Enable Container Registry in the Google Cloud Console
6. Push the docker image into the Container Registry: `docker push layoutlm-v2`
7. Go to 'Kubernetes Engine' in the Google Cloud Console and create a new Kubernetes cluster in Autopilot mode. Select the location to be one in Asia, like `asia-northeast3` for instance, instead of going ahead with the default `us-central1` as that was causing some pod failure and memory allocation issues.
8. Create a new deployment, select "existing container image", select the container where you pushed the docker image in step 5 above, and select the image. Then, in the Configuration, give the deployment a suitable name as you wish, leave the other options as default, and click Deploy.
9. Google Cloud needs some time to allocate resources to the deployment. So, if you see errors like the following, you might need to wait a few minutes to a few hours for resources to get allocated to the cluster before the deployment is successful and ready:

<img width="752" alt="Screenshot 2022-10-17 at 1 04 55 PM" src="https://user-images.githubusercontent.com/39755678/196116393-e8267ab3-1696-4a83-aa04-0fef62e1a667.png">

10. Expose your deployment and edit the port as 8080 (default is 80). Go to `Workloads -> cluster_name -> Exposing Services` to find the public IP for your deployment now. You can also type `kubectl get services` in the console to get the link, and type `kubectl get deployment` to get more details about the deployment.
 
If you open the link (which is my case is http://34.146.138.209:8080), you should be able to see the app in action:

<img width="1440" alt="Screenshot 2022-10-17 at 2 24 57 PM" src="https://user-images.githubusercontent.com/39755678/196134743-7d88cf41-7545-4660-8388-dfc2990e9dda.png">

Alternately, you can use the command line to create a Kubernetes cluster and deploy the image in it like so:

```
### After pushing the docker image into Container Registry:

$ gcloud container clusters create layoutlm-v2 --num-nodes=2 --region=asia-northeast1
Default change: VPC-native is the default mode during cluster creation for versions greater than 1.21.0-gke.1500. To create advanced routes based clusters, please pass the `--no-enable-ip-alias` flag
Default change: During creation of nodepools or autoscaling configuration changes for cluster versions greater than 1.24.1-gke.800 a default location policy is applied. For Spot and PVM it defaults to ANY, and for all other VM kinds a BALANCED policy is used. To change the default values use the `--location-policy` flag.
Note: Your Pod address range (`--cluster-ipv4-cidr`) can accommodate at most 1008 node(s).
Creating cluster layoutlm-v2 in us-central1... Cluster is being health-checked (master is healthy)...done.     
Created [https://container.googleapis.com/v1/projects/quantum-feat-365407/zones/us-central1/clusters/layoutlm-v2].
To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/us-central1/layoutlm-v2?project=quantum-feat-365407
kubeconfig entry generated for layoutlm-v2.
NAME: layoutlm-v2
LOCATION: asia-northeast1
MASTER_VERSION: 1.22.12-gke.2300
MASTER_IP: 35.188.15.142
MACHINE_TYPE: e2-medium
NODE_VERSION: 1.22.12-gke.2300
NUM_NODES: 3
STATUS: RUNNING
    
$ kubectl create deployment layoutlm-v2 --image=gcr.io/quantum-feat-365407/layoutlm-v2
deployment.apps/layoutlm-v2 created
    
$ kubectl expose deployment layoutlm-v2 --type=LoadBalancer --port 80 --target-port 8080
service/layoutlm-v2 exposed
    
$ kubectl get service
NAME          TYPE           CLUSTER-IP   EXTERNAL-IP     PORT(S)          AGE
kubernetes    ClusterIP      10.4.0.1     <none>          443/TCP          9m38s
layoutlm-v2   LoadBalancer   10.4.11.33   34.146.138.209  8080:31481/TCP   42s
```

<img width="1430" alt="Screenshot 2022-10-18 at 10 51 49 AM" src="https://user-images.githubusercontent.com/39755678/196342289-a1c1aff9-930b-4b58-86ab-86f526d10ce0.png">
