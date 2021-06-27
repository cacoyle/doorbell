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
2) Under the *app submission api* dropdown, click `create a new security profile`
3) Enter your desired name and description, and click `save`
4) Click the *web settings* tab, and copy the `client id` and `client secret` values
##### Lambda Skeleton
1) Go to the [Lambda management page](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions)
2) Click the `create function` button
3) Select the `Author from scratch` card
4) Select your function name, and select the latest available python runtime (*`3.7` at this time*)
5) Click `create function` and copy your lambda function's ARN
6) Add a trigger to your function selecting 'Alexa Smart Home'
##### Alexa Skill
1) Go to the [Alexa Skill Developer page](https://developer.amazon.com/alexa/console/ask) and click 'create skill'
2) Copy your new skill's id
3) Copy your lambda function's ARN into the `default endpoint` field
4) If you have geographic region considerations, click the relevant checkboxes below
5) In the left hand sidebar, click `Account Linking`, and enter the following values

| Field  | Value |
| -------| ----- |
| Your Web Authorization URI  | https://www.amazon.com/ap/oa  |
| Access Token URI  | https://api.amazon.com/auth/o2/token  |
| Your Client ID | The client id value from the Security Profile [section](#Security-Profile) |
| Your Secret | The client secret value from the Security Profile [section](#Security-Profile) |
| Scope | profile:user_id |
| Default Access Token Expiration Time | 3600 or whatever you think is reasonable |
6) In the left hand sidebar, click `Permissions`
7) Enable the `Send Alexa Events` toggle
8) Copy the `Alexa Client Id` and `Alexa Client Secret` values
##### Update Lambda Function for Discovery and Authorization
1) Go to the [Lambda management page](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions)
2) Edit your function !*TODO make both ends read the dynamodb user table from ssm*
3) Paste the content of [lambda_function.py](/lambda/lambda_function.py) into the body of the new lambda
4) You can also create tests for [discovery](/lambda/test/discovery.json) and [authorization](/lambda/test/authorization.json)
##### DynamoDB Configuration
1) Go to the [dynamo configuration page](https://console.aws.amazon.com/dynamodb/home?region=us-east-1)
2) Click `Create Table`
3) Enter the table name and set partition key to user (think of this like a primary key)
4) Update the `DYNAMO_TABLE` value in the lambda function and `DYNAMO_TABLE` value in config.py to match the name of the dynamo table you've created
##### IAM Policies
1) Go to the [IAM policy configuration page](https://console.aws.amazon.com/iam/home#/policies)
2) Click 'Create Policy' button
3) In the new page, click the `JSON` tab and clear out the default contents
4) Paste the contents of [the dynamo iam policy](iam/policy.json), be sure to update the `Resource` ARN to match the region and name of the dynamo table you've created, click 'next'
5) Add any tags if desired, click next
5) Enter the desired name of the new iam policy, I used 'PIDoorBellDynamoAccess' for example
##### IAM Role for Lambda Execution
1) Go to the [IAM Role configuration page](https://console.aws.amazon.com/iam/home#/roles)
2) Click 'Create Role'
3) Select `AWS Service` from the 'trusted entity' tiles
4) Select 'Lambda' from the 'common use cases' section
5) In the next page under 'Attach permissions policies', select the `AWSLambdaBasicExecutionRole`, as well as the policy you created in the [previous step](IAM-Policies)
6) Click 'next' and add tags as desired
7) Click next, enter your desired role name, I used 'PIDoorBellRole' for example
8) Client 'create role'
##### IAM Role for Lambda Function
Go to the [Lambda configuration page](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions) and edit your function
2) Under the configuration tab, on the lefthand menu, select `Permissions`
3) In the 'Execution Role' section, click `Edit`
4) Under the 'Edit basic settings' page, select 'Use an Existing role', and select the role you created in the [previous step](IAM-Role-for-Lambda-Execution)
5) Click Save
##### Doorbell IAM User
1) Go to the [IAM User configuration page](https://console.aws.amazon.com/iam/home#/users)
2) Click 'Add User' button
3) Enter the desired username, and set the 'access type' to `Programmatic access`, click `next`
4) Click the 'Attach existing policies directly tile, select the name of the IAM policy you created in the [policies step](IAM-Roles-and-Policies) to enable dynamo access
6) Click next, review, and finish
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


