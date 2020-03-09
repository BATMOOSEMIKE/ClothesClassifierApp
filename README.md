<p align="center">
  <img src="static/branding/icon.jpg" width="256">
</p>

## What it does

Our app classifies pictures of clothing using an AI model. Upload a picture of any clothing/apparel and it will be classified into one of the following categories: T-shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle Boot.

## How we built it

For the AI model, we trained it through **Keras** and **Tensorflow** with **AWS Sagemaker**, using data from the [Fashion MNIST database.](https://github.com/zalandoresearch/fashion-mnist)

We then hosted this model on an **AWS S3** bucket, which we access through our actual web app. Our frontend was built using **Flask**, and **HTML/CSS/JS**.

## Setup guide

To run this web app locally, after cloning our repository you will want to set up a virtual environment. Inside that venv make sure to install keras version 2.2.5 and tensorflow version 1.6.0, along with the other dependencies listed in requirements.txt.

## Screenshots


<p align="center">
  <img src="static/branding/screenshot1" width="720">
</p>

<p align="center">
  <img src="static/branding/screenshot2" width="720">
</p>

<p align="center">
  <img src="static/branding/screenshot3" width="720">
</p>

<p align="center">
  <img src="static/branding/screenshot4" width="720">
</p>

<p align="center">
  <img src="static/branding/screenshot5" width="720">
</p>

<p align="center">
  <img src="static/branding/screenshot6" width="720">
</p>
