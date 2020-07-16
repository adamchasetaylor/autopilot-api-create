import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Create New Autopilot Bot, unique_name MUST be unique
assistant = client.autopilot \
  .assistants \
  .create(
    friendly_name='Tell Me A Joke', 
    unique_name='joke-assistant'
  )

print(assistant.sid)

# Return Tasks (default [] empty)
tasks = client.autopilot \
  .assistants(assistant.sid) \
  .tasks \
  .list(limit=20)

for record in tasks:
  print(record.sid)

# Add a Task

my_actions = {
'actions': [
    {
        'say': {
            'speech': 'I was going to look for my missing watch, but I could never find the time.'
        }
    }
]
}

task = client.autopilot.assistants(assistant.sid) \
  .tasks \
  .create(friendly_name='tell-a-joke', actions=my_actions, unique_name='tell-a-joke')

print(task.sid)

# Create Sample

sample = client.autopilot \
  .assistants(assistant.sid) \
  .tasks(task.sid) \
  .samples \
  .create(language='en-US', tagged_text='joke')

print(sample.sid)

# Create ModelBuild

model_build = client.autopilot \
  .assistants(assistant.sid) \
  .model_builds \
  .create()

print(model_build.sid)

# Delete the Bot
# client.autopilot.assistants(assistant.sid).delete()