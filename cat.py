!git clone https://github.com/TheStingerX/Ilaria-RVC-Mainline
!pip install aria2
import codecs
from IPython.display import clear_output, Javascript
import urllib.request
e = codecs.decode('IbvprPbairefvbaJroHV','rot_13')
%cd Ilaria-RVC-Mainline
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/D32k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o D32k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/D40k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o D40k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/D48k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o D48k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/G32k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o G32k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/G40k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o G40k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/G48k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o G48k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/f0D32k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o f0D32k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/f0D40k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o f0D40k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/f0D48k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o f0D48k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/f0G32k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o f0G32k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/f0G40k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o f0G40k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/pretrained_v2/f0G48k.pth -d /content/Ilaria-RVC-Mainline/assets/pretrained_v2 -o f0G48k.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/hubert_base.pt -d /content/Ilaria-RVC-Mainline/assets/hubert -o hubert_base.pt
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://raw.githubusercontent.com/poiqazwsx/Ilaria-RVC-Mainline/main/assets/hubert/hubert_inputs.pth -d /content/Ilaria-RVC-Mainline/assets/hubert -o hubert_inputs.pth
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lj1995/{e}/resolve/main/rmvpe.pt -d /content/Ilaria-RVC-Mainline/assets/rmvpe -o rmvpe.pt
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://github.com/poiqazwsx/Ilaria-RVC-Mainline/blob/main/assets/rmvpe/rmvpe_inputs.pth -d /content/Ilaria-RVC-Mainline/assets/rmvpe -o rmvpe.pth
urllib.request.urlretrieve("https://raw.githubusercontent.com/poiqazwsx/Ilaria-RVC-Mainline/main/infer/lib/audio.py", "/content/Ilaria-RVC-Mainline/infer/lib/audio.py")
print("File replaced successfully.")
%mkdir /content/Ilaria-RVC-Mainline/assets/weights
!pip install -r requirements.txt
clear_output()
print("Finished Installing")


import codecs
abc = codecs.decode("vasre-jro", "rot_13")
!python {abc}.py --colab
