import re
import math


SENTENCE_END = "</s>"

class UnigramLanguageModel:
    def __init__(self, file_path, smoothing=False):
        self.counts = dict()
        self.total_count = 0
        with open(file_path, "r") as f:
            for line in f:
                everyline = line.rstrip("\n")
                words = everyline.split(" ")
                words.append(SENTENCE_END)
                for word in words:
                    self.counts[word] = self.counts.get(word, 0) + 1
                    self.total_count += 1
        with open("./model_file_wiki.txt", "w") as f:
            for word in self.counts:
                probability = float(self.counts[word]/self.total_count)
                f.write(word + " " + str(probability)+"\n")
def Load_Model(file_path):
    probabilities  = dict()
    with open(file_path, "r") as f:
        for line in f:
            everyline = line.rstrip("\n")
            xs = everyline.split(" ")
            probabilities[xs[0]] = xs[1]
    return probabilities

def Test_and_Print(file_test_path):
    probabilities = Load_Model("./model_file_wiki.txt")
    print(probabilities)
    lamda1 = 0.95
    lamdaunk = 1 - lamda1
    V = 1000000
    W = 0
    H = 0
    unk = 0
    with open(file_test_path, "r") as f:
        for line in f:
            everyline = line.rstrip("\n")
            words = everyline.split(" ")
            words.append(SENTENCE_END)
            for w in words:
                W += 1
                P = lamdaunk / V
                # check = probabilities.get(w,0)
                if w in probabilities.keys():
                    P += lamda1 * float(probabilities[w])
                else:
                    unk += 1
                H += math.log(1/P,2)
    print("entropy = " + str(H/W))
    print("coverage = " + str((W - unk)/W))


if __name__ == '__main__':
    #
    # rstrip: tạo ra một chuỗi copy loại bỏ kì từ cuối cùng của chuỗi
    # được truyền vào trong hàm
    # slpit: tách phần tử rồi đẩy vào mảng
    #

    data_train_path = "./test/01-train-input.txt"
    data_test_path = "./test/01-test-input.txt"
    data_train_wiki_path = "./data/wiki-en-train.word"
    data_test_wiki_path = "./data/wiki-en-test.word"
    # dataset_model = UnigramLanguageModel(data_train_wiki_path)
    # print(dataset_model)
    Test_and_Print(data_test_path)
