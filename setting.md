
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
import matplotlib

[f.fname for f in matplotlib.font_manager.fontManager.ttflist]
```
