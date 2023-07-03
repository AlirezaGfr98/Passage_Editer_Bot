from typing import Final

import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


print('Starting up bot...')


TOKEN: Final = 'YOUR_BOT_TOKEN'
BOT_USERNAME: Final = 'YOUR_BOT_ID'


async def Guide(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text('✅ راهنمای استفاده از ربات: '+'\n'+
'📝 جهت تعویض یک کلمه با کلمه دیگر :'+'\n'+
'🔰برای تعیین واژه اولیه از دستور زیر استفاده کنید :'+'\n'+'@ow word'+'\n'+
'🔰برای تعیین واژه جایگزین از دستور زیر استفاده کنید :'+'\n'+'@nw word'+'\n'+'🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰'+ '\n' +
'🔰برای افزودن کلمه به متن مورد نظر از دستور زیر استفاده کنید :'+'\n'+'@dd word'+'\n'+
'🚫برای توقف دستور افزودن این دستور را وارد کنید.'+'\n'+'@dd ###'+ '\n' +'🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰'+'\n' +
'🔰 برای  حذف یک کلمه از متن مورد نظر از دستور زیر استفاده کنید :'+'\n'+'@rm word'+'\n'+
'🚫برای توقف دستور حذف این دستور را وارد کنید.'+'\n'+'@rm ###'+ '\n' +
'❌ در دستورات بالا ☝️ بجای word ، کلمه مورد نظر خود را وارد کنید'+ '\n' +'🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰🟰'+ '\n' +
'🔰جهت ارسال مستقیم محتوای ادیت شده به کانال مورد نظر باید ربات در کانال ادد شده و ادمین شود، '+'\n'+
'▪️همچنین باید دستور زیر را برای ربات وارد کنید.'+'\n'+'@fc @id'+'\n'+
'❌در دستور بالا بجای @id باید آیدی کانال را وارد کنید .'+'\n'+
'🚫اگر مجددا میخواهید پیام ویرایش شده ربات به شما فرستاده شود این دستور را وارد کنید:'+'\n'+'@fc 11111')




async def change_replacing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text

    if text[0].split() == ['@']:
        if text[1].split() == ['o']:
            if text[2].split() == ['w']:
                if text[3].split() == []:
                    old = text[:0] + text[4:]
                    primery = "primeryword.txt"
                    f = open("primeryword.txt", "w")
                    f.write(old)

                    await update.message.reply_text(" واژه اولیه به " + old + "تغيير کرد.")
    if text[0].split() == ['@']:
        if text[1].split() == ['n']:
            if text[2].split() == ['w']:
                if text[3].split() == []:
                    new = text[:0] + text[4:]
                    g = open("alternativeword.txt", "w")
                    g.write(new)

                    await update.message.reply_text(" واژه جايگزين به " + new + " تغيير کرد. ")
    f = open("primeryword.txt", "r")
    old = f.readline()

    g = open("alternativeword.txt", "r")
    new = g.readline()


    if text[0].split() == ['@']:
        if text[1].split() == ['f']:
            if text[2].split() == ['c']:
                if text[3].split() == []:
                    username = text[:0] + text[4:]
                    #id = "thisIDsend.text"
                    h = open("thisIDsend.txt",'w')
                    h.write(username)

                    await update.message.reply_text(" محتواي ويرايش شده به کانال " + username +'  ' + "ارسال خواهد شد.")
    h = open("thisIDsend.txt","r")
    username = h.readline()


    if text[0].split() == ['@']:
        if text[1].split() == ['d']:
            if text[2].split() == ['d']:
                if text[3].split() == []:
                    addition = text[:0] + text[4:]
                    k = open("additionword.txt",'w')
                    k.write(addition)

                    await update.message.reply_text(" به متن ارسال شده  " + addition +'  ' + " اضافه خواهد شد .")

    if text[0].split() == ['@']:
        if text[1].split() == ['r']:
            if text[2].split() == ['m']:
                if text[3].split() == []:
                    delete = text[:0] + text[4:]
                    d = open("deleteword.txt",'w')
                    d.write(delete)

                    await update.message.reply_text(" از متن ارسال شده واژه  " + delete +'  ' + " .حذف خواهد شد ")

    else:

        k = open("additionword.txt","r")
        addition = k.readline()
        additions = k.readlines()

        d = open("deleteword.txt","r")
        delete = d.readline()

        if username == '11111' :
            #دستورات ويرايش متن در اين قسمت
            text=text.replace(old ,new)
            if addition != '###':
                for i in additions :
                    text = text + i
            if delete != '###':
                text = text.replace(delete ,' ')
            #text = text + '\n' + '\n' + '#FollowerOfAli'
            await update.message.reply_text(text)

        else:
            #دستورات ويرايش متن در اين قسمت
            text=text.replace(old ,new )
            if addition != '###':
                for i in additions :
                    text = text + i
            if delete != '###':
                text = text.replace(delete ,' ')
            #دريافت پيام در پي وي و ويرايش و ارسال مستقيم به کانال
            await telegram.Bot(TOKEN).sendMessage(username , text)
    f.close()
    g.close()
    h.close()
    k.close()
    d.close()
    #for chek bot activity and hosting ....
    user_name = update.effective_user.username
    await telegram.Bot(TOKEN).sendMessage('A CHANNEL ID' , user_name )


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('help', Guide))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, change_replacing))

    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=1)
