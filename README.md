# pyramid-surveymonkey-example
A boiler plate web app that connects to the SurveyMonkey v3 API

## Windows Instructions
### Install Python 3.7 & pip
Python 3.7 can be installed along with pip [here](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe).

#### What is Python 3.7?
Python is the programming language we're using with this example codebase. Python is an interpreted language, which means we need to install an interpreter to run our Python scripts. More information [here](https://www.python.org/doc/essays/blurb/).

#### What is pip?
pip is a package management system used to install and manage software packages written in Python. This is similar to composer in PHP, NuGET in C#, npm in JavaScript...etc.

We'll want to add the `python` & `pip` commands to our `Path` variable.

   1. Open the `Environment Variables` window. On Windows 10 this can be done by searching `edit environment variables for your account` in the Start menu.
   1. Edit the `Path` variable either for the current User or the System.
   1. Add the full path to the folder containing `python.exe` to the beginning of the `Path` variable. For example, mine was located at `C:\Users\Scott\AppData\Local\Programs\Python\Python37-32`.
   1. Also add the full path to the folder containing `pip.exe` to the beginning of the `Path` variable. For example, mine was located in the same path as `python.exe` under the `Scripts` folder.
   1. Confirm the changes.
   1. Open up Command Prompt (`cmd` in Start menu) and type `python`, a Python shell should appear. **Note: Restarting the computer may be required for these changes to be recognized**

### Install virtualenv
In the Command Prompt, run `pip install virtualenv`.

#### What is virtualenv?
virtualenv is a tool to create isolated Python environments. This is useful for keeping all the packages we install with `pip` in one project separated from the packages in another project. We can even use virtual environments to run different versions of Python from the one specified in the `Path`.

### Create & activate a virtual environment
   1. If you haven't already, clone this repo to the local machine.
   1. With Command Prompt, navigate to the root of this project on the local machine and run `virtualenv pyenv`.
   1. Activate the virtual environment by running `pyenv\Scripts\activate` from the project root.
   1. `(pyenv)` should now be visible to the left of the command prompt.

#### What happened?
We've just created a virtual environment folder named `pyenv` using the default version of Python we installed and hooked up to the `Path`. We've also activated the virtual environment, which means all future `python` & `pip` commands will be run in this isolated environment. So if we install a package using `pip` it'll be available to us when we use a Python shell, but it won't be available if we leave this environment or activate a different virtual environment where we haven't installed the package.

**NOTE: To leave a virtual environment, simply run `deactivate` from within the virtual enviroment.**
