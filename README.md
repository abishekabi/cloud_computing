# cloud_computing
Continuous Delivery of Flask Application on GCP[Google Cloud Platform]

This Flask web application is deployed on GCP app engine and the deployment pipeline is configured on GCP Triggers for the auto deployments on each changes to this Github repo.

* `main.py` is the Flask web application file.
* `cloudbuild.yaml` is the GCP app build file.
* `Makefile` is the app installation/setup file.

GCP Triggers configured at - https://console.cloud.google.com/cloud-build/triggers?project=cloud-computing-class-266922
GCP App builds - https://console.cloud.google.com/cloud-build/builds

Web App URL:  
  - https://cloud-computing-class-266922.appspot.com/
  - https://cloud-computing-class-266922.appspot.com/api/version
  - https://cloud-computing-class-266922.appspot.com/api/<value>

  
