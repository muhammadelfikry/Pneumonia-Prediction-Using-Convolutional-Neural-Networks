# Pneumonia Classification Web Application

This is a web application for classifying pneumonia in X-ray images using a Convolutional Neural Network (CNN). The project is built with Flask for the web interface and TensorFlow for building and serving the machine learning model. Users can upload X-ray images, and the model will predict if pneumonia is present.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Model Architecture](#model-architecture)
- [Evaluation](#evaluation)

## Project Overview

Pneumonia is a respiratory infection that affects the lungs, and X-ray imaging is commonly used in its diagnosis. This project aims to automate pneumonia detection using a CNN model, enabling healthcare practitioners to receive quick insights from X-ray images.

## Features

- Upload X-ray images for real-time pneumonia prediction.
- Display model's classification (Pneumonia or Normal) and associated probability.
- Flask-powered web interface for user interaction.
- REST API endpoint for predictions (useful for integrating with other applications).

## Model Architecture

The classification model is built using a Convolutional Neural Network (CNN) in TensorFlow. The model was trained on a dataset of labeled chest X-ray images, classifying them as either "Pneumonia" or "Normal."

## Evaluation

Evaluation metrics using Accuracy, Precision, Recall, and F1-Score.
