# DIY IoT Alexa Doorbell with Raspberry Pi

### Why?
This came up as a reason to play with alexa smarthome device integrations, and our cats freak out anytime the doorbell rings or we have strangers over, it's very stressful for them and I wanted a less audio-specific notification for people at the door.

In addition, there's no room on either side of the front door to properly mount the V1 Ring I got used on woot, so I attached it directly to the front door.  I didn't know until later that it's recording function is based on IR and not pixel change in the video stream, so it's pretty much useless to me.  And I didn't want law enforcement potentially having unrestricted access to a camera mounted to the front of my house.  Finally, no one seems to be interested in opening the storm door to press a button vs the legacy doorbell on the trim.
***
### Requirements
* Raspberry Pi
* Wire, connectors, solder, crimpers, etc
* Analog doorbell
* Amazon Web Services Account
* Amazon Developer Account
* Existing doorbell, access to wiring, and enough knowledge to not electrocute yourself.  Existing doorbells may have a stepdown transformer as part of their installation and should be treated with caution
* Acknowledging that I am not an expert and i have no idea what I'm doing at any time whatsoever

***
### Manual Setup
###### *NOTE: The below URLs are static to the us-east-1 region, adjust accordingly for your environment*
##### Security Profile
1) Go to the [Developer Console API Access page](https://developer.amazon.com/apps-and-games/console/api-access/home.html) 
2) Under the 'app submission api' dropdown, click 'create a new security profile'
3) Enter your desired name and description, and click 'save'
4) Click the 'web settings' tab, and copy the client id and client secret values
##### Lambda Function for Discovery and Authorization
1) Go to the [Lambda management page](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions)
2) Click the 'create function' button
3) Select the 'Author from scratch' card
4) Select your function name, and select the latest available python runtime (*3.7 at this time*)
5) Click 'create function' and copy your lambda function's ARN
##### Alexa Skill
1) Go to the [Alexa Skill Developer page](https://developer.amazon.com/alexa/console/ask) and click 'create skill'
2) Copy your new skill's id
3) Copy your lambda function's ARN into the 'default endpoint' field
4) If you have geographic region considerations, click the relevant checkboxes below
5) In the left hand sidebar, click 'Account Linking', and enter the following values
| Field  | Value |
| -------| ----- |
| Your Web Authorization URI  | https://www.amazon.com/ap/oa  |
| Access Token URI  | https://api.amazon.com/auth/o2/token  |

***
### Pulumi Setup
1)
***
### Integrations

##### Hue

##### RTSP
***
### Custom Integrations
##### TODO


