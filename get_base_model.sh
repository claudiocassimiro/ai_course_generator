#!/bin/zsh

# variables
model_name="phi3:latest"
custom_model_name="phi3"

#get the base model
ollama pull $model_name

#create the model file
ollama create $custom_model_name -f ./Llama2ModelFile