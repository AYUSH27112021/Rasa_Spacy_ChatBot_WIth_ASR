# Telugu ASR
Speech Recognition for Indian Languages

## Notes
This model is a fine-tuned version of `openai/whisper-small` on the Telugu data from multiple publicly available ASR corpora.

The Telugu model is trained on the + a private corpus recorded based on the shared files.

### To infer a single audio file using this model, the following code snippet can be used:
```
import torch
from transformers import pipeline
audio = "/path/to/audio.format" # path to the audio file to be transcribed
device = "cuda:0" if torch.cuda.is_available() else "cpu"

transcribe = pipeline(task="automatic-speech-recognition", model="/path/to/PyTorch/model/", chunk_length_s=30, device=device)
transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="te", task="transcribe")
print('Transcription: ', transcribe(audio)["text"])
```
## Training hyperparameters
The following hyperparameters were used during training:

```
learning_rate: 1e-05
train_batch_size: 24
eval_batch_size: 48
seed: 22
optimizer: adamw_bnb_8bit
lr_scheduler_type: linear
lr_scheduler_warmup_steps: 15000
training_steps: 10000 (can be increased)
mixed_precision_training: True
```
## Evaluation results
```
Wer = 22.8931
```
**NOTE->** Please note that a sample `data.csv` is provided and the custom dataset must be in the required format.