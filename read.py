def read_article(file_name):
    file = open(file_name, "r")
    if sumtype == 'sum':
        filedata = file.readlines()
        article = filedata[0].split(". ")
        sentences = []

        for sentence in article:
            print(sentence)
            sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
        
        
        return sentences
    else:
        filedata = file.read()
        return filedata
