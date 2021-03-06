# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 23:03:06 2020

@author: 13034
"""


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics',
                             hobbies='table tennis')
print(user_profile)

# the practice of 8-14 is similar to this one.