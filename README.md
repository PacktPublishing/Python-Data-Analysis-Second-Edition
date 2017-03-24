# Python Data Analysis Second Edition
Python Data Analysis Second Edition by Packt

This is the code repository for [Python Data Analysis - Second EditionPython Data Analysis - Second Edition](https://www.packtpub.com/big-data-and-business-intelligence/python-data-analysis-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781787127487), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Go toData analysis allows making sense of heaps of data. Python, with its strong set of libraries, is a popular language used today to conduct various data analysis, machine learning and visualization tasks.

With this book, you will learn about data analysis with Python in the broadest sense possible, covering everything from data retrieval, cleaning, manipulation, visualization, and storage to complex analysis and modeling. It focuses on a plethora of open source Python modules such as NumPy, SciPy, matplotlib, pandas, IPython, Cython, scikit-learn, and NLTK. In later chapters, the book covers topics such as data visualization, signal processing, and time-series analysis, databases, predictive analytics and machine learning. This book will turn you into an ace data analyst in no time. Mapt
## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
import scipy.io.wavfile as sw import matplotlib.pyplot as plt import urllib
import numpy as np

request = urllib.request.Request('http://www.thesoundarchive.com/austinpowers/smashin gbaby.wav')
response = urllib.request.urlopen(request) print(response.info())
WAV_FILE = 'smashingbaby.wav' filehandle = open(WAV_FILE, 'wb') filehandle.write(response.read()) filehandle.close()
sample_rate, data = sw.read(WAV_FILE)
print("Data type", data.dtype, "Shape", data.shape)

plt.subplot(2, 1, 1) plt.title("Original") plt.plot(data)

newdata = data * 0.2
newdata = newdata.astype(np.uint8)
print("Data type", newdata.dtype, "Shape", newdata.shape) sw.write("quiet.wav", sample_rate, newdata)
plt.subplot(2, 1, 2) plt.title("Quiet") plt.plot(newdata)2

plt.show()
 

```

The code examples in this book should work on most modern operating systems. For all
chapters, Python > 3.5.0 and pip3 is required. You can download Python 3.5.x from https
://www. python. org/downloads/. On this webpage, you can find installers for Windows
and Mac OS X as well as source archives for Linux, Unix, and Mac OS X. You can find
instructions for installing and using python for various operating systems on this webpage:
https://docs.python.org/3/using/index.html. 

## Related Products
* [Mastering Python Data Analysis](https://www.packtpub.com/big-data-and-business-intelligence/mastering-python-data-analysis?utm_source=github&utm_medium=repository&utm_campaign=9781783553297)

* [Getting Started with Python Data Analysis](https://www.packtpub.com/big-data-and-business-intelligence/getting-started-python-data-analysis?utm_source=github&utm_medium=repository&utm_campaign=9781785285110)

* [Data Mining with Python: Implementing Classification and Regression](https://www.packtpub.com/big-data-and-business-intelligence/data-mining-python-implementing-classification-and-regression?utm_source=github&utm_medium=repository&utm_campaign=9781785885716)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
