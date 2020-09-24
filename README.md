# How to run the comparison test:


## **Install Python 3.X** ##
In order to be able to run the comparator test, Python 3.X needs to be installed in the machine. Most *nix based Operating systems come with Python 3.X installed.
To check if python is already installed run the below command in your terminal:
> python3 --version

The output should be as shown below if Python is already installed:
> Python 3.6.8

If you get an error `command python3 not found`, then you need to install Python before running the test. You can download and install Python from  https://www.python.org/downloads/


## **Install the python package manager - pip**
Once Python is installed, run the below command in the terminal, to install the python pacakage manager - pip:
> sudo apt install python-pip

The above command is for Debian distributions of Linux OS. More info can be found at:
- [Installing pip](https://pip.pypa.io/en/stable/installing/)
- [Installing using linux tools](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)


## **Clone the repository** 
Clone the repository to your local machine


## **Install dependencies**
- Go to the project directory
- Run the command `pip install -r requirements.txt`.
- All required packages would be installed in your machine.


## **Run the test**
From within the project root directory, run the following command:
> pytest comparator.py


## **Configuring the variance limit**

The default tolerance value for the variance is set as 2 units. If you wish to change this value, you can do so in the `config.json` file in the **config** directory.

Open the config.json file. Find the element with the name *VARIANCE_TOLERANCE_LIMIT* in the file. Change this value to any positive/negative number as required.  