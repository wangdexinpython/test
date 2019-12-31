import chardet
ss="ea5ce87e176bdf15dca129e98b7c590c"
s1=str("1").encode()
detector = chardet.detect(s1)
print(detector)


