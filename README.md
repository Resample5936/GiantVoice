# GiantVoice
Python script that sends messages to multiple Slack channels at the same time

#Setup
This script relies on Slack webhooks (specially coded URLs) to send one message to many channels. There are a couple steps necessary to generate these URLs:
<ol>
  <li>Register an app in your workspace at (https://api.slack.com/apps)</li>
  <li>In your app settings, turn on webhooks via the left-hand menu. </li>
  <li>Generate a webhook URL for each channel you'd like Giant Voice to post in.</li>
  <li>Copy the URLs to the JSON file, using the example format. Please be aware that these URLs should be treated like secrets. Anyone with access to the URL can post to your Slack workspace.</li>
</ol>
It may be necessary to install the requests function into your Python installation.<br> 
    pip install requests
Finally, modify line 13 of the GiantVoice.py file to point to the JSON file location.

#Use
When the program is run, it will prompt the user for a message. Simply type something and hit enter! 
