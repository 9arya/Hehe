import kagglehub

# Download latest version
path = kagglehub.dataset_download("allenclose/amazon-india-sales-2025-analysis")

print("Path to dataset files:", path)