# ===============================
# Rebuild and Restart JupyterHub
# ===============================

Write-Host "Stopping existing container..."
docker stop jhub 2>$null

Write-Host "Removing existing container..."
docker rm jhub 2>$null

Write-Host "Removing old image..."
docker rmi my-jupyterhub 2>$null

Write-Host "Building fresh image..."
docker build --no-cache -t my-jupyterhub .

Write-Host "Starting new container..."
docker run -d -p 8000:8000 --name jhub my-jupyterhub

Write-Host ""
Write-Host "JupyterHub restarted successfully!"
Write-Host "Open: http://localhost:8000"
