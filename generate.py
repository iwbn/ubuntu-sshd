import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='make ssh-enabled docker image from base image')
parser.add_argument('base_image', type=str, help='base image name')
args = parser.parse_args()


with open("Dockerfile.template", 'r') as f:
	template = f.read()


res = template.replace("%BASE-DOCKER%", args.base_image)


name = args.base_image.split("/")[-1]
base_name = name.split(":")[0]
if len(args.base_image.split(":")) > 1:
	raise ValueError("plase give base_image name with tag")
base_tag = args.base_image.split(":")[1]
new_name = base_name + "-sshd" + ":" + base_tag

dir_name = new_name

os.makedirs(dir_name, exist_ok=True)
with open(os.path.join(dir_name, 'Dockerfile'), 'w') as f:
	f.write(res)
subprocess.run(['docker build -t %s .' % new_name], shell=True, check=True, cwd=dir_name)

