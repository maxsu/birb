#!/bin/bash

# 

AWS_CONFIG_FILE='$HOME/.local/'


VOICE="$1"

if [ -z $1 ]
then 
  VOICE='Joanna'
fi


DATE=$(date -I)
UUID=$(uuidgen)
BASE="$HOME/.aws/polly/cache"
FILE="$BASE/$UUID"


say() {
  # Read stdin
  TEXT=$(cat)
  # Log the text and copy to user
  echo "$TEXT" | tee $FILE.txt
  echo
  echo "mp3: file://$FILE.mp3"
  echo "txt: file://$FILE.txt"

  # Synthetize text and store locally
  aws polly synthesize-speech \
    --output-format mp3       \
    --voice-id "$VOICE"       \
    --text "$TEXT"            \
    $FILE.mp3
  # Play stored file
  play $FILE.mp3
}

# Execute 'say' if stdin exists
if [ -p /dev/stdin ]; then
  say
else
  # Otherwise pipe the command arguments to stdin
  echo "$*" | say
fi
