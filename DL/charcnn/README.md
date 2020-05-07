# charCNN
Character level Convolutional Networks for Text Classification(2015)

## 1. Abstract
bag of words, n-grams, TF-IDF variants, word-based CNN & RNN과 비교하여 charCNN의 성능을 실험적으로 탐구한 결과를 보여주는 논문

## 2. Introduction
* Text Classification 분야에서 word-based n-gram 모델이 좋은 성과를 보여주고 있음
* CNN은 raw signal에서 특성을 추출하는데 탁월한 성능을 보임
* 둘을 응용하여 charCNN model을 만들었음 

## 3. Character-level Convolutional Networks
1. Key Modules
   * max-pooling, ReLU, SGD 사용
2. Character quantization
   * quantize = encoding의 의미로  사용됨
   * m = alphabet 개수(숫자, 특수문자 포함)
   * one-hot encoding(1-of-m encoding) 사용
   * character sequence의 길이를 l0으로 고정.<br>이 길이를 초과하면 버리고, 부족하면 zero-vector를 채워줌
   * character quantization order는 backward로 해서 최근에 읽힌 character가 output의 시작 부분에 위치하도록 함
3. Model Design<br>
   * ![image](https://github.com/study-ai-data/Deep-Learning/blob/master/charcnn/charcnn_model_design.PNG)
   * parameter 수를 기준으로 large, small model을 각각 구현
   * 6개의 conv layer, 3개의 fc layer
   * 정규화를 위해 p=0.5 dropout 사용
4. Data Augmentation using Thesaurus
   * Augmentation: 확대, Thesaurus: 유의어 사전
   * appropriate data augmentation은 딥러닝에서 generalization 문제를 어느정도 해결해줌
   * 언어는 순서가 있기 때문에 image같이 signal을 변경하는 것은 불가
   * 문장의 구성을 바꾸는 등 rephrase하는 것은 불가능. 유의어를 바꿔주는 방식 채택
   * 얼마나 바꿀 것이고, 어떤 것을 바꿀 것인지는 0.5 확률의 geometric distribution 사용

## 4. Comparision Model
1. Traditional Methods
   * Bag-of-words and its TF-IDF
     * 50,000 most frequent words from the training subset
     * 빈도수와 TF-IDF값을 feature로 지정
   * Bag-of-n-grams and its TF-IDF
     * 500,000 most freqjent n-grams(up to 5-grams) from the training subset
   * Bag-of-means on word embedding
     * K0means clustering을 word2vec embedding space에 적용
     * 같은 cluster 안에 있는 데이터들이 embedding의 평균을 같이 사용
2. Deep Learning Methods
   * word-based CNN
     * 300 size의 word2vec embedding 사용
   * word-based LSTM
     * ![image](https://github.com/study-ai-data/Deep-Learning/blob/master/charcnn/charcnn_lstm.PNG)
     * 300 size의 word2vec embedding 사용
     * LSTM cell들의 output값들의 평균을 feature로 사용하여 multinomial logistic regression에 사용
     * vanilla architecture 사용
3. Choice of Alphabet
대소문자를 구별하는 경우에는 대부분 성능이 좋지 않음.<br>
같은 alphabet이라도 대소문자를 구분하여 다른 문자로 인식하기 때문에 regularization 문제가 발생한 것으로 추정됨

## 5. Large-scale Datasets
* ![image](https://github.com/study-ai-data/Deep-Learning/blob/master/charcnn/charcnn_result.PNG)  
* AG : AG’s news corpus
* Sogou : Sogou news corpus
* DBP : DBPedia ontology dataset
* Yelp.P : Yelp reviews
  * predicting a polarity label by considering stars 1~2 negative, 3~4 positive
* Yelp.F : Yelp reviews
  * predicting full number of stars the user has given
* Yah.A : Yahoo! Answers dataset
* Amz.F : Amazon reviews
  * full score prediction
* Amz.P : Amazon reviews
  * polarity prediction

## 6. Discussion
* ![image](https://github.com/study-ai-data/Deep-Learning/blob/master/charcnn/charcnn_discussion.PNG)  
* Character-level ConvNet도 효율적인 모델임
* n-grams TF-IDF는 dataset을 조금 늘릴 경우에 더 효과적임. dataset을 많이 늘릴 시 charCNN의 성능이 더 좋음
* **charCNN이 리뷰, 댓글 등 User-generated data(Yelp, Yah, Amz)에 더 강함**
  * character 단위로 분석하기 때문에 맞춤법이 틀린 문자에 더 robust함
  * **반면에 맞춤법이 정확한 data(AG, Sogus, DBP)에서는 n-gram TF-IDF가 성능이 좋음**
* dataset이 커졌을 때는, 대소문자를 구분한 것이 성능에 좋지 않음
  * regularization effect 문제로 추정  

## 7. Conclusion
character-level ConvNet is an effective method

## Reference
* paper: https://arxiv.org/abs/1509.01626
* code: https://github.com/yoonkim/lstm-char-cnn