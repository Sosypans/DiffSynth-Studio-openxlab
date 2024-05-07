import os

def sd_model_download():
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//realisticasianthaila_v20 -d /home/xlab-app-center/models/Stable-diffusion -o realisticasianthaila_v20.ckpt")
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//DreamShaper_8_pruned -d /home/xlab-app-center/models/Stable-diffusion -o DreamShaper_8_pruned.safetensors")
  os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/Tinsley/realisticasianthaila/weight//rev-animated-v1-2-2 -d /home/xlab-app-center/models/Stable-diffusion -o rev-animated-v1-2-2.safetensors")

#多进程启动
import multiprocessing
multiprocessing.Process(target=sd_model_download).start()
