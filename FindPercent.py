class percentage():
    def percentageMark():
        tamil=int(input("tamil"))
        english=int(input("english"))
        math=int(input("math"))
        sicence=int(input("sicence"))
        socialsicence =int(input("socialsicence"))
        fiveSubjectmark = tamil + english + math + sicence + socialsicence
        maxMark = 500
        dev = fiveSubjectmark/maxMark 
        percentage = dev * 100
        return percentage


    