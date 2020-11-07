from boto3 import Session
from conf import conf


def polly_session():
    """Create an amazon polly session"""
    success = False
    for i in range(0, 3):
        session = Session(**conf.session).client("polly")
        success = True
        break
    if not success:
        raise
    _synth = lambda x: session.synthesize_speech(Text=x, **conf.synth)[
        "AudioStream"
    ].read()
    return _synth


def synth(text, service_factory=polly_session):
    """Synth text to a binary audio stream"""
    speech_service = service_factory()
    stream = speech_service(text)
    return stream