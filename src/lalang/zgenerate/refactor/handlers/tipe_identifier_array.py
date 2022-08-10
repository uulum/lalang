from app.transpiler.zgenerate.refactor.handlers.common import peta_tipe_data
from app.treeutils import (anak, beranak, chdata, child, child1, child2,
                           child3, child4, chtoken, data, ispohon, istoken,
                           jumlahanak, sebanyak, token)


def tipe_identifier_array(tree, language="py"):
    kembali = ""

    kembalian = "__JENIS[]"
    if beranak(tree):
        prim = child1(tree)  # item_type
        primi = child1(prim)  # integer
        primitive = data(primi)
        petakan = peta_tipe_data[language].get(primitive, primitive)
        kembalian = kembalian.replace("__JENIS", petakan)
        return kembalian
    kembalian = kembalian.replace("__JENIS", "")
    if language == "py":
        pass
    elif language == "ts":
        pass
    elif language == "rs":
        pass
    elif language == "java":
        pass
    elif language == "kt":
        pass
    elif language == "go":
        pass
    elif language == "rb":
        pass
    elif language == "v":
        pass
    elif language == "dart":
        pass
    elif language == "cpp":
        pass
    elif language == "cs":
        pass
    elif language == "hs":
        pass
    elif language == "clj":
        pass
    elif language == "scala":
        pass
    elif language == "php":
        pass
    elif language == "swift":
        pass
    elif language == "elixir":
        pass
    elif language == "erlang":
        pass
    return kembali
