# bert-naver

## 준
GPU의 갯수와 GPU 이름을 출력합니다.
```
import torch
import os

n_devices = torch.cuda.device_count()
print(n_devices)

for i in range(n_devices):
    print(torch.cuda.get_device_name(i))
```

torch, keras, tf 등 기존 ML/DL 패키지 외 필요한 패키지와 데이터를 다운받습니다.
Huggingface의 transformer와 네이버 영화 리뷰 데이터입니다.

```
!pip install transformers
!git clone https://github.com/e9t/nsmc.git 
```


이제 정말로 시작합니다. 필요한 패키지를 import해줍니다.
제일 중요한 건 파이토치와 트랜스포머입니다.

```
import tensorflow as tf
import torch

from transformers import BertTokenizer
from transformers import BertForSequenceClassification, AdamW, BertConfig
from transformers import get_linear_schedule_with_warmup
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import random
import time
import datetime
```

git clone을 하면 현재 파이썬 파일 혹은 Jupyter notebook이 있는 자리에 nsmc라는 이름의 디렉토리가 생성되었을 것입니다.    
해당 디렉토리 내의 train, test 텍스트 파일을 불러옵니다.

```
train = pd.read_csv("nsmc/ratings_train.txt", sep='\t')
test = pd.read_csv("nsmc/ratings_test.txt", sep='\t')

print(train.shape)
print(test.shape)
```
출력하면 output으로 각각 (150000, 3), (50000, 3)이 출력됩니다.      
전체의 25%가 테스트셋으로 배분되어있는 데이터입니다. 

## 전처리
### Train Set 전처리

train이 어떻게 생겼는지 확인해봅니다.
```
train.head(5)
```


```

```


```

```


```

```


```

```


```

```


```

```


```

```


