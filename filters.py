# from aiogram.dispatcher.filters import BoundFilter
# from aiogram import types
#
# class IsAdminFilter(BoundFilter):
# 	async def check(self, *args) -> bool:
# 		pass
#
# 	key = 'is_admin'
#
# 	def __init__(self, is_admin):
# 		self.is_admin = is_admin
#
# 	async def admin_rights(self, message: types.Message):
# 		member = await bot.get_chat_member(message.chat.id, message.from_user.id)
# 		return member.is_chat_admin()