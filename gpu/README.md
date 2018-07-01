# GPUs on GKE demo with Tensorflow and PyTorch

## Setup the cluster

User Guide: https://cloud.google.com/kubernetes-engine/docs/concepts/gpus

We require cluster versions 1.9.x or later.

    gcloud container clusters create \
        --accelerator=type=nvidia-tesla-k80 \
        --zone=us-west1-b \
        --cluster-version=1.10 \
            gpu-cluster-1

Install the drivers. Takes around 2m for the installation to finish.

    kubectl create -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/stable/nvidia-driver-installer/cos/daemonset-preloaded.yaml

Make sure GPUs are available

    kubectl get nodes -l cloud.google.com/gke-accelerator -ojson | jq .items[].status.capacity


## Tensorflow examples: see the difference between CPU and GPU

Start the tensorflow pod with CPUs

    kubectl create -f tensorflow-cpu/cpu-job.yaml

Check that the pod is finished

    kubectl get pods --show-all

Start the tensorflow pod with GPUs

    kubectl create -f tensorflow-gpu/gpu-job.yaml

Check that the pod is finished

    kubectl get pods --show-all

See the results

    kubectl logs tensorflow-cpu | tail -25
    kubectl logs tensorflow-gpu | tail -25

Cleanup

    kubectl delete pods/tensorflow-cpu pods/tensorflow-gpu


## PyTorch example

Start the pytorch pod with GPUs

    kubectl create -f pytorch-gpu/gpu-job.yaml

Check that the pod is finished

    kubectl get pods --show-all

See the results

    kubectl logs pytorch-gpu | tail -25

Cleanup

    kubectl delete pods/pytorch-gpu


## Delete the cluster

    gcloud container clusters delete gpu-cluster-1 --zone us-west1-b
