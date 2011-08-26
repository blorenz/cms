def mark_words(content,keyword):
    total_words = []

def count_density(content,keyword):
    number_times = content.count(keyword)
    ngram_count = len(keyword.split())
    density = number_times / float(len(content.split()))
    return density



def test_mamaMia():
    mamaMia = \
            "Mamma mia, here I go again\
            Mamma mia, here I go again\
            My my, how can I resist you?\
            Mamma mia, does it show again?\
            My my, just how much I've missed you"

    print count_density(mamaMia,'Mamma mia')

if __name__ == "__main__":
    test_mamaMia()


