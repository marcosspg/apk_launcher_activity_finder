from ast import parse
from tkinter import filedialog
from lxml import etree as et;

filetypes = [('Archivos XML', '*.xml')];
androidNamespace = {"android":"http://schemas.android.com/apk/res/android"}

openedFile = filedialog.askopenfile(filetypes=filetypes, title="Open AndroidManifest.xml", defaultextension=filetypes);
manifestPath = openedFile.name;
openedFile.close();
try:

    with open(manifestPath, encoding="utf-8") as manifestFile:
        parser = et.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
        manifestRoot = et.fromstring(manifestFile.read().encode("utf-8"), parser=parser);
        manifestFile.close();
        for activity in manifestRoot.xpath("//activity"):
            if activity.xpath("intent-filter") != None:
                if activity.xpath("intent-filter/action/@android:name", namespaces=androidNamespace)[0] == "android.intent.action.MAIN":
                    #Has android.intent.action.MAIN
                    if activity.xpath("intent-filter/category/@android:name", namespaces = androidNamespace)[0] == "android.intent.category.LAUNCHER":
                        print("Launcher activity: "+activity.xpath("@android:name", namespaces=androidNamespace)[0]);
                        break;
except Exception as e:
    
    print("################################## ¡Error! ##################################");
    print("An error has occurred. Try again or report this stacktrace here https://github.com/marcosspg/apk_launcher_activity_finder/issues");
    print("-----------------------------------------------");
    print();
    print();
    print(repr(e));
    print();