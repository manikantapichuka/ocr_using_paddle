FROM paddlepaddle/paddle:3.0.0b1

# Install dependencies
RUN pip install --upgrade pip
RUN pip install paddleocr fastapi uvicorn

# Copy the server code
COPY app.py /app/app.py
WORKDIR /app

# Expose port for external access
EXPOSE 5000

# Run the PaddleOCR server
CMD ["python3", "app.py"]
