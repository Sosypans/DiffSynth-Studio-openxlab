# 给我的朋友写的
import os
import threading
#使用的库
from pathlib import Path
import subprocess
import pandas as pd
import shutil
import os
import time
import re
import gc
import requests
import zipfile
import threading
import time
import socket
from concurrent.futures import ProcessPoolExecutor
# import wandb
import base64
import subprocess

try:
    def notbook():
        os.system("pip install jupyterlab")
        os.system("pip install pyngrok")
        # 构建命令字符串
        ngrok_command = f"ngrok http 8889 --authtoken=2cdw5pJsqgsq1igQKeHIpNwTNG7_7LQD3jojKKQ7PzcnNkok5"
        ngrok_command2 = f"ngrok tunnel --label edge=edghts_2doueG9BDi9rCXUGnsSsNbTab8H --authtoken=2douOsr61tUyYwMVF3lfj9uZGoa_6FPJ2x1xhKPbL6z4euKkM --region=ap http://localhost:8889"
        jupyter_command = "jupyter-lab --no-browser --ip=0.0.0.0 --allow-root --notebook-dir=/ --port=8889 --LabApp.allow_origin=* --LabApp.token= --LabApp.base_url="

        # 启动 ngrok 进程
        ngrok_process = subprocess.Popen(ngrok_command, shell=True)
        time.sleep(30)
        ngrok_process2 = subprocess.Popen(ngrok_command2, shell=True)
        # 启动 Jupyter 进程
        jupyter_process = subprocess.Popen(jupyter_command, shell=True)
        #os.system(f"ngrok tunnel --authtoken={ngrok_token} --region=ap http://localhost:8888 & python jupyter-lab --ServerApp.shutdown_no_activity_timeout=1800 --TerminalManager.cull_inactive_timeout=1800 --TerminalManager.cull_interval=300 --MappingKernelManager.cull_idle_timeout=1800 --MappingKernelManager.cull_interval=300 --MappingKernelManager.cull_connected=True --MappingKernelManager.cull_busy=True --no-browser --ip=0.0.0.0 --allow-root --notebook-dir=/ --port=8888 --LabApp.token= --LabApp.allow_origin=* --LabApp.base_url=")

    ngrok_token = "2bgXLjjKFvxfbuZFlR2NMZkvL8n_4WrK7f15FLtWb8p7v3oaF"
    _ngrok_token = "2CXyNlT9xGfFoL5ruI6hQV20FNq_7tbmuzS9RtyNTkyEe1J6C"

    os.system("pip install nvidia-ml-py3")
    os.chdir(f"/home/xlab-app-center/test2")
    os.system(f"git clone https://openi.pcl.ac.cn/2575044704/stable-diffusion-webui-v1.8.0 /home/xlab-app-center/test2/stable-diffusion-webui")

    os.system(f"cp /home/xlab-app-center/test2/styles.csv /home/xlab-app-center/test2/stable-diffusion-webui/styles.csv")
    os.chdir(f"/home/xlab-app-center/test2/stable-diffusion-webui")
    os.system(f"git lfs install")
    os.system(f"git reset --hard")
    import os

    ngrok_token = "2bgXLjjKFvxfbuZFlR2NMZkvL8n_4WrK7f15FLtWb8p7v3oaF" #7862端口
    _ngrok_token = "2CXyNlT9xGfFoL5ruI6hQV20FNq_7tbmuzS9RtyNTkyEe1J6C" #7863端口

    def remove_restart():
        os.chdir("/home/xlab-app-center/test2/stable-diffusion-webui/html")
        os.system("rm ./footer.html && wget -O footer.html https://hf-mirror.com/datasets/ACCA225/openxlab/resolve/main/footer.html")
        os.chdir("/home/xlab-app-center/test2/stable-diffusion-webui/modules")
        os.system("rm ./ui_settings.py && wget -O ui_settings.py https://hf-mirror.com/datasets/ACCA225/openxlab/resolve/main/ui_settings.py")
    remove_restart()
    def create_directory(directory_path):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    def download_file(url, destination_path):
        os.system(f'wget -O {destination_path} {url}')

    # 设置基本路径
    base_directory = '/home/xlab-app-center/test2/stable-diffusion-webui'
    configs_directory = os.path.join(base_directory, 'configs')

    # 创建configs文件夹
    create_directory(configs_directory)

    # 下载配置文件
    #download_file('https://hf-mirror.com/datasets/ACCA225/openxlab/resolve/main/config-pub.json', os.path.join(configs_directory, 'config.json'))
    #download_file('https://hf-mirror.com/datasets/ACCA225/openxlab/resolve/main/ui-config-pri2.json', os.path.join(configs_directory, 'ui-config-pri.json'))
    #download_file('https://hf-mirror.com/datasets/ACCA225/openxlab/resolve/main/ui-config-pub.json', os.path.join(configs_directory, 'ui-config.json'))
    # 下载配置文件
    download_file('https://hf-mirror.com/datasets/ACCA225/openxlab/resolve/main/config-pub.json', os.path.join(base_directory, 'config.json'))
    download_file('https://hf-mirror.com/datasets/ACCA225/openxlab/resolve/main/ui-config-pri2.json', os.path.join(base_directory, 'ui-config-pri.json'))
    download_file('https://hf-mirror.com/datasets/ACCA225/openxlab/resolve/main/ui-config-pub.json', os.path.join(base_directory, 'ui-config.json'))
    download_file('https://hf-mirror.com/datasets/ACCA225/openxlab/resolve/main/ui-config-pub2.json', os.path.join(base_directory, 'ui-config2.json'))

    os.chdir(f"/home/xlab-app-center/test2/stable-diffusion-webui/extensions")
    os.system(f"rm -rf ./batchlinks-webui")
    os.system(f"rm -rf ./sd-extension-system-info")
    show_shell_info = False
    def run(command, cwd=None, desc=None, errdesc=None, custom_env=None,try_error:bool=True) -> str:
        global show_shell_info
        if desc is not None:
            print(desc)

        run_kwargs = {
            "args": command,
            "shell": True,
            "cwd": cwd,
            "env": os.environ if custom_env is None else custom_env,
            "encoding": 'utf8',
            "errors": 'ignore',
        }

        if not show_shell_info:
            run_kwargs["stdout"] = run_kwargs["stderr"] = subprocess.PIPE

        result = subprocess.run(**run_kwargs)

        if result.returncode != 0:
            error_bits = [
                f"{errdesc or 'Error running command'}.",
                f"Command: {command}",
                f"Error code: {result.returncode}",
            ]
            if result.stdout:
                error_bits.append(f"stdout: {result.stdout}")
            if result.stderr:
                error_bits.append(f"stderr: {result.stderr}")
            if try_error:
                print((RuntimeError("\n".join(error_bits))))
            else:
                raise RuntimeError("\n".join(error_bits))

        if show_shell_info:
            print((result.stdout or ""))
        return (result.stdout or "")
    import subprocess
    def sdmodel():
        def download_with_aria2(urls):
            # 使用循环遍历所有的下载链接
            for url in urls:
                # 将huggingface.co替换为hf-mirror.com
                url = url.replace('huggingface.co', 'hf-mirror.com')
                file_name = url.split('/')[-1].split('?')[0]
                # 构建aria2c命令
                command = f'aria2c -x 16 -s 16 -c -k 1M -o "{file_name}" "{url}" -d /home/xlab-app-center/test2/stable-diffusion-webui/models/Stable-diffusion'

                try:
                    # 使用subprocess模块运行aria2c命令
                    subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    # 打印错误信息（如果有）
                    print(f'Error downloading {url}: {e}')

        # 直接将链接作为多行字符串传递给函数
        download_urls = """
        https://huggingface.co/HiroHiroHirook/meinamix_meinaV8/resolve/main/meinamix_meinaV8.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/anything_v50.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/blindbox_v1_mix.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/cuteyukimixAdorable_naiV3style.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/ddicon_v10.ckpt?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/meinamix_meinaV11.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/meinapastel_v6-inpainting.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/meinapastel_v6Pastel.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/midjourney_20230624181825.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/mixProV4_v4.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/qteamixQ_omegaFp16.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/uberRealisticPornMerge_urpmv13.safetensors?download=true
        https://huggingface.co/datasets/ACCA225/kagglemodel/resolve/main/kaggle/temp/velaMix_velaMixVersion2.safetensors?download=true
        """

        # 使用字符串的splitlines方法将字符串分割成列表
        urls_list = download_urls.strip().splitlines()

        # 调用函数开始下载
        download_with_aria2(urls_list)
    #sdmodel()
    def mkdirs(path, exist_ok=True):
        if path and not Path(path).exists():
            os.makedirs(path,exist_ok=exist_ok)
    plugins = [
        "https://gitcode.net/overbill1683/stable-diffusion-webui-localization-zh_Hans",
        #"https://gitcode.net/ranting8323/multidiffusion-upscaler-for-automatic1111",
        "https://gitcode.net/ranting8323/adetailer",
        "https://gitcode.net/ranting8323/sd-webui-inpaint-anything",
        "https://gitcode.net/ranting8323/a1111-sd-webui-tagcomplete",
        "https://gitcode.net/nightaway/sd-webui-infinite-image-browsing",
        "https://openi.pcl.ac.cn/2575044704/sd-extension-system-info",
        "https://openi.pcl.ac.cn/2575044704/batchlinks-webui",
        'https://openi.pcl.ac.cn/2575044704/stable-diffusion-webui-localization-zh_CN',
        'https://openi.pcl.ac.cn/2575044704/sd-webui-lora-block-weight',
        'https://openi.pcl.ac.cn/2575044704/sd-skin-extension',
        "https://kkgithub.com/thygate/stable-diffusion-webui-depthmap-script.git",
        #"https://gitcode.net/ranting8323/sd-webui-controlnet",
        #"https://kkgithub.com/SignalFlagZ/sd-webui-civbrowser.git",
        #"https://kkgithub.com/continue-revolution/sd-webui-animatediff.git",
        #"https://kkkkgithub.com/aigc-apps/sd-webui-EasyPhoto.git",
        "https://kkgithub.com/Iyashinouta/sd-model-downloader.git",
        "https://kkgithub.com/fkunn1326/openpose-editor.git",
        "https://kkgithub.com/zero01101/openOutpaint-webUI-extension.git",
        "https://kkgithub.com/LonicaMewinsky/gif2gif.git",
        #"https://kkgithub.com/modelscope/facechain.git",
        "https://openi.pcl.ac.cn/2575044704/sd-webui-controlnet",
        "https://openi.pcl.ac.cn/2575044704/sd-webui-agent-scheduler",
        "https://openi.pcl.ac.cn/2575044704/sd-webui-depth-lib"
    ]
    suffix_1 = "Nyan9"
    suffix_2 = "BiliBili"
    needed_extensions = [
        "https://openi.pcl.ac.cn/2575044704/sd-extension-system-info",
        "https://openi.pcl.ac.cn/2575044704/batchlinks-webui",
    ]
    os.system("rm -rf /home/xlab-app-center/test2/stable-diffusion-webui/extensions/sd-webui-animatediff/")
    for plugin in plugins:
        os.system(f"git clone {plugin}")
    #for plugin in needed_extensions:
    #    os.system(f"git clone {plugin}")
    os.makedirs('/home/xlab-app-center/test2/stable-diffusion-webui/models/adetailer', exist_ok=True)
    os.chdir(f"/home/xlab-app-center/test2/stable-diffusion-webui/models/adetailer")
    os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/Bingsu/adetailer/resolve/main/hand_yolov8s.pt -d /home/xlab-app-center/test2/stable-diffusion-webui/models/adetailer -o hand_yolov8s.pt")
    os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/Bingsu/adetailer/resolve/main/hand_yolov8n.pt -d /home/xlab-app-center/test2/stable-diffusion-webui/models/adetailer -o hand_yolov8n.pt")
    os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/datasets/ACCC1380/private-model/resolve/main/kaggle/input/museum/131-half.safetensors -d /home/xlab-app-center/test2/stable-diffusion-webui/models/Stable-diffusion -o [萌二次元]131-half.safetensors")
    os.system(f"rm /home/xlab-app-center/test2/stable-diffusion-webui/models/Stable-diffusion/*porn*.safetensors")

    os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/datasets/ACCC1380/private-model/resolve/main/ba.safetensors -d /home/xlab-app-center/test2/stable-diffusion-webui/models/Lora -o ba.safetensors")
    os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/datasets/ACCC1380/private-model/resolve/main/racaco2.safetensors -d /home/xlab-app-center/test2/stable-diffusion-webui/models/Lora -o racaco2.safetensors")
    os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/coinz/Add-detail/resolve/main/add_detail.safetensors -d /home/xlab-app-center/test2/stable-diffusion-webui/models/Lora -o add_detail.safetensors")
    os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://hf-mirror.com/datasets/VASVASVAS/vae/resolve/main/pastel-waifu-diffusion.vae.pt -d /home/xlab-app-center/test2/stable-diffusion-webui/models/VAE -o pastel-waifu-diffusion.vae.pt")
    # os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/sdxl-refiner-1.0/weight//sd_xl_refiner_1.0.safetensors -d /home/xlab-app-center/test2/stable-diffusion-webui/models/Stable-diffusion -o sd_xl_refiner_1.0.safetensors")
    # os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/cyber-realistic/weight//cyberrealistic_v32.safetensors -d /home/xlab-app-center/test2/stable-diffusion-webui/models/Stable-diffusion -o cyberrealistic_v32.safetensors")
    os.chdir(f"/home/xlab-app-center/test2/stable-diffusion-webui")
    print('webui launching...')
    pwd_1 = ngrok_token + suffix_1
    pwd_2 = _ngrok_token + suffix_2
    package_envs = [
        {"env": "STABLE_DIFFUSION_REPO", "url": os.environ.get('STABLE_DIFFUSION_REPO', "https://gitcode.net/overbill1683/stablediffusion")},
        {"env": "STABLE_DIFFUSION_XL_REPO", "url": os.environ.get('STABLE_DIFFUSION_XL_REPO', "https://gitcode.net/overbill1683/generative-models")},
        {"env": "K_DIFFUSION_REPO", "url": os.environ.get('K_DIFFUSION_REPO', "https://gitcode.net/overbill1683/k-diffusion")},
        {"env": "CODEFORMER_REPO", "url": os.environ.get('CODEFORMER_REPO', "https://gitcode.net/overbill1683/CodeFormer")},
        {"env": "BLIP_REPO", "url": os.environ.get('BLIP_REPO', "https://gitcode.net/overbill1683/BLIP")},
    ]
    os.environ["PIP_INDEX_URL"] = "https://mirrors.aliyun.com/pypi/simple/"
    for i in package_envs:
        os.environ[i["env"]] = i["url"]

    import os
    import time
    import wandb
    import nvidia_smi
    import os
    import time
    import wandb

    # nginx 反向代理配置文件
    def echoToFile(content:str,path:str):
        if path.find('/') >= 0:
            _path = '/'.join(path.split('/')[:-1])
            run(f'''mkdir -p {_path}''')
        with open(path,'w') as sh:
            sh.write(content)
    # 检查网络
    def check_service(host, port):
        try:
            socket.create_connection((host, port), timeout=5)
            return True
        except socket.error:
            return False
    def localProxy():
        os.system('sudo apt install nginx -y')
        download_file('https://huggingface.co/datasets/ACCA225/openxlab/resolve/main/proxy_nginx.conf', os.path.join(base_directory, 'proxy_nginx.conf'))
        if not check_service('localhost',_server_port):
            run(f'''nginx -c /home/xlab-app-center/test2/stable-diffusion-webui/proxy_nginx.conf''')
        run(f'''nginx -s reload''')

    # WandB登录
    os.system('wandb login 5c00964de1bb95ec1ab24869d4c523c59e0fb8e3')
    nvidia_smi.nvmlInit()
    # 初始化WandB项目
    wandb.init(project="gpu-temperature-monitor")

    import threading
    import requests

    def check_website(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"The website {url} is accessible.")
            else:
                print(f"The website {url} returned status code: {response.status_code}")
                notbook()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while trying to access {url}: {e}")

    def run_check_periodically(url, interval):
        check_website(url)
        threading.Timer(interval, run_check_periodically, args=(url, interval)).start()


    import os
    import threading
    import wandb
    import time
    def monitor_gpu():
        while True:
            try:
                # 获取 GPU 温度
                handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)  # 0 表示第一个 GPU
                gpu_temperature = nvidia_smi.nvmlDeviceGetTemperature(handle, nvidia_smi.NVML_TEMPERATURE_GPU)

                # 获取 GPU 使用率
                utilization = nvidia_smi.nvmlDeviceGetUtilizationRates(handle)
                gpu_usage = utilization.gpu

                # 使用 WandB 记录 GPU 温度和使用率
                wandb.log({"GPU 温度": gpu_temperature, "GPU 使用率": gpu_usage})

            except Exception as e:
                print(f"Error: {e}")

            time.sleep(60)
    def zrok():
        notbook()

        #os.system("wget https://hf-mirror.com/datasets/ACCA225/frp-1/resolve/main/frpc")
        #os.system("chmod +x ./frpc")
        #os.system("./frpc -f bsnehoeds17ett71i2cr79ujoa7ndkxz:13738352 & ./frpc -f bsnehoeds17ett71i2cr79ujoa7ndkxz:13738353")
        pass

    _pwd_1 = base64.b64encode(pwd_1.encode()).decode()
    _pwd_2 = base64.b64encode(pwd_2.encode()).decode()

    apitoken = "{}:{}".format(_pwd_1, _pwd_2)
    def start():

        try:
            #安装环境
            os.system(f"python launch.py --api --xformers --exit --enable-insecure-extension-access --gradio-queue --disable-safe-unpickle")
        except Exception as e:
            # 在这里处理异常的代码
            print(f"启动SD发生错误: {e}")
        try:
            while True:
                #os.system(f"python launch.py --api --xformers --exit --enable-insecure-extension-access --ui-settings-file /home/xlab-app-center/test2/config.json --ui-config-file /home/xlab-app-center/test2/ui-config.json --gradio-queue --disable-safe-unpickle")
                os.system(f"python launch.py --xformers --enable-insecure-extension-access --gradio-queue --disable-safe-unpickle --allow-code")
        except Exception as e:
            # 在这里处理异常的代码
            print(f"启动SD发生错误: {e}")

    # 实例保活
    import time

    def session_saver():
        try:
            import cupy as cp
        except ImportError:
            print("cupy模块未安装，正在安装...")
            try:
                import pip
                pip.main(['install', 'cupy'])
                import cupy as cp
            except ImportError:
                print("无法安装模块，请确保已正确安装pip。")
                return

        while True:
            for _ in range(11):
                matrix_a = cp.random.rand(10000, 10000)
                matrix_b = cp.random.rand(10000, 10000)
                result = cp.dot(matrix_a, matrix_b)
                print("实例保活:", result)
                del matrix_a, matrix_b, result
                cp.cuda.Stream.null.synchronize()
            time.sleep(500)

    #keepliving_thread = threading.Thread(target=session_saver)
    net_thread = threading.Thread(target=zrok)

    net_thread.start()
    #keepliving_thread.start()

    start_thread = threading.Thread(target=start)
    start_thread.start()
    # 要检测的网站
    website_url = "https://surely-definite-monarch.ngrok-free.app"

    # 间隔时间（秒）
    interval = 1800

    # 第一次立即运行一次
    #run_check_periodically(website_url, interval)

    monitor_gpu()

    #keepliving_thread.join()
    time.sleep(9999999)
except Exception as e:
    print("执行这个线程的时候发生重大错误：", e)