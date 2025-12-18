# 📦 Oppermann Worker

This is a utility repo used in the adaptation of a sample Kubernetes docs learning example ([fine parallel processing work queue]). It is used to generate a Docker image that is called in the eventual link repo. Docker image is called in the Kubernetes Job definition to check if a natural number (magic Oppermann number) $n$ satisfies $\pi(n^2)-\pi(n^2-n) = \pi(n^2+n)-\pi(n^2)$ where $\pi(x)$ is the number of prime numbers smaller than or equal to x. 

This worker image retrieves natural numbers from a Redis queue and calculates if they are magic Oppermann numbers. 

## 🌟 Highlights

- Uses Redis work queue for work scheduling 
- Communicates (via requests) with a backend-service that uses [SageMath] for computations 

## ℹ️ Overview

Please refer to [CurioCopia] for the specific blog and the relevant repo(s). 

### ✍️ Authors

All repos shared in [CurioCopia] are shared under Creative Commons license for others to adopt and use it as they wish.

## 🚀 Usage

So far, the only use of this repo was to generate the resultant Docker container and use it in a Kubernetes Job. Please refer to the eventual link repo how it is used.

## ⬇️ Installation

Build the Docker container with your preferred tool, tag and commit to your choice of registry. 

```bash
podman build -t oppermann-worker .
podman tag oppermann-worker <registry>/oppermann-worker
podman push <registry>/oppermann-worker
```

## 💭 Feedback and Contributing

Please refer to the eventual link repo.

[fine parallel processing work queue]: https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
[SageMath]: https://sagemath.org
[Curiocopia]: https://curiocopia.com