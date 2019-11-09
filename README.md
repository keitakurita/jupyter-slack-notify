[![pypiv](https://img.shields.io/pypi/v/jupyter_slack.svg)](https://pypi.python.org/pypi/jupter_slack)
[![pyv](https://img.shields.io/pypi/pyversions/jupyter_slack.svg)](https://pypi.python.org/pypi/jupyter_slack)
[![License](https://img.shields.io/pypi/l/jupyter_slack.svg)](https://pypi.python.org/pypi/jupyter_slack)

# Jupyter Slack Notifier
Tired of constantly checking your jupyter notebook to see if your code has finished executing?  
Frustrated by checking your code after waiting hours, only to see your code failed in 5 minutes?  
Worry no more! This magic command will notify you via slack when your code finishes or fails!  

## Installation
`$ pip install jupyter_slack`

## Usage
Import in your notebook and use like this:
![usage](https://i.imgur.com/3bKBr8b.png)

You should receive messages in slack like this:
![outcome](https://i.imgur.com/sidwVIm.png)

You can also use the features within your code like this: 
```python
import jupyter_slack
jupyter_slack.notify_self("hello world")
```

Or, if you want notifications when execution fails and/or know how long your command takes,
you can use the following context manager: 
```python
import jupyter_slack
with jupyter_slack.Monitor("hello world", time=True):
    do_something()
```

## Instructions

### Slack Apps
1. Create an [incoming webhook](https://api.slack.com/messaging/webhooks)

2. Set the following environmental variable: 
```bash
export SLACK_WEBHOOK_URL=your_webhook_url
```


### Legacy Tokens (Will eventually be deprecated so not recommended)
1. Acquire a [Slack api token](https://api.slack.com/docs/oauth-test-tokens)

2. Set the following variables in your .bashrc (or whatever profile you are using):  
```bash
$ export SLACK_TOKEN=slack_token  
$ export SLACK_ID=username  
```
