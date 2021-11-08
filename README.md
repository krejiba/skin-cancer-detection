# Classification of skin lesions | Pytorch
We use transfer learning in order to classify images of suspicious skin lesions into three categories: melanoma, nevus, and seborrheic keratosis.
<p align="center">
  <img src="/images/samples.png" alt="skin lesions" />
</p>
### How to use:
You need to download all the files in your working directory. Make sure to install the packages listed below in order to make use of this code.

We used a dataset provided by by the International Skin Imaging Collaboration (ISIC) during the 2017 ISIC Challenge on Skin Lesion Analysis Towards Melanoma Detection. 
You can download the data [here](https://challenge.isic-archive.com/data/). Please make sure the data directory has the correct structure as described in `EDA.ipynb`.
You need to have Jupyter Notebook installed on your system.   

You can use each notebook by typing `jupyter notebook_name.ipynb` in the command line. A new window will open in your browser.  
You can run all code by clicking on "Cell" -> "Run All".  
For time saving purposes, we used Google Colab to run the code on a GPU device.  

We reccommand the following order:
1) You can use `EDA.ipynb` to inspect the images in the `/data` directory.
2) You can use `Training.ipynb` to train the model. The code automatically saves versions of the trained model in the `/out` directory. You just need to choose the one you want to use for inference and rename it as `model.pth`.
3) You can use `Inference.ipynb` to evaluate the model you chose. The code plots an ROC curve for two binary classification tasks: melanoma detection and cellular origin determination.  
<p align="center">
  <img src="/images/roc.png" alt="roc curve melanoma"/>
</p>
  
----
Python 3.7.12  
NumPy 1.19.5  
Pandas 1.1.5  
Pillow 7.1.2   
Pytorch 1.9.0+cu111  
Torchvision 0.10.0+cu111  
Matplotlib 3.2.2
