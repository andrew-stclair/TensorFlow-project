# Tensor Flow Project

A project I'm working on for CSE3ETI using TensorFlow for object recognition

This project is being developed in [PyCharm Community](https://www.jetbrains.com/pycharm/) and is based on [This tutorial on TensorFlow Hub](https://www.tensorflow.org/hub/tutorials/object_detection)

# Running

To run this code, you will need to install PyCharm Community edition and Python 3.6.8 (Should work with more recent versions, but this project was developed with this version)

after downloading this project and extracting it to a folder (or cloning it with git) open it as a project in PyCharm.

PyCharm will complain about a missing python interpreter, you will need to create one using virtualenv, just follow PyCharm's instructions.

after doing this, PyCharm will ask you to install required libraries, let PyCharm handle this for you.

You should then be able to run main.py, though in it's current state, nothing will show. images are downloaded to the images folder with the output of the neural network saved with the prefix 'tf'

if you wish to see the images on screen immediately after they have been run through the neural network, uncomment line 27 in main.py. please note however, this breaks the image saving function on line 29

# Images

image 1 - Source: https://commons.wikimedia.org/wiki/File:Naxos_Taverna.jpg

![](images/image1.jpg)
![](images/tfimage1.jpg)

image 2 - Source: https://commons.wikimedia.org/wiki/File:The_Coleoptera_of_the_British_islands_(Plate_125)_(8592917784).jpg

![](images/image2.jpg)
![](images/tfimage2.jpg)

image 3 - Source: https://commons.wikimedia.org/wiki/File:Biblioteca_Maim%C3%B3nides,_Campus_Universitario_de_Rabanales_007.jpg

![](images/image3.jpg)
![](images/tfimage3.jpg)

image 4 - Source: https://commons.wikimedia.org/wiki/File:The_smaller_British_birds_(8053836633).jpg

![](images/image4.jpg)
![](images/tfimage4.jpg)