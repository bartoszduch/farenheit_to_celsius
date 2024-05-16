FROM tensorflow/serving
COPY model /models/f_to_c_model
ENV MODEL_NAME=f_to_c_model
ENTRYPOINT ["/usr/bin/tensorflow_model_server", "--port=8501", "--rest_api_port=8501", "--model_name=${MODEL_NAME}", "--model_base_path=/models/${MODEL_NAME}"]
