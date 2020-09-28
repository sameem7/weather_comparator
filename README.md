# How to run the comparison test:


## **Requirements**

- Softwares:
  - Google Chrome 
  - Python 3.X
  - Python package manager - pip3
- OS:
  - macOS (Verified)
  - Windows (Verified)
  - Linux (I currently do not have a Linux machine, so could not verify the test execution in Linux)

***Note: Skip to step 4 if Google Chrome, Python 3.x and pip3 are already installed***

## **1. Install Google Chrome** ##
Download and install the Google Chrome browser from 

## **2. Install Python 3.X** ##
In order to be able to run the comparator test, Python 3.X needs to be installed in the machine. Most *nix based Operating systems come with Python 3.X installed.
To check if python is already installed run the below command in your terminal:
> python3 --version

The output should be as shown below if Python is already installed:
> Python 3.6.8

If you get an error `command python3 not found`, then you need to install Python before running the test. You can download and install Python from  https://www.python.org/downloads/


## **3. Install the python package manager - pip**
Once Python is installed, run the below command in the terminal, to install the python pacakage manager - pip:
> sudo apt install python-pip

The above command is for Debian distributions of Linux OS. More info can be found at:
- [Installing pip](https://pip.pypa.io/en/stable/installing/)
- [Installing using linux tools](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)


## **4. Clone the repository** 
Clone the repository to your local machine


## **5. Install dependencies**
- Go to the project root directory
- Run the command `pip install -r requirements.txt`.
- All required packages would be installed in your machine.


## **6. Run the test suites**
From within the project root directory, run the following command to execute all tests:
> robot test

To run the test suites individually:
  > robot test/<test_suite_name>.robot

Example:
  > robot test/comparator_data_driven_test.robot


## **7. View the generated reports** 

- Once the test execution is completed, there will be 3 report files created in the root directory:
    - *output.xml*
    - *log.html*
    - *report.html*
- Test Execution results are present in the *report.html* file.
- Copy the path of *report.html* and paste it in a browser, to view the HTML report.
  - After the completion of the test execution, the path of *report.html* will be available in the terminal. The path can also be copied here.




## **8. Configuring the variance limit**

The default tolerance value for the variance is set as 2 units. If you wish to change this value, you can do so in the `config.json` file in the **config** directory.

Open the config.json file. Find the element with the name *VARIANCE_TOLERANCE_LIMIT* in the file. Change this value to any positive/negative number as required.  