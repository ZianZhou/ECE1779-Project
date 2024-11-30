FROM python:3.10-slim
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*
RUN curl -o coverity_tool.tgz https://example.com/path-to-coverity-tool.tgz && \
    tar -xvzf coverity_tool.tgz && \
    mv cov-analysis-linux64-* /opt/coverity
ENV PATH="/opt/coverity/bin:$PATH"
RUN pip install flask
COPY app.py /app/app.py
EXPOSE 5000
CMD ["python", "/app/app.py"]
