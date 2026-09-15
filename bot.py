from os import getenv
import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()
TOKEN=getenv("BOT_TOKEN")

main_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="schedule")]

          
    ],
   resize_keyboard=True   

)

schedule_keybord = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="monday", callback_data="monday")],
        [InlineKeyboardButton(text="tuesday", callback_data="tuesday")],
        [InlineKeyboardButton(text="wednesday", callback_data="wednesday")],
        [InlineKeyboardButton(text="thursday", callback_data="thursday")],
        [InlineKeyboardButton(text="friday", callback_data="friday")]

    ]


)
back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="back",
                callback_data="back_to_days"
            )
        ]
    ]
)

back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="back", callback_data="back_to_days")]
    ]
)

dp = Dispatcher()
router = Router()
dp.include_router(router)


#обработчик
@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Just pick this fucking thing already.",
         reply_markup=main_keybord
    )

@router.message(F.text == "schedule")
async def show_schedule(message: Message):
      await message.answer(
            "Choose a day of the week.",
        reply_markup=schedule_keybord
      )


@router.callback_query(F.data == "monday")
async def monday(callback: CallbackQuery):
    await callback.message.edit_text(
        "monday\n\n"
        "1 СС и ТДВ\n"
        "Кабинет: 410\n"
        "Индык А.И.\n"
        "Недели: 1–17\n\n"

        "2 МДК.01.03\n"
        "Кабинет: 202л\n"
        "Артемов С.В.\n"
        "Недели: 1–15\n\n"

        "3 МДК.01.01\n"
        "Кабинет: 307л\n"
        "Николаенко И.Д.\n"
        "Недели: 1–15\n\n"

        "4 МДК.01.02\n"
        "Кабинет: 315л\n"
        "Николаенко К.С.\n"
        "Недели: 2, 6, 10, 12\n\n"

        "4 МДК.01.01\n"
        "Кабинет: 307л"
        "Николаенко И.Д.\n"
        "Недели: 13,14\n\n",

        reply_markup=back_keyboard
    )
    await callback.anwer()

#обработчик назад
@router.callback_query(F.data == "back_to_days")
async def back_to_days(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose a day of the week.",
        reply_markup=schedule_keybord
    )

    await callback.answer()

# 2 день...

@router.callback_query(F.data == "tuesday")
async def tuesday(callback: CallbackQuery):
    await callback.message.edit_text(
        "tuesday\n\n"
        "1 МДК.01.01.\n"
        "Кабинет: 307л\n"
        "Николаенко И.Д.\n"
        "Недели: 1-16\n\n"

        "2 МДК.01.02\n"
        "Кабинет: 315л\n"
        "Николаенко К.С\n"
        "Недели: 1-16\n\n"

        "3 ОПБД\n"
        "Кабинет: 203л\n"
        "Буценко Е.В.\n"
        "Недели: 1-15\n\n"

        "4 ОПБД\n"
        "Кабинет: 203л\n"
        "Буценко Е.В.\n"
        "Недели: 12,13\n\n"

        "4 МДК.01.04\n"
        "Кабинет: 202л\n"
        "Артемов С.В.\n"
        "Недели: 15\n\n",

        reply_markup=back_keyboard
    )
    await callback.anwer()

    #обработчик назад
@router.callback_query(F.data == "back_to_days")
async def back_to_days(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose a day of the week.",
        reply_markup=schedule_keybord
    )

    await callback.answer()

# 3 день

@router.callback_query(F.data == "wednesday")
async def wednesday(callback: CallbackQuery):
        await callback.message.edit_text(
        "wednesday\n\n"
        "1 МДК.01.02\n"
        "Кабинет: 315л\n"
        "Николаенко К.С.\n"
        "Недели: 1-12,14,15\n\n"

        "2 МДК.01.01\n"
        "Кабинет: 307л\n"
        "Николаенко И.Д.\n"
        "Недели: 1-15\n\n"

        "3 ОПБД\n"
        "Кабинет: 203л\n"
        "Буценко Е.В.\n"
        "Недели: 1-15\n\n"

        "4 МДК.01.04.\n"
        "Кабинет: 202л\n"
        "Артемов С.В.\n"
        "Недели: 1,3,5,7,9,11\n\n"

        "4 МДК.01.03\n"
        "Кабинет: 202л\n"
        "Артемов С.В.\n"
        "Недели: 2,4,6,8,10,14,15\n\n",

        reply_markup=back_keyboard
    )
        await callback.anwer()

@router.callback_query(F.data == "back_to_days")
async def back_to_days(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose a day of the week.",
        reply_markup=schedule_keybord
    )

    await callback.answer()

        
@router.callback_query(F.data == "thursday")
async def thursday(callback: CallbackQuery):
        await callback.message.edit_text(
        "thursday\n\n"
        "1 МДК.01.01\n"
        "Кабинет: 307л\n"
        "Николаенко И.Д.\n"
        "Недели: 1-15\n\n"

        "2 МДК.01.02\n"
        "Кабинет: 315л\n"
        "Николаенко К.С.\n"
        "Недели: 1-12,14,15\n\n"

        "3 ОПБД\n"
        "Кабинет: 203л\n"
        "Буценко Е.В.\n"
        "Недели: 1-15\n\n"

        "4 Физ.Культура\n"
        "Кабинет: Хуйло старое\n"
        "Волков В.В\n"
        "Недели: 11,13\n\n"

        "4 СС и ТДВ\n"
        "Кабинет: 410\n"
        "Индык А.И.\n"
        "Недели: 11,13\n\n",

        reply_markup=back_keyboard
        
    )
        await callback.anwer()

@router.callback_query(F.data == "back_to_days")
async def back_to_days(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose a day of the week.",
        reply_markup=schedule_keybord
    )

    await callback.answer()


@router.callback_query(F.data == "friday")
async def friday(callback: CallbackQuery):
        await callback.message.edit_text(
        "friday\n\n"
        "1 Ин.Язык\n"
        "Кабинет:409,314 \n"
        "Степаненко О.А.\n"
        "Кривцова С.Н.\n"
        "Недели: 1,3-5,7-9,11-17\n\n"

        "2 МДК.01.02\n"
        "Кабинет: 315л\n"
        "Николаенко К.С.\n"
        "Недели: 1-12\n\n"

        "2 МДК 01.01\n"
        "Кабинет: 307л\n"
        "Николаенко И.Д.\n"
        "Недели: 13,14\n\n"

        "2 Физ.Культура\n"
        "Кабинет:\n"
        "Волков В.В.\n"
        "Недели: 15-17\n\n"

        "3 МДК 01.04\n"
        "Кабинет: 202л\n"
        "Артемов С.В.\n"
        "Недели: 1-15\n\n"

        "4 СС и ТДВ\n"
        "Кабинет: 410\n"
        "Индык А.И.\n"
        "Недели: 2-11,13-15\n\n",

        reply_markup=back_keyboard
    )
        await callback.anwer()

@router.callback_query(F.data == "back_to_days")
async def back_to_days(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose a day of the week.",
        reply_markup=schedule_keybord
    )

    await callback.answer()
    
async def main():
    bot= Bot(token=TOKEN)

    print("Start..")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())