from slackbot.bot import Bot
import led

def main():
    bot = Bot()
    led.run()
    bot.run()

if __name__ == "__main__":
    print "Starting...."
    main()