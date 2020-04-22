## Ubuntu 18.04 Matplotlib 한글 폰트 설치

**2020년 4월 21**

설치된 기본 폰트 확인

```zsh
ls -l /usr/share/fonts/
ls -l /usr/share/fonts/truetype/
```

네이버 나눔글꼴 설치 및 폰트 캐시 삭제

```zsh
sudo apt-get install fonts-nanum
sudo fc-cache -fv
```

나눔 글꼴 복사

```zsh
# Python
sudo cp /usr/share/fonts/truetype/nanum/Nanum* /usr/local/lib/python3.7/dist-packages/matplotlib/mpl-data/fonts/ttf/

# Anaconda 가상환경
sudo cp /usr/share/fonts/truetype/nanum/Nanum* /home/unerue/anaconda3/envs/"name"/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/

sudo fc-cache -fv
```

`jupyter lab`

```python
import matplotlib.font_manager

[f.fname for f in matplotlib.font_manager.fontManager.ttflist]
```


## Ubuntu 18.04

```zsh
conda install -c conda-forge opencv=4.1.0
```

## Ubuntu and Mac

우분투에서...
```zsh
ssh name@host -p 
sudo vim /etc/ssh/sshd_config
```

```vim
X11Forwarding yes
X11DisplayOffset 10
PrintMotd no
PrintLastLog yes
TCPKeepAlive yes
```
맥에서...
```zsh
cd ~/.ssh
vim config
```

```vim
host name
  Hostname name
  Port 22
  ForwardAgent yes
  ForwardX11 yes
```
opencv 버전 4에서 영상이 됨