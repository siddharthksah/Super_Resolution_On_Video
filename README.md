# Easy to use Super resolution implementation

![Upscaled](upscaled.jpeg)


Below are instructions to implement in in your local system using a separate development environment using the [Conda](http://conda.pydata.org/docs/index.html) package management system which comes bundled with the Anaconda Python distribution provided by Continuum Analytics.

### Step 1:
[Fork and clone](https://github.com/siddharthksah/Super_Resolution_On_Video) a copy of this repository on to your local machine.

### Step 2:
Create a `conda` environment called `super-resolution` and install all the necessary dependencies, the environment.yml file is uploaded in the repo for ease:

    $ conda env create -n super-resolution python=3.8 -y
    
### Step 3:
Install the extra dependencies, it is not required but helps in making sure the jupyter notebook is running in the right conda env:

    $ pip install -r requirement.txt
    $ conda install nb_conda

### Step 4:
Activate the `super-resolution' environment:

    $ source activate super-resolution

To confirm that everything has installed correctly, type

    $ which pip

at the terminal prompt. You should see something like the following:

    $ ~/anaconda/envs/super-resolution/bin/pip

which indicates that you are using the version of `pip` that is installed inside the `super-resolution` Conda environment and not the system-wide version of `pip` that you would normally use to install Python packages.

### Step 5:
Change into your local copy of the this repo:

    $ cd Super_Resolution_On_Video

### Step 6:
Run the code:

    $ python3 loop.py


Inspired from [ISR](https://github.com/idealo/image-super-resolution)
