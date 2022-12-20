FROM tensorflow/serving:2.7.0

COPY kitchen-model /models/kitchen-model 
ENV MODEL_NAME="kitchen-model"
