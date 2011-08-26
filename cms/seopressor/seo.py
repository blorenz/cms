from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer

def getBigram(haystack):
    tokenizer = WordPunctTokenizer()
    words = tokenizer.tokenize(haystack)
    bcf = BigramCollocationFinder.from_words(words)
    stopset = set(stopwords.words('english'))
    filter_stops = lambda w: len(w) < 3 or w in stopset
    bcf.apply_word_filter(filter_stops)

    return bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4)

def getTrigram(haystack):
    tokenizer = WordPunctTokenizer()
    words = tokenizer.tokenize(haystack)
    tcf = TrigramCollocationFinder.from_words(words)
    stopset = set(stopwords.words('english'))
    filter_stops = lambda w: len(w) < 3 or w in stopset
    tcf.apply_word_filter(filter_stops)

    return tcf.nbest(TrigramAssocMeasures.likelihood_ratio, 4)

def mark_words(content,keyword):
    total_words = []

def count_density(content,keyword):
    number_times = content.count(keyword)
    ngram_count = len(keyword.split())
    density = number_times / float(len(content.split()))
    return density



def test_mamaMia():
    weightloss = """The Dangers of Water Fasting Weight Loss

    Coming from age-old times, water fasting weight loss has had faith based meaning. Fasting is part of numerous religions as a show of loyalty to the cloth. Water fasting weight loss has also been a resource utilized for protest and exposure. The faster is subject to horrendous hunger pangs. Why would someone do this to themselves?

    A broad range of folks make use of fasting to get speedy outcomes and to lose weight. There are several effective specifics that can be credited to water fasting. While water does indeed not really cost you anything for you to obtain, the expense of the diet is really small. Because no food is becoming eaten, the free water is the only element essential. Next, an individual can obtain weight loss gains really rapidly. Without ingesting food, our body begins to utilize its own supply of food.The body fat in the human body can serve as fodder for the generation of energy for your internal organs. Third, it detoxifies your body. The state of detoxing is when one.s body is getting rid of the elements which can be toxic although not reconsuming them. Lastly, fasting is definitely achieved. The only real necessity is sufficient willpower to step away from foods. Every person is actually capable immediately of accomplishing this. No weight loss alternatives need to be furnished. Absolutely no distinctive meals or ingredients must be purchased. The dieting switch can immediately be switched on.
    The .Good. of Water Fasting Weight Loss

    Although dangers are out there, you can find positive aspects that may result from water fasting weight loss. Water is naturally free of vegetable or animal fats and possesses certainly no calories. The consumption of a substantial increase of water will assist the kidneys in cleansing. Urinary tract infections will likely be prevented by the volume of urine that flows from the considerable amounts of water drank. Appetite can be staved off by drinking plenty of water. Water can even clear the skin of blemishes and promote a healthier glow. After all, the human body is about thirty percent water so a water fasting weight loss plan should be regarded as holistic and all-natural.

    Weight that is shed from a water fasting weight loss program can be quite numerous and also very dangerous. Each person is different so the weight loss will vary but could be upwards of four pounds a day! This is one of the biggest draws that can suppress any inhibition to the negative factors of water fasting weight loss. Sometimes a water fasting weight loss diet plan will be undertaken with the notion of quitting after a few pounds are lost. After a few pounds, the dieter wants more gains and she stays on the diet convinced that it isn.t dangerous.

    Exactly how water fasting results in weight loss isn.t rocket science . but it is biological science! Calories that are consumed that do not get burnt off with work are converted into fat. Fat is like a battery that the body can call on when it needs energy but food is not in the system. If one continues to overeat, these stores of energy are never called upon thus they are continuously added to by the extra calories. The striking thing is that our bodies are naturally fighting water fasting weight loss! The body begins to shut down processes and reduce metabolism as not to burn through its energy reserves when a person begins to fast. With the metabolism slowed, the body is still in this state when it returns to the consumption of food. The body is utilizing even less of the food that is being ingested than before, increasing the amount of fat that remains. In sum, more weight will be acquired and all the weight that was lost will regain when you return to a normal diet routine from a water fasting weight loss diet.

    There are scientific studies that tend to favor water fasting weight loss, but they are presented in skewed fashion. Calorie reduction in diets has had studies observe longevity effects on humans and rodent subjects. Diseases that correlate to aging have been thought to be delayed by water fasting. Such examples of diseases that could be delayed are diabetes, heart disease and Alzheimer.s disease. Arteries could benefit from water fasting weight loss as they are more cholesterol-free. This is because of the belief that the foods that bring about this problem are now being abstained from and not absorbed.
    The Bad of Water Fasting Weight Loss

    It is not correct assume that the medical field is a proponent of a water fasting weight loss diet plan. First, the subjects of the study weren.t followed long enough to see if water fasting could result in a longer life expectancy. In addition, many vitamins and minerals are necessary to the human body to remain healthy. Water is not a sufficient source of these minerals and vitamins. Other nutrients are required by the body that simply are not found in water. The conditions that can result from not getting enough nutrients are dizziness, gallstones, dehydration, fatigue and constipation. The ultimate risk is of death or serious bodily harm if you fast for too long.

    Medical professionals recommend not to fast if you suffer from any one of a number of medical conditions like diabetes. Water fasting weight loss diets can result in uncontrolled blood sugar levels that could result in blood sugar comas that could lead to death. Another medical condition that is dangerous to fast with is the condition of being pregnant. Weight gain is a natural thing that comes with the joy of pregnancy. The developing baby will be without the fundamental vitamins and nutrients of life if the mother intends to water fast. Vitamins and pills are not an adequate substitute for what is found naturally in the foods that we consume every day . meats, poultry, fruits, vegetables, dairies and grains.
    Even if you come to the conclusion that water fasting weight loss is unsafe but still yearn to fast to lose weight, consult with a licensed medical practitioner prior to commencing. A doctor will discuss if it is safe and appropriate for you. There are many risks to encounter during water fasting weight loss."""
    
    mamaMia = \
            "Mamma mia, here I go again\
            Mamma mia, here I go again\
            My my, how can I resist you?\
            Mamma mia, does it show again?\
            My my, just how much I've missed you"

    print count_density(mamaMia,'Mamma mia')
    print getBigram(weightloss)
    print getTrigram(weightloss)

if __name__ == "__main__":
    test_mamaMia()


