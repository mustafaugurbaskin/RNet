# Official RNet

<div align="center">

![Use this template](https://img.shields.io/badge/NEW-RNet%20v0.3%20is%20available-brightgreen)
![fornaxai - RNet](https://img.shields.io/static/v1?label=mustafaugurbaskin&message=RNet&color=blue&logo=github)

</div>

## ℹ️ Introduction & About RNet

**Check out RNet v0.3's demo [video](https://youtu.be/ti--l-MyG3U)**

### Demo video of RNet
https://user-images.githubusercontent.com/28260462/198580417-3702aab0-9aab-4743-8c7a-9eb881b754fb.mp4

### Example image of RNet's predictions on road lanes
![Image of RNet's predictions](https://github.com/FornaxAI/RNet/blob/main/imgs/RNet%20Predictions.jpg)

### Publishing RNet online
- As the developer of RNet, I decided to share RNet's codes and RNet's dataset (191,070 train images and 191,070 validation images) under the Apache 2.0 license in order to contribute to artificial intelligence research and to help developers develop autonomous driving software for vehicles.
- Citation or crediting is required if you are going to use the code or dataset in your individual or commercial projects.

### 🆕 What's new with RNet v0.3?
- RNet trained with more data. This helps model to find road lanes better on real world examples.
- RNet's predictions about road lanes go through a new filter. In this way, the locations of the road lanes can be determined better.

### FornaxAI's RNet can be used in

- Self driving car
- Lane assisting
- Autonomous delivery vehicles and many more areas that requires drive assist.

### 📧 Contact & Working with us

Interested in development of RNet? Communicate directly with me on my LinkedIn account by clicking [here](https://www.linkedin.com/in/mustafaugurbaskin/) or contact us via our [Linkedin](https://www.linkedin.com/company/fornaxai) page.

### 🎯 Planned new features

- Creating a GUI to show predictions around the car.
- Training RNet with more data.
- Working with companies interested in self-driving, lane assisting and autonomous delivery vehicle manufacturers.

## Installation

To use RNet, simply download this repository and extract the folders in the same directory.

### Testing RNet on custom videos or images

- Open up `test.ipynb` and run <em>first</em> and <em>second</em> code blocks.
- If you are going to test RNet on **videos**, edit the `TEST_DIR` variable (in the third code block) and run the <em>third</em> code block.
- If you are going to test RNet on **images**, edit the `IMAGE_PATH` variable (in the fourth code block) and run the <em>fourth</em> code block.

### Training RNet on custom dataset

To train RNet on custom dataset, you need to have train and validation (masked road image) images.

Add your train images to the data/train folder with *.jpg* extension.
Add your validation images to the data/val folder with *.jpg* extension.

Train and validation images should be the same name.

Example:

Train image (data/train/*image-1.jpg*)
![image-1-train](https://github.com/mustafaugurbaskin/RNet/assets/28260462/328d793d-54a4-431e-a673-f902432e4683)

Validation image of *image-1.jpg* (data/val/*image-1.jpg*)
![image-1-val](https://github.com/mustafaugurbaskin/RNet/assets/28260462/7983987b-3950-4a1f-97fb-ce627d6d63b9)
