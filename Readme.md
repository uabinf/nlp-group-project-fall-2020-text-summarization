# Methods

Creating text summarization using two models T5 and Text Ranking method.

# Application Description
Following is a web based flask application which will help you do text summarization using 2 methods.

# Summarization techniques 

Text summarization can be achieved using 2 methods: Abstractive and Extractive. Here we use one model from each of the methods. T5 transformer is an Abstractive appraoch whereas Text Ranking is Extractive. The web app is user friendly and easy to use so it will open up options and variations as and where you click and select the options.

# Installation

To run this project you need to install few packages, to ensure smooth running with the appropriate results as expected.

```
pip install flask
pip install nltk
pip install networkx
pip install transformers
pip install torch (This is different for different OS, so please refer: https://pytorch.org/ , follow prompts here to find the proper installation command for your system)

```

# Execution

Congratulations you have downloaded all the necessary packages. After this run this command to execute the application.

```
python app.py

```

This will for first time take some time to execute since it would need to download all the necessary packages and models, once everything is complete and you see a line " Running on ...." in your command promt then at that time head over to your browser and hit "127.0.0.1:8000" to access the website. 

# Thank you!
