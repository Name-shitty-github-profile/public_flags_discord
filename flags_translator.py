def translate(flag: int):
  flags = {
    131072: 'VERIFIED_DEVELOPER',
    65536: 'VERIFIED_BOT',
    16384: 'BUG_HUNTER_LEVEL_2',
    4096: 'SYSTEM',
    1024: 'TEAM_USER',
    512: 'PREMIUM_EARLY_SUPPORTER',
    256: 'HYPESQUAD_ONLINE_HOUSE_3',
    128: 'HYPESQUAD_ONLINE_HOUSE_2',
    64: 'HYPESQUAD_ONLINE_HOUSE_1',
    8: 'BUG_HUNTER_LEVEL_1',
    4: 'HYPESQUAD',
    2: 'PARTNER',
    1: 'STAFF'
  }
 userflags = []

  while flag != 0:
    for item in flags.keys():
        if flag >= item:
            userflags.append(flags[item])
            flag = flag - item
  return userflags
