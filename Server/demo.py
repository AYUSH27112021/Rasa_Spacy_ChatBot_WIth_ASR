import nemo.collections.asr as nemo_asr

asr_model = nemo_asr.models.EncDecCTCModel.restore_from('/home/siva/Downloads/Model-te.nemo', strict=False)
path = '/home/siva/Desktop/rasaprojects/TE_final/abc/server/uploads//blob'

files = [path]
transcript = asr_model.transcribe(paths2audio_files=files)[0]
print(f'Transcript: "{transcript}"')