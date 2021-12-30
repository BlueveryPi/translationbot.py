from googletrans import Translator
import iso639

translator = Translator()
no=["?"]

def trans(txt, native="ko"):
    transed=translator.translate(txt, dest=native)
    detected=translator.detect(txt)
    detected=detected.lang
    if (txt not in no) and transed.text.lower()!=txt.lower() and transed.text.lower()!=(txt+".").lower():
        if detected in ["en", native]:
            return transed.text
        else:
            return transed.text+f"({iso639.to_name(detected)})"

    else:
        return False

def check(txt, native):
    return (translator.detect(txt)).lang==native