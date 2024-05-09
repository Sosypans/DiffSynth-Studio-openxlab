import os

def sd_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//realisticasianthaila_v20 -d /home/xlab-app-center/models/stable_diffusion -o realisticasianthaila_v20.ckpt")
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//DreamShaper_8_pruned.safetensors -d /home/xlab-app-center/models/stable_diffusion -o DreamShaper_8_pruned.safetensors")
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//rev-animated-v1-2-2.safetensors -d /home/xlab-app-center/models/stable_diffusion -o rev-animated-v1-2-2.safetensors")

def sdXL_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//realistic_bailingXL_v2.safetensors -d /home/xlab-app-center/models/stable_diffusion_xl -o realistic_bailingXL_v2.safetensors")

def AnimateDiff_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/houshaowei/AnimateDiff/weight//mm_sd_v15.ckpt -d /home/xlab-app-center/models/AnimateDiff -o mm_sd_v15.ckpt")

#def lora_model_download():
def Jupyter_start():
  import subprocess
  import threading
  import time
  import socket
  import urllib.request
  ngrok_command = f"ngrok tunnel --label edge=edghts_2gArJM3tI9Q5SlPc0geDZRSXW6d --authtoken=2bsl75MUm8RmOcXO4Unrtfpu0jb_7MVgK4P6CyufseMyAY7Xv --region=ap http://localhost:8889"
  jupyter_command = "jupyter-lab --no-browser --ip=0.0.0.0 --allow-root --notebook-dir=/ --port=8889 --LabApp.allow_origin=* --LabApp.token= --LabApp.base_url="
  # 启动 ngrok 进程
  ngrok_process = subprocess.Popen(ngrok_command, shell=True)
  # 启动 Jupyter 进程
  jupyter_process = subprocess.Popen(jupyter_command, shell=True)


#多进程启动
import multiprocessing
#multiprocessing.Process(target=sd_model_download).start()
#multiprocessing.Process(target=AnimateDiff_model_download).start()
#multiprocessing.Process(target=sdXL_model_download).start()
#multiprocessing.Process(target=lora_model_download).start()
multiprocessing.Process(target=Jupyter_start).start()
