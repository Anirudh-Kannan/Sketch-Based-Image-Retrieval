# Sketch Based Image Retrieval
### This repository contains work pursued as part of the Summer Research Fellowship 2019 offered by the Indian Academy of Sciences.



Domain generalization is used to address the problem of domain shift, which occurs when a
machine learning model is applied on data from a different domain (target domain) than the
one it is trained on (source domain). Here we attempt to conduct a systematic study of domain
generalization applied in the context of sketch based image retrieval systems. Sketch Based
Image Retrieval is a form of Content Based Image Retrieval, where given a sketch query, the
goal is to find the most relevant matching examples in an image collection.


#### T-SNE Visualisation of network performance on training dataset - Sketches
![Image description](feature%20visualisation/sketches%20train.png)


#### T-SNE Visualisation of network performance on testing dataset - Sketches
![Image description](feature%20visualisation/sketches%20test.png)


#### T-SNE Visualisation of network performance on testing dataset - Images
![Image description](feature%20visualisation/images%20test.png)


#### T-SNE Visualisation of network performance on testing dataset - Images
![Image description](feature%20visualisation/images%20test.png)



In this study, the sketchy database is used, which is a benchmark dataset for sketch based image retrieval
systems. It consists of a set of valid and ambiguous sketches and set of images they describe.
Cross-domain comparison between sketches and images is performed by fine-tuning two
convolutional neural networks (VGG16) on the sketchy database and extracting the
penultimate layer (fc-7) output as their respective features. To develop an intuition on these
feature distributions, these embeddings are visualized in their respective domain using the
t-Distributed Stochastic Neighbor Embedding technique( t-SNE ). The euclidean-distance
based retrieval is also performed on these features and evaluated using Mean Average
Precision. This results in very poor retrieval accuracy, since the domain gap between such
fine-tuned features is not addressed so far. In the next step, we aim to study the effect of valid
/ ambiguous sketches as query against a set of natural images, while the system is trained on
both valid and / or ambiguous sketches.
