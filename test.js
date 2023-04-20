const bot = BotManager.getCurrentBot();

bot.addListener(Event.MESSAGE, msg => {
    msg.isDualApp = msg.systemUserId == 95;

    if (msg.room.name == '류현승' && msg.isDualApp) {
        msg.reply(`isMention: ${msg.isMention}, hasMention: ${msg.hasMention}`);
    }
});