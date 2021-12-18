 <a href="https://telegram.me/A2z_tech">
    <img src="https://di5qs4dv32t01.cloudfront.net/wp-content/uploads/2021/12/telegram-34.jpg" width="250">
  </a><br>

Press the below button to deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
<a href="https://youtu.be/2MFOUs2vKz8"><br>
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>
then goto the <a href="#mandatory-vars">variables tab</a> for more info on setting up environmental variables.



Required Vars

`API_ID` : Go to [my.telegram.org](https://my.telegram.org) to Get this.

`API_HASH` : Go to [my.telegram.org](https://my.telegram.org) to Get this.

`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)

`BIN_CHANNEL` : Create a new channel (private/public), post something in your channel. Forward that post to [@missrose_bot](https://telegram.dog/MissRose_bot) and **reply** `\id`. Now copy paste the forwarded channel ID in this field. 


Optional Vars

`SLEEP_THRESHOLD` : Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds.

`WORKERS` : Number of maximum concurrent workers for handling incoming updates. Defaults to `3`

`PORT` : The port that you want your webapp to be listened to. Defaults to `8080`

`WEB_SERVER_BIND_ADDRESS` : Your server bind adress. Defauls to `0.0.0.0`

`NO_PORT` : (can be either `True` or `False`) If you don't want your port to be displayed. You should point your `PORT` to `80` (http) or `443` (https) for the links to work. Ignore this if you're on Heroku.

`FQDN` :  A Fully Qualified Domain Name if present. Defaults to `WEB_SERVER_BIND_ADDRESS`

`HAS_SSL` : (can be either `True` or `False`) If you want the generated links in https format.
## How to use the bot

:warning: **Before using the  bot, don't forget to add the bot to the `BIN_CHANNEL` as an admin**
 
`/start` : To check if the bot is alive or not.

To get an instant stream link, just forward any media to the bot and boom, its fast af.

## faQ

- How long the links will remain valid or is there any expiration time for the links generated b the bot?
> The links will be valid as longs as your bot is alive and you haven't deleted the log channel.

## Contributing

Feel free to contribute to this project if you have any further ideas
