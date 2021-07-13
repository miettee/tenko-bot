from tenko import tenko
import creds


bot = tenko("t^")
token = creds.token
bot.remove_command('help')

initial_extensions = (
    'cogs.topgg', 'cogs.vibecheck2', 'cogs.reacts', 'cogs.imagecmds', 'cogs.shu-text', 'cogs.shu-image', 'cogs.miscs'
)

if __name__ == '__main__':

    for extension in initial_extensions:
        bot.load_extension(extension)



bot.run(token)