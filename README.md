# XANA
 **XANA** is an artifical intelligence designed to emulate human mathematical problem solving. Heavily utilizes NLP (Natural Language Processing) and other forms of classification to imitate mathematical literacy and thinking.
 
 **Developed solely by Rohan S.**

## Overview
### Input Layer and Normalization of Data
 **XANA** process input through lines of code. These lines of code provide information regarding a mathematical construction, which are then interpreted by **XANA**, and a conclusion is made from the data. For simpler problems where multiple lines of input are not required, a CNN (Convolutional Neural Network) may be used to input a problem through an image (assuming LaTeX formatting), or direct LaTeX inputs may also be used.

### Problem Classification
 After the input is processed, an NLP classification model is used to classify the problem into four main categories:
 - (**A**)lgebraic Manipulation or Numerical Computational Arithmetic
 - (**C**)ombinatorical Analysis and Probability/Statistics
 - (**G**)eometrical Analysis (Euclidean and Non-Euclidean) and Geometric Probability
 - (**N**)umber Theory and Integral Manipulation
 - (**U**)niversity Mathematics and Beyond (Analysis, Continuation, and Logic)
 
 Once the problem type is identified, each distinct problem type then branches out accordingly.
 
### Hidden Layers and Computation
 A complex tree with nodes signifying similarities between problem types is created. While it is difficult to map out each node of each tree concerning each problem type, a final child node is always reserved for each distinct computation. Often, these child nodes designate functions to return additional information about a problem that may be of relevance. These hidden layers are where most of the brute computation happens, and many mathematical aspects of this layer are written in C++ to speed up computation time for larger numbers.
 
### Output
 The final layer of the artificial intelligence is reserved for output, typically in the form of images. These outputs are stored in one folder with the most strongly related result being prioritized in the first image and additional information regarding the problem stored in the following images.
 
## Download
 While this project is not finished or finalized in any form, the code, in its entirety, remains open source and can be downloaded at any time. No particular setup is required.
 
 If any errors or exceptions are raised, add the path of the project to your PATH variable and ensure all imported libraries are installed in your Python folder. Make sure you have both the MinGW C++ compiler with at least C++17 and at least Python 3.7 installed on your system and added to your PATH variable.
 
 No official documentations of the syntax exist, and a GUI (graphical user interface) is not supported, but basic input can be given in the input file found in the root directory of the project.
