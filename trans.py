from transliterate.base import TranslitLanguagePack


class RomanianLanguagePack(TranslitLanguagePack):
    language_code = "ro"
    language_name = "Romanian"
    mapping = (
        u"абвгдезийклмнопрстуфхъыьАБВГДЕЗИЙКЛМНОПРСТУФХЪЫЬ",
        u"abvgdeziiclmnoprstufh'iiABVGDEZIJKLMNOPRSTUFH'Y'",
    )
    pre_processor_mapping = {
        u"Ч": u"Ch",
        u"ч": u"ci",
        u"Ш": u"S",
        u"ш": u"s",
        u"Ж": u"J",
        u"ж": u"j",
        u"Ц": u"T",
        u"ц": u"t",
        u"ё": u"io",
        u"Ю": u"Iu",
        u"ю": u"iu",
        u"Я": u"ea",
        u"я": u"ea",
    }


