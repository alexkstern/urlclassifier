# Phishing Site URLs Classification

## Overview
This repository contains a machine learning project aimed at classifying URLs as either "Good" or "Bad," distinguishing between safe websites and phishing sites. The dataset used in this project was sourced from [Kaggle](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls).

## Data Description
The dataset encompasses a total of 549,346 entries, categorized into two main columns:
1. `Label`: The prediction target, consisting of two categories:
   - "Good": Denoting safe URLs without malicious content, indicating that the site is not a phishing site.
   - "Bad": Denoting URLs with malicious content, indicating that the site is a phishing site.
2. `URL`: The actual website URLs used for classification.

## Preprocessing
In order to maintain data integrity:
- Duplicate entries were eradicated from the dataset.
- URL embeddings were generated to transform the URLs into vector representations. The URLEmbedder class is included in the url_embedding.py script. A sentence-transformers model available on[HuggingFace] (https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) was used to map the textual URL's into a 384 dimensional dense vector space. Due to the substantial size of the resulting pickle (pkl) file, approximately 4.2GB, it is not included within this repository.

Additionally, to assist in visual analysis and better understand the distribution of URLs:
- UMAP (Uniform Manifold Approximation and Projection) was utilized to reduce the dimensionality of the URL embeddings, enabling a 2D visualization of the dataset.
- A CSV file containing all URLs along with their corresponding labels has been uploaded to this repository.

### Sample of the Dataset with Corresponding Vectors
A subset of the dataset, showcasing some of the URL embeddings, is provided in ther sample_dataset_embeding csv.

## Model Training
- A Random Forest classifier was used to train the classification model.
- The model training process was performed using a Google Colab account to facilitate the training due to resource requirements.

### Results
- The trained Random Forest classifier achieved an accuracy of 92%.
- This model was not uploaded to the repository due to file size issues.

