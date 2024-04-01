# RASA-Spacy Chatbot With ASR
## TELUGU RASA
### Installation of Telugu Spacy model
```
conda create --name <env_name> python=3.10.4 
conda activate <env_name>
pip install Spacy
```
**_NOTE:_**  Follow the 'README' inside the Spacy pipeline. To install it once the virtual environment is created.

## Install Rasa
```
pip install rasa
rasa init
```
Once the rasa module is installed replace the files inside the Rasa folder with the current files
## Train and Test the Rasa bot
```
rasa train
rasa shell
```
**_NOTE:_**  To test the spacy nlu separately in Rasa
```
rasa shell nlu
```
