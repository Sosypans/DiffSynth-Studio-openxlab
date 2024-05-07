import os

def sd_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//realisticasianthaila_v20 -d /home/xlab-app-center/models/stable-diffusion -o realisticasianthaila_v20.ckpt")
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//DreamShaper_8_pruned -d /home/xlab-app-center/models/stable-diffusion -o DreamShaper_8_pruned.safetensors")
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//rev-animated-v1-2-2 -d /home/xlab-app-center/models/stable-diffusion -o rev-animated-v1-2-2.safetensors")

def sdXL_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//realistic_bailingXL_v2.safetensors -d /home/xlab-app-center/models/stable-diffusion_xl -o realistic_bailingXL_v2.safetensors")

def AnimateDiff_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/houshaowei/AnimateDiff/weight//mm_sd_v15.ckpt -d /home/xlab-app-center/models/AnimateDiff -o mm_sd_v15.ckpt")

#多进程启动
import multiprocessing
multiprocessing.Process(target=sd_model_download).start()
multiprocessing.Process(target=AnimateDiff_model_download).start()
multiprocessing.Process(target=sdXL_model_download).start()
