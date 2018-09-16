from langconv import Converter

def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

def Simplified2Traditional(sentence):
    '''
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    '''
    sentence = Converter('zh-hant').convert(sentence)
    return sentence

if __name__=="__main__":
	while True:
	    string=input('需要转换的中文：')
	    simplified_sentence=Traditional2Simplified(string)
	    traditional_sentence=Simplified2Traditional(string)
	    print('转换为简体： ',simplified_sentence)
	    print('转换为繁体： ',traditional_sentence)
	    print('=======================================')

