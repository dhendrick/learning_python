# learning_python

## How to run the web service

    python app.py

## How to use the AWS console

    https://console.aws.amazon.com/

    Login as a root user
    user: dan.hendrick@gmail.com
    password: ?

    Go to the EC2 service page to create/stop/start machines

## How to copy a file from your laptop to an EC2 machine

    scp -i emily-ec2-machine.pem requirements.txt ec2-user@54.158.190.135:/home/ec2-user/

## How to login to an EC2 machine

    ssh -i emily-ec2-machine.pem ec2-user@54.158.190.135

## Example EC2 machine commands

    # What directory am I in?
    pwd
    
    # List the files in the current directory
    ls -l

    # What version of python is installed?
    python -V

    # Become the super user (administrator)
    sudo su

    # Install Python version 3
    yum install python3

    # Verify the verson of Python 3
    python3 -V

    # Install needed Python packages
    pip3 install -r requirements.txt 

    # Exit the super user account
    exit

    # Run the Python web service (using Python 3). To stop, use Ctrl-C.
    python3 app.py 

    # Edit a Python file
    vi app.py 

    # Exit the EC2 machine
    exit

