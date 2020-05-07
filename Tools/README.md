# Tools
|-|tensorflow|pytorch|
|:--:|:--:|:--:|
|Requirements|- Python 3.5-3.7<br>- pip 19.0 이상(manylinux2010 지원 필요)<br>- Ubuntu 16.04이상(64비트)<br>- macOS 10.12.6(Sierra) 이상(64비트)<br>*(GPU 지원x)*|[Operating systems<br>that support PyTorch](https://developer.ibm.com/technologies/artificial-intelligence/articles/cc-get-started-pytorch/) 참고|
|Installation|```pip install tensorflow```<br>(CPU+GPU 최신버전 설치)<br><br>- 특정 CPU: ```pip install tensorflow==1.15```<br>- 특정 GPU: ```pip install tensorflow-gpu==1.15```|[:octocat:](https://pytorch.org/)|
|Update|```pip3 install --upgrade tensorflow```<br>```pip3 install --upgrade tensorflow-gpu```|```conda update pytorch torchvision cudatoolkit -c pytorch```|
|Document|[:octocat:](https://www.tensorflow.org/install/pip?hl=ko#virtualenv-%EC%84%A4%EC%B9%98)|[:octocat:](https://tutorials.pytorch.kr/)|