import whisper

# Valid model_names are :
# tiny, base, small, medium, large, large-v2, or large-v3

class Whisper_Transcriber():

    model = None

    def init(self, model_name = "large-v3"):
        print(f"Loading Open AI Whisper model {model_name}")
        self.model = whisper.load_model(model_name)
        print("  complete")

    def transcribe(self, audio_file_name):
        if self.model == None:
           self.init()

        result = self.model.transcribe(audio_file_name)
        return result['text']