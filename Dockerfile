FROM jupyterhub/jupyterhub:latest

WORKDIR /srv/jupyterhub

# Install JupyterLab (single-user server)
RUN pip install --no-cache-dir jupyterlab notebook

# Ensure PATH includes venv bin
ENV PATH="/srv/venv/bin:$PATH"

# Copy files
COPY jupyterhub_config.py .
COPY my_authenticator.py .

EXPOSE 8080

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
