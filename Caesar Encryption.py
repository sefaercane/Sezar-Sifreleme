def sezar(yazi,birim):
    yaziBüyük = yazi.upper()
    sifreliYazi = []
    alfabe = ["A", "B", "C","Ç","D", "E", "F", "G","Ğ", "H", "I","İ", "J", "K", "L", "M", "N", "O","Ö", "P","R", "S","Ş", "T","U","Ü" ,"V", "Y", "Z"]

    for i in yaziBüyük:
        harfSira  = alfabe.index(i)
        sifreliHarf = (harfSira + birim) % 29
        cikti = alfabe[sifreliHarf]
        sifreliYazi.append(cikti)

    yazihali = ""
    for i in sifreliYazi:
        yazihali = yazihali + i
    return yazihali.lower()
