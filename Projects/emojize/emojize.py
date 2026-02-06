import emoji
# import requests
# import json

user_input = input('Input: ')

output = emoji.emojize(user_input, language='alias')

print('Output: ', output)

# response = requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")
#
# # print(emoji.EMOJI_DATA(user_input))
#
# print(json.dumps(response.json()))

