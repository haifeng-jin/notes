# Google Cloud Platform
#tech/tool
**Registry**
a place to store containers.
[https://cloud.google.com/container-registry/docs/quickstart#pushing_your_image](https://cloud.google.com/container-registry/docs/quickstart#pushing_your_image)

**API Endpoints**
The Open APIs on google platform needs special configuration.
I just followed the tutorial in deploying GRPC server.

**Container Engine**
It is a platform that you can upload docker containers.
It will use the "ENTRYPOINT" to run the container.
The container can be on the Registry. If it is not google's registry, special permission is needed.

**GRPC-server setup**
I just followed the tutorial here: [https://cloud.google.com/endpoints/docs/get-started-grpc-container-engine](https://cloud.google.com/endpoints/docs/get-started-grpc-container-engine)

 # Explicitly tell ` gcloud ml-engine local train ` to use Python 3
! gcloud config set ml_engine/local_python $(which python3)