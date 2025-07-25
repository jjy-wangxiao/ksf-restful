import re

def clean_string(s: str = "") -> str:
    """
    清洗字符串：去除首尾空白、全角转半角、中文标点转英文标点，统一换行和制表符为空格。
    """
    def fullwidth_to_halfwidth(ustring):
        """全角转半角"""
        rstring = ""
        for uchar in ustring:
            inside_code = ord(uchar)
            # 全角空格直接转为半角空格
            if inside_code == 0x3000:
                inside_code = 0x0020
            # 全角字符（除空格）根据关系转化
            elif 0xFF01 <= inside_code <= 0xFF5E:
                inside_code -= 0xFEE0
            rstring += chr(inside_code)
        return rstring

    # 中文标点与英文标点映射
    cn_punc = "，。！？【】（）％＃＠＆１２３４５６７８９０：；“”‘’"
    en_punc = ",.!?[]()%#@&1234567890:;\"\"''"
    table = str.maketrans(cn_punc, en_punc)

    s = s.strip()
    s = fullwidth_to_halfwidth(s)
    s = s.translate(table)
    # 将 \r, \n, \r\n, \t 替换为一个空格
    s = re.sub(r'[\r\n\t]+', ' ', s)
    s = re.sub(r"\s+", " ", s)  # 多余空白合并为一个空格
    s = s.replace("Φ", "φ").replace("φ", "直径")
    #s = s.replace("×", "X").replace("X", "x").replace("x", "*") #   “*”在数据库有可能导致奇怪问题，会被丢掉
    s = s.replace("*", "x").replace("×", "X").replace("x", "X")
    s = s.upper()  #被坑死了，python去重后是区分大小写的，但是mysql若字段的排序规则以 _ci 结尾（如 utf8mb4_unicode_ci），则 UNIQUE 约束会视 A 和 a 为相同值，禁止重复。若排序规则为 _bin（如 utf8mb4_bin），则 A 和 a 视为不同值，允许同时存在
    return s

def clean_dw(s: str = "") -> str:
    s = clean_string(s)
    s = s.replace("·", "").replace(".", ",")
    s = s.replace("KW?H", "kWh").replace("KW·H", "kwh")
    s = s.lower()
    return s