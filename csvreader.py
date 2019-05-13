def readfile():
    c3 = ['happy', 'sad', 'sarcasm', 'sassy', 'angry', 'bored', 'shit', 'disappointed', 'study', 'exams', 'presentation', 'drunk', 'embarrassed', 'slap', 'punch', 'hit', 'avenger', 'sos', 'just kidding', 'oh my god', 'lol', 'lmfao', 'ttyl', 'brb', 'byob', 'seriously', 'festival', 'party', 'excited', 'shocked', 'surprsie', 'hungry', 'eat', 'school', 'college', 'think', 'tired', 'sleep', 'lonely', 'stressed', 'nervous', 'kiss', 'ily', 'bae', 'suspicious', 'frustrated', 'anxiety', 'drive', 'meet', 'love', 'flirt', 'peace out', 'legendary', 'friends', 'high five', 'bff', 'idk', 'news', 'greetings', 'morning', 'night', 'texting', 'fifa', 'computer', 'weather', 'pizza', 'food', 'football', 'cunning', 'eveteasing', 'cartoon','soccer', 'playstation', 'tv', 'haha', 'game of thrones', 'chill', 'you know nothing', 'chill', 'joey', 'homework', 'Starwars', 'office', 'math', 'data science', 'i am broke', 'holiday', 'art', 'painting', 'salman','hmiym', 'weed', 'flight', 'fight', 'bitch', 'ditch', 'breakup', 'friendzone', 'gym', 'photos', 'smoke', 'money', 'movie', 'what', 'why', 'how', 'minions', 'heart', 'pokemon', 'coffee', 'bollywood', 'srk','noodles', 'coke', 'marvel', 'cook', 'no', 'yes', 'days', 'weeekend', 'thanks', 'you are welcome', 'ugh', 'mother', 'scream', 'talk', 'sorry', 'justin bieber', 'whatsapp', 'USA', 'trump', 'hollywood','modi', 'gamble', 'poker', 'nevermind', 'sure', 'drama', 'queen', 'king', 'btw', 'haters gonna hate', 'war', 'god', 'michal scott', '?', 'harry potter', 'lord of the rigns', 'ready', 'ronaldo', 'messi', 'ipl','sherlock', 'lgbtq', 'lies', 'freedom', 'goals', 'love', 'whats up', 'sansa star', 'captain marvel', 'by the way', 'laugh', 'bro', 'celebration', 'google it', 'wow', 'drop', 'club', 'swim', 'beach', 'thanksgiving', 'halloween', 'st. patrick', 'paris', 'india', 'hakuna matata', 'bill', 'company', 'where', 'system', 'each', 'right', 'program', 'hear', 'so', 'question', 'during', 'work', 'play', 'government', 'run', 'small', 'number', 'off', 'always', 'move', 'like', 'night', 'live', 'Mr', 'point', 'believe', 'hold', 'today', 'bring', 'happen', 'next', 'without', 'before', 'large', 'all', 'million', 'must', 'home', 'under', 'water', 'room', 'write', 'mother', 'area', 'national', 'money', 'story', 'young', 'fact', 'month', 'different', 'lot', 'right', 'study', 'book', 'eye', 'job', 'word', 'though', 'business', 'issue', 'side', 'kind', 'four', 'head', 'far', 'black', 'long', 'both', 'little', 'house', 'yes', 'after', 'since', 'long', 'provide', 'service', 'around', 'friend', 'important', 'father', 'sit', 'away', 'until', 'power', 'hour', 'game', 'often', 'lead', 'social', 'understand', 'whether', 'back', 'watch', 'together', 'follow', 'around', 'parent', 'only', 'stop', 'face', 'anything', 'create', 'public', 'already', 'speak', 'others', 'read', 'level', 'allow', 'add', 'office', 'spend', 'door', 'health', 'person', 'art', 'sure', 'such', 'war', 'history', 'party', 'within', 'grow', 'result', 'open', 'change', 'morning', 'walk', 'reason', 'low', 'win', 'research', 'girl', 'guy', 'early', 'food', 'before', 'moment', 'himself', 'air', 'teacher', 'force', 'offer', 'enough', 'both', 'education', 'across', 'although', 'remember', 'foot', 'second', 'boy', 'maybe', 'toward', 'able', 'age', 'off', 'policy', 'everything', 'love', 'process', 'music', 'including', 'consider', 'appear', 'actually', 'buy', 'probably', 'human', 'wait', 'serve', 'market', 'die', 'send', 'expect', 'home', 'sense', 'build', 'stay', 'fall', 'oh', 'nation', 'plan', 'cut', 'college', 'interest', 'death', 'course', 'someone', 'experience', 'behind', 'reach', 'local', 'kill', 'six', 'remain', 'effect', 'use', 'yeah', 'suggest', 'class', 'control', 'raise', 'care', 'perhaps', 'little', 'late', 'hard', 'field', 'else', 'pass', 'former', 'sell', 'major', 'sometimes', 'require', 'along', 'development', 'themselves', 'report', 'role', 'better', 'economic', 'effort', 'up'
          ]

return list(set(c3))

def extract_time(json):
    try: #Also convert to int since update_time will be string.When comparing# strings, "10"
is smaller than "2".
return int(json['Score'])
except KeyError:
    return 0

def n():
    j = [{
         'id': 1,
         'Score': 2
         }, {
         'id': 2,
         'Score': 3
         }]
j.sort(key = extract_time, reverse = True)
print(j)
n()
