# import default image
FROM python:latest
# The default dir to work from
WORKDIR /src/
# copy requirements list and add to workdir using ./
COPY ./requirements.txt ./
# Run pip install requirements
RUN pip install --no-cache-dir -r requirements.txt
# This lines copy all code from . = my app-folder and .. is the routers-folder within app-folder.
COPY . .
# this starts the image.
CMD ["python3", "src/main.py"]
