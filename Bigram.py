import math

SENTENCE_START = '<s>'
SENTENCE_END = '</s>'

class BigramLanguageModel:
    def __init__(self, file_path, smoothing=False):
        self.counts = dict()
        self.context_counts = dict()

        with open(file_path, "r") as f:
            for line in f:
                everyline = line.rstrip("\n")
                words = everyline.split(" ")
                words.insert(0,SENTENCE_START)
                words.append(SENTENCE_END)
                previous_word = None
                for word in words:
                    if previous_word != None:
                        if previous_word != SENTENCE_START and word != SENTENCE_END:
                            self.counts[(previous_word +" "+ word)] = self.counts.get((previous_word +" " +word), 0) + 1
                            self.context_counts[previous_word] = self.context_counts.get(previous_word, 0) + 1
                            self.counts[word] = self.counts.get(word,0) + 1
                    previous_word = word
            # print(self.counts)
            # print(self.context_counts)
        with open("./bigram_file_test.txt", "w") as f:
            for ngram,count in self.counts.items():
                # print(ngram, count)
                tmp = ngram.split(" ")
                tmp.pop()
                context = " ".join(tmp)
                print(context)
                # print(self.context_counts)
                if context in self.context_counts:
                        # print(context)
                    probability = float(self.counts[ngram]/self.context_counts[context])
                    f.write(str(ngram) + "  " + str(probability)+"\n")
def Load_Model(file_path):
    probabilities  = dict()
    with open(file_path, "r") as f:
        for line in f:
            everyline = line.rstrip("\n")
            xs = everyline.split("  ")
            probabilities[xs[0]] = xs[1]
        # print(probabilities)
    return probabilities

def Test_Bigram(file_test_path):
    probabilities = Load_Model("./bigram_file_test.txt")
    # print(probabilities)
    lamda1 = 0.4
    lamda2 = 0.5
    V = 1000000
    W = 0
    H = 0

    with open(file_test_path, "r") as f:
        for line in f:
            everyline = line.rstrip("\n")
            words = everyline.split(" ")
            words.append(SENTENCE_END)
            words.insert(0,SENTENCE_START)
            # print(words)
            previous_word = None
            for word in words:
                if previous_word != None:
                    if previous_word != SENTENCE_START and word != SENTENCE_END:
                        if word in probabilities:
                            P1 = lamda1*float(probabilities[word]) + (1-lamda1) / V
                            # print(probabilities[word])
                            print(P1)
                        # print(type(tamp))
                        tamp = "".join(previous_word + " "  + word)
                        if tamp in probabilities[previous_word + " "  + word]:
                            # print("ok")
                            P2 = lamda2*float(probabilities[previous_word + " "  + word]) + (1-lamda2) * P1
                            # print(P2)
                        # H += math.log(1 / P2, 2)
                        # W += 1
                previous_word = word
            print(H)
            print(W)

    # print(P1)
    # print(P2)
    # print(H)
    # print(W)
    # print("entropy = " + str(H / W))

if __name__ == '__main__':
    #
    # rstrip: tạo ra một chuỗi copy loại bỏ kì từ cuối cùng của chuỗi
    # được truyền vào trong hàm
    # slpit: tách phần tử rồi đẩy vào mảng
    #

    data_train_path = "./test/02-train-input.txt"
    # data_test_path = "./test/02-test-input.txt"
    data_train_wiki_path = "./data/wiki-en-train.word"
    data_test_wiki_path = "./data/wiki-en-test.word"
    data_test_bigram = "./bigram_data_test.txt"
    dataset_model = BigramLanguageModel(data_train_path)
    # print(dataset_model)
    # Test_Bigram(data_test_bigram)

