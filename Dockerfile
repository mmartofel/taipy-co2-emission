FROM registry.fedoraproject.org/f33/python3

# Add application sources with correct permissions for OpenShift
USER 0

# Add required files
ADD main.py .
ADD requirements.txt .
COPY data data
COPY images images
COPY pages pages

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 3000 
EXPOSE 3000

# Run an app
# CMD python3 main.py --host=0.0.0.0 --port=3000
CMD ["taipy", "run", "--no-debug", "--no-reloader", "main.py", "--host", "0.0.0.0", "-P", "3000"]
# CMD ["sleep", "infinity"]