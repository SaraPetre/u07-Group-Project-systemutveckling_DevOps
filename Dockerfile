# import default image
FROM python:latest
# The default dir to work from
WORKDIR /app
# copy requirements list and add to workdir using ./
COPY requirements.txt ./
# Run pip install requirements
RUN pip install -r requirements.txt
# This lines copy all code from . = my app-folder and .. is the routers-folder within app-folder.
COPY . .
# this starts the image.
CMD ["python3", "src/main.py"]