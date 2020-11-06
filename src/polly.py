from boto3 import Session
from conf import conf

# Create a polly session
success = False
for i in range(0, 3):
    polly = Session(**conf.session).client("polly")
    success = True
    break
if not success:
    raise

# Test client
polly.synthesize_speech(Text='', **conf.synth)

def synth(text):
    ''' Synth text to a binary audio stream
    '''
    result = polly.synthesize_speech(Text=text, **conf.synth)
    stream = result["AudioStream"].read()
    return stream