def count_letter_occurrences(text):
    text = text.lower()
    letter_counts = {}

    for char in text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts


# Example usage
text = ("MWFIN AKHLN RVMWF UNKPF RMFKI NAGFV TRNBX AFTKL TNRVM WFRMW"
        "FEKFL MFVTR NKTUG UTRSF RXFRM AEATI NRVNA AMWFA XMMAF TELMF"
        "KLLMT TVNRV INXMF VXRNK TIMWF MXBFW NLUTB FMWFI NAKHL LNXVM"
        "TMNAG TOBNR EMWXR ZLTOL WTFLN RVLWX PLNRV LFNAX RZINC TOUNY"
        "YNZFL NRVGX RZLNR VIWEM WFLFN XLYTX AXRZW TMNRV IWFMW FKPXZ LWNSF IXRZL")
letter_counts = count_letter_occurrences(text)
sorted_letter_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

for letter, count in sorted_letter_counts:
    print(f"'{letter}': {count}")
