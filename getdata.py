import requests 

feature_id_dict = {
        "35": "adv", "31" : "adj", "30":"n", "29" : "excl", "38": "postp",
        "39": "conj", "34": "v", "33": "v", "32": "v", "36": "v", 
        "40": "pron", "42": "old", "43": "fig.", "44": "dialect",
        "45": "coll.", "41": "slang", "47": "s.w.", "89":"sports",
        "91": "nautical", "90": "botany", "97": "chem.", "13": "phy.", 
        "108": "phy.", "103": "lit.", "88": "music", "100": "law",
        "102": "zoology", "96": "psy.", "101": "math.", "124": "military",
        "113": "socio.", "94": "geog.", "98": "anat.", "110": "geol.",
        "307": "med.", "95": "grammar", "92": "hist.", "99": "trade"         
                  }

valency_dict = {"34": "intr.", "33": "acc.", "32": "dat.", "36": "inst."}

lang_dict = {"0": "tr", "19": "tr+", "12": "fa", "11": "ar", "13": "fr", "18": "en", "14": "it", "21": "hy", "393": "el"}


def get_data(search_word):
    URL = "https://sozluk.gov.tr/gts"    
    PARAMS = {'ara':search_word}     
    received_data = requests.get(url = URL, params = PARAMS)
    return received_data.json()
    
    
def get_language(data):
    return lang_dict.get(data["lisan_kodu"])
    
    
def get_senses(data):
    return data["anlam_say"]
        
        
def get_pos(data):
    try:
        feature_id = data["anlamlarListe"][0]["ozelliklerListe"][0]["ekno"]
        return feature_id_dict.get(feature_id)
    except:
        pass
    
    
def get_feature(data):
    try:
        feature_id = data["anlamlarListe"][0]["ozelliklerListe"][1]["ekno"]
        return feature_id_dict.get(feature_id)
    except:
        pass
    
    
def get_valency(data):
    try:
        feature_id = data["anlamlarListe"][0]["ozelliklerListe"][0]["ekno"]
        return valency_dict.get(feature_id)
    except:
        pass




            
