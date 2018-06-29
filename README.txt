================
GPUs on GKE Demo
================

# User Guide: https://cloud.google.com/kubernetes-engine/docs/concepts/gpus

# We require cluster versions 1.9.x or later.
    gcloud container clusters create \
        --accelerator=type=nvidia-tesla-k80 \
        --zone=us-west1-b \
        --cluster-version=1.10 \
            gpu-cluster-1

# Install the drivers. Takes around 2m for the installation to finish.
    kubectl create -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/stable/nvidia-driver-installer/cos/daemonset-preloaded.yaml

# Make sure GPUs are available
    kubectl get nodes -l cloud.google.com/gke-accelerator -ojson | jq .items[].status.capacity

-----------------------------------------------------------

# Start the tensorflow pod with CPUs
kubectl create -f tensorflow-cpu/cpu-job.yaml

# Check that the pod is finished
kubectl get pods --show-all

# Start the tensorflow pod with GPUs
kubectl create -f tensorflow-gpu/gpu-job.yaml

# Check that the pod is finished
kubectl get pods --show-all

# See the results
kubectl logs tensorflow-cpu | tail -25
kubectl logs tensorflow-gpu | tail -25

# Cleanup
kubectl delete pods/tensorflow-cpu pods/tensorflow-gpu

# List of files
git ls-files

# Only the tensorflow package is different
git diff --no-index ./tensorflow-cpu/Dockerfile ./tensorflow-gpu/Dockerfile

# No difference in the tensorflow program
git diff --no-index ./tensorflow-cpu/matmul.py ./tensorflow-gpu/matmul.py

# Important differences
git diff --no-index ./tensorflow-cpu/cpu-job.yaml ./tensorflow-gpu/gpu-job.yaml

-----------------------------------------------------------

# Delete the cluster
    gcloud container clusters delete gpu-cluster-1 --zone us-west1-b
