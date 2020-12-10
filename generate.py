import os
import subprocess

with open("Dockerfile.template", 'r') as f:
	template = f.read()

CUDA_CUDNN_VERSION = [("10.1", "7"), ("10.2", "7"), ("10.2","8"), ("11.0", "8")]
UBUNTU_VERSION = ["18.04"]


for ubuntu_version in UBUNTU_VERSION:
	for cuda_version, cudnn_version in CUDA_CUDNN_VERSION:
		res = template.replace("%CUDA_VERSION%", cuda_version)
		res = res.replace("%UBUNTU_VERSION%", ubuntu_version)
		res = res.replace("%CUDNN_VERSION%", cudnn_version)
		
		dir_name = '%s-%s-%s' % (ubuntu_version, cuda_version, cudnn_version)

		os.makedirs(dir_name, exist_ok=True)
		with open(os.path.join(dir_name, 'Dockerfile'), 'w') as f:
			f.write(res)
		subprocess.run(['docker build -t %s .' % "sgvr-gpu-base:2.0-cuda%s-cudnn%s-devel-ubuntu%s" % (cuda_version, cudnn_version, ubuntu_version)], shell=True, check=True, cwd=dir_name)

