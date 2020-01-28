# EISEN

Eisen is a package that consists of popular datasets, 
model architectures, data loading functions, common image 
transformations, training, testing and validation work-flows
which are useful when working on medical image analysis tasks
using deep learning.

Eisen implements an opinionated API that builds directly 
on PyTorch. The goal of Eisen is to be:
* Extremely simple to use
* Extremely easy to understand
* Similar to other packages in the PyTorch echosystem
* Easy to contribute to

When developing Eisen we have therefore decided to keep the
number of lines of code to the minimum, adopt a 
component-based architecture, 
avoid over-engineering and promote an easy-to-follow 
coding style. 

Users of Eisen should be able to get started in a few minutes,
by following the examples contained in this README.

Developers of Eisen should be able to grasp the entire 
code-base in a few hours. 

Simplicity is the answer.

## This repository

Contains just the code to create a meta package for Eisen such that 
all its components can be installed easily by only executing

```
pip3 install eisen
```