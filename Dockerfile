FROM registry.fedoraproject.org/f33/python3

# Add application sources with correct permissions for OpenShift
USER 0

# Add required files
ADD main.py .
ADD requirements.txt .
ADD data .
ADD images .
ADD pages .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 3000 
EXPOSE 3000

# Run an app
CMD python3 main.py --host=0.0.0.0 --port=3000