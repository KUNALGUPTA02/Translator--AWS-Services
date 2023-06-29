import tkinter as tk
import boto3
from tkinter import StringVar
from tkinter import *
import requests
import json
root=tk.Tk()

root. geometry("400x500")
root.title("AWS Translator") 
textExample=tk.Text(root, height=10)
textExample.pack()
result_text = StringVar()
lang_sel = StringVar()
result_text.set("Translated Text will be displayed here!!")
languages = {"Hindi":'hi',"Gujarati":'gu'}
lang_sel.set('Language')
w = OptionMenu(root, lang_sel, *languages.keys())
w.pack()

def getText ():
    global to_lang,languages
    result=textExample.get ("1.0", "end")
    url = "http://translatorcc-env.eba-g3bwpihb.us-east-1.elasticbeanstalk.com/getTranslation"
    payload = {"text":result,"from_lang":"en","to_lang":languages[lang_sel.get()]}
    payload = json.dumps(payload)
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url=url,data=payload,headers=headers)
    data = resp.json()
    # print(resp.status_code)
    # print("Translated Text : "+response.get('TranslatedText'))
    # print("Source Language Code: "+response.get('SourceLanguageCode'))
    # print("Target Language Code: "+response.get('TargetLanguageCode'))
    result_text.set(data["translated_text"])
    
btnRead=tk.Button(root, height=1, width=10, text='Read', command=getText)
btnRead.pack() 
transl = tk.Label(root,textvariable=result_text)
transl.pack()
root.mainloop()
