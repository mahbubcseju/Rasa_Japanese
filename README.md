# Rasa_Japanese
Rasa is an open source machine learning framework to automate text-and voice-based conversations.Rasa's primary purpose is to help you build contextual, layered conversations with lots of back-and-forth. To have a real conversation, you need to have some memory and build on things that were said earlier. Rasa lets you do that in a scalable way.

## How to use rasa for japanese language?

### Installation
- Firstly install rasa in your own environment as following: 
```
git clone https://github.com/RasaHQ/rasa.git
cd rasa
```
- As we will add a custom component to tokenize japanese text , we will use mecab library for tokinzing the text.  
 add mecab-python3  at the end of requirements.txt file. Or install mecab using pip.
```
pip install mecab-python3
```
- Now install all the requirements using : 
```
pip install -r requirements.txt
pip install -e .
```
### Create Project
- First run the following command:
  ```
   rasa init --no-prompt
   
   ```
- Then add the Japanese language tokenizer in the path "rasa/rasa/nlu/japanese_tokenizer.py".
I have added the file in "rasa/rasa/nlu/japanese_tokenizer.py" path.
- Add JapaneseTokenizer component class in /rasa/rasa/nlu/registry.py.
   E.g:
   ```
   from rasa.nlu.tokenizers.japanese_tokenizer import JapaneseTokenizer
   
   ```
   Add class name inside component_classes = [] dictionary.
   E.g
     ```
   component_classes = [
    # tokenizers
    JapaneseTokenizer,
    MitieTokenizer,
    SpacyTokenizer,
    WhitespaceTokenizer,
    JiebaTokenizer,
    ]
  ```
- Now add JapaneseTokenizer as pipeline in config.yml as follows:
   ```
    # Configuration for Rasa NLU.
    # https://rasa.com/docs/rasa/nlu/components/
    language: jp
    pipeline:
      - name: "JapaneseTokenizer"
      - name: "RegexFeaturizer"
      - name: "CRFEntityExtractor"
      - name: "EntitySynonymMapper"
      - name: "CountVectorsFeaturizer"
      - name: "EmbeddingIntentClassifier"
    # Configuration for Rasa Core.
    # https://rasa.com/docs/rasa/core/policies/
    policies:
      - name: MemoizationPolicy
      - name: KerasPolicy
      - name: MappingPolicy

   ```
- Now Add data as data/nlu.md, stories.md and domail.yml.
  E.g: 
  
  nle.md:
    ```
    ## intent:greet
    - ハロー
    - もしもし
    - 初めまして
    - こんにちは
    - はじめまして
    
    ## intent:icebreak12
    - よろしくお願いします
    - こちらこそ
    - 宜しくお願いします
    - 問題ないです
   ```
   stories.md:
   ```
    ## happy path
    * greet
      - utter_greet
    * icebreak12
      - utter_icebreak12
   ```
   domain.yml:
    ```
    intents:
    - utter_icebreak12
    - greet
    templates:
      utter_icebreak12:
      - text: 今どこで、何をしていますか？
      utter_greet:
      - text: ご協力いただきありがとうございます。本日は宜しくお願いします
    actions:
    - utter_greet
    - utter_icebreak12
    ```

- Now train your model using:
    ```
      rasa train
    ```
- To chat run:
    ```
      rasa shell
    ```
