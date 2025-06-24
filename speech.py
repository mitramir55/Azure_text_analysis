from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
from azure.ai.projects.models import ConnectionType
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.ai.projects import AIProjectClient
import azure.cognitiveservices.speech as speech_sdk


def main():

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    try:
        global speech_config

        # Get config settings
        load_dotenv()
        project_key = os.getenv('PROJECT_KEY')
        location = os.getenv('LOCATION')

        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(project_key, location)
        print('Ready to use speech service in:', speech_config.region)

        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()

    except Exception as ex:
        print(ex)

def TranscribeCommand():
    command = ''

    # Configure speech recognition
    current_dir = os.getcwd()
    audioFile = current_dir + '/time.wav'
    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)


     # Process speech input
    print("Listening...")
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)


    # Return the command
    return command


def TellTime():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)


    # Configure speech synthesis
    output_file = "output.wav"
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    audio_config = speech_sdk.audio.AudioConfig(filename=output_file)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config, audio_config,)


     # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)
    else:
        print("Spoken output saved in " + output_file)


    # Print the response
    print(response_text)


if __name__ == "__main__":
    main()