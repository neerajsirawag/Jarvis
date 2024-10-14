from buildin.Chrome import ChromeList

class Trash_Parce:
    
    #[1,2,3,4,5] #Q = "ARTTTT" => FALSE
    #[1,2,3,4,5] #Q = "1hwe2sdf" => TRUE
    @staticmethod
    def check_if_any_in_str(lis: list, st: str):
        for i in lis:
            if i in st:
                return True
        return False
    
    
    #["hii","my","name"] #Q = hii my Neeraj ==> FALSE
    #["hii","my","name"] #Q = hii my name is Neeraj ==> TRUE
    @staticmethod
    def check_if_any_in_list(lis: list, st: list):
        for i in lis:
            if type(i) in list:
                if not Trash_Parce.check_if_any_in_str(i,st):
                    return False
            else:
                if i not in st:
                    return False
        return True

def ChromeCode(query):
    for _, lists in ChromeList.items():
        A = Trash_Parce.check_if_any_in_str(lists, query)
        if A:
            return _
    return False