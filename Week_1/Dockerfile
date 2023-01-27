# this is the image name
FROM python:3.9 
# this is the command I want to run
RUN pip install pandas
# this creates a working directory and cd s into it
WORKDIR /app
# this copies pipeline.py on my host machine into the container
COPY pipeline.py pipeline.py
# this executes python pipeline.py in bash
ENTRYPOINT ["python", "pipeline.py"]