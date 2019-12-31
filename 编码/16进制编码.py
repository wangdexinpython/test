import time

ss = r'''li class\x3d\x22TrT0Xe\x22\x3e5 Bill Clinton. Age: 68. Founder, The Clinton Foundation. ... \x3c/li\x3e\x3cli class\x3d\x22TrT0Xe\x22\x3e6 Aung San Suu Kyi. Age: 68.'''

# articals = artical_pat.findall(response_text) and artical_pat.findall(response_text)[0] or ""
# articals_html = re.sub(r"<[^>]*>", '', articals.encode('utf8').decode("unicode-escape"))
# artical = re.sub(r"&.*?;", "", articals_html).encode('raw_unicode_escape').decode('utf8').replace('.slice(6, -6)', '')


res = ss.encode('utf-8').decode("unicode-escape")
print(res)

