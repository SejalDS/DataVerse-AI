FROM python:3.11-slim

WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Pre-install all data science libraries
RUN pip install --no-cache-dir \
    pandas==2.0.3 \
    numpy==1.24.3 \
    matplotlib==3.7.2 \
    seaborn==0.12.2 \
    scipy==1.11.1 \
    scikit-learn==1.3.0 \
    plotly==5.15.0

RUN mkdir -p /workspace/temp

ENV PYTHONPATH=/workspace:$PYTHONPATH

CMD ["/bin/bash"]