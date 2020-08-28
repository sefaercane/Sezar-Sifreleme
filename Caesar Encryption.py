def sezar(yazi,birim):
    yaziBüyük = yazi.upper()
    sifreliYazi2 = []
    sifreliYazi = []
    alfabe = ["A", "B", "C","Ç","D", "E", "F", "G","Ğ", "H", "I","İ", "J", "K", "L", "M", "N", "O","Ö", "P","R", "S","Ş", "T","U","Ü" ,"V", "Y", "Z"]

    for i in yaziBüyük:
        harfSira  = alfabe.index(i)
        sifreliHarf = (harfSira + birim) % 29
        sifreliYazi.append(sifreliHarf)
        cikti = alfabe[sifreliHarf]
        sifreliYazi2.append(cikti)

    yazihali = ""
    for i in sifreliYazi2:
        yazihali = yazihali + i
    return yazihali.lower()
