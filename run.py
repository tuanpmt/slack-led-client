from slackbot.bot import Bot
from led import LedService

def main():
    bot = Bot()
    led = LedService()
    led.run()
    bot.run()

if __name__ == "__main__":
    print "Starting...."
    main()