import os
import subprocess

IMAGES = [
	'nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04',
	'nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04',
	'nvidia/cuda:10.2-cudnn7-devel-ubuntu16.04',
	'nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04',
	'nvidia/cuda:10.2-cudnn8-devel-ubuntu16.04',
	'nvidia/cuda:10.2-cudnn8-devel-ubuntu18.04',
	'nvidia/cuda:11.0-cudnn8-devel-ubuntu18.04',
	'nvidia/cuda:11.1-cudnn8-devel-ubuntu18.04',
	'tensorflow/tensorflow:nightly-gpu',
	'tensorflow/tensorflow:latest-gpu',
	'pytorch/pytorch:1.7.0-cuda11.0-cudnn8-devel',
	'pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel',
	'pytorch/pytorch:1.5.1-cuda10.1-cudnn7-devel'
]

for image in IMAGES:
	subprocess.run(['python3 generate.py %s' % image], shell=True, check=True)

