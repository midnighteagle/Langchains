# improrting the OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

# importing the dotenv in the file.
load_dotenv()

# setup the embeddings:
Embeddings = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 500)

# creation of Documents
documents = [
    # list 
    
    "Virat Kohli is widely regarded as one of the greatest batsmen in the history of international cricket. Born on November 5, 1988, in Delhi, India, he rose to prominence after captaining the Indian team to a historic victory in the 2008 Under-19 World Cup. Known for his fierce aggression, impeccable technical mastery, and unparalleled chasing ability in limited-overs formats, Kohli served as the anchor of India's batting lineup for over a decade. As a former captain of the Indian national team across all formats, he instilled a culture of elite fitness, mental resilience, and dominant fast-bowling strategies that elevated India to the number one ranking in Test cricket. Over his illustrious career, he has shattered numerous records, including becoming the fastest player to reach 10,000 ODI runs and surpassing Sachin Tendulkar's legendary milestone for the most centuries in One Day Internationals. Beyond his extraordinary statistics, Kohli's global impact on fitness, commercial athletic branding, and the competitive spirit of modern cricket has firmly established him as a transcendent icon of world sport.",
    
    "Sachin Tendulkar, widely revered as the Master Blaster is globally acclaimed as one of the greatest cricketers to ever play the game. Born on April 24, 1973, in Mumbai, India, he made his international debut in 1989 at the tender age of 16, embarking on a monumental 24-year career that would define modern cricket. Blessed with an immaculate technique, textbook straight drives, and extraordinary mental longevity, Tendulkar carried the weight and expectations of a billion fans every time he walked out to bat. He stands as the all-time leading run-scorer in both Test matches and One Day Internationals (ODIs) and remains the only player in cricketing history to score 100 international centuries. A crowning achievement of his career came in 2011 when he won the ICC Cricket World Cup on his home ground in Mumbai. As the first sportsman to be awarded India's highest civilian honor, the Bharat Ratna, Tendulkar's legacy extends far beyond his breathtaking numbers he transformed cricket into a unifying cultural phenomenon in India and set the ultimate gold standard for generations of batsmen across the globe.",
    
    "Sunny Deol (born Ajay Singh Deol) is a legendary Indian actor, director, and politician who remains one of Hindi cinema's most iconic action stars. The eldest son of veteran actor Dharmendra, Sunny made a stellar debut in 1983 with the romantic drama Betaab, but quickly carved out a massive niche for himself as the ultimate angry young man of the late 80s and 90s. Famous for his powerful dialogue delivery, explosive action sequences, and the beloved pop-culture moniker of his Dhai Kilo Ka Haath (two-and-a-half-kilogram hand), he delivered career-defining, National Award-winning performances in cult classics like Ghayal and Damini.His historic blockbuster Gadar: Ek Prem Katha (2001) became a cultural phenomenon across India, a legacy he cemented further with the monumental box-office success of its sequel, Gadar 2, which smashed records upon its release. Beyond his cinematic career, Deol has also served the public as a Member of Parliament (MP). Characterized by his unique blend of intense, raw screen presence and an incredibly gentle, soft-spoken real-life persona, Sunny Deol stands as a true titan of Indian commercial entertainment.",

    "Dara Singh (born Deedar Singh Randhawa) was a legendary Indian professional wrestler, actor, and politician whose monumental physique and gentle persona made him an enduring symbol of ultimate strength in Indian pop culture. Born on November 19, 1928, in Punjab, he dominated the world of professional wrestling for decades, remaining undefeated throughout his career. He competed in hundreds of matches globally, famously defeating world champions like King Kong and Lou Thesz, which earned him the title of Rustom-e-Hind (Champion of India) and eventually induction into the Legacy category of the WWE Hall of Fame.Transitioning seamlessly into cinema, Dara Singh became India's first true action hero, starring in numerous stunt and feature films throughout the 1960s and 70s. However, he achieved immortal television status later in life for his definitive portrayal of Lord Hanuman in Ramanand Sagar's iconic epic series Ramayan (1987)—a performance so powerful that his face became synonymous with the deity for millions of households. He later capped his illustrious life of public service by serving as a nominated Member of Parliament in the Rajya Sabha, leaving behind a legacy as a timeless icon of humility, physical prowess, and cultural reverence.",

    "Rohit Sharma, widely celebrated as the Hitman, is one of the most destructive and elegant opening batsmen in modern cricket history and a highly successful captain of the Indian national team. Born on April 30, 1987, in Nagpur, Maharashtra, he made his international debut in 2007 but truly revolutionized his career when he was promoted to open the batting in 2013. Known for his effortless timing, signature pull shot, and an uncanny ability to score massive hundreds, Rohit holds the breathtaking record for the highest individual score in One Day Internationals (264 runs against Sri Lanka) and is the only player to smash three double-centuries in ODI cricket.As a leader, his legacy is defined by a brilliant tactical mind and a calm demeanor under pressure; he captained the Mumbai Indians to five historic Indian Premier League (IPL) titles and achieved a crowning international achievement by leading India to victory in the 2024 ICC Men's T20 World Cup. Following that triumph, he retired from T20 internationals as the format's all-time leading run-scorer and six-hitter, while continuing to lead the national side with distinction in Test and ODI formats.",

    "Akshay Kumar (born Rajiv Hari Om Bhatia) is one of Indian cinema's most prolific and versatile superstars, widely known as the Khiladi of Bollywood. Born on September 9, 1967, he trained extensively in martial arts in Bangkok and worked as a chef before making his acting debut in the early 1990s. He shot to fame with the thrilling Khiladi series, establishing himself as India's premier action star who famously performs his own high-octane stunts.",
    
    "Suresh Raina is a former Indian international cricketer widely celebrated as one of the finest left-handed middle-order batsmen and elite fielders of the modern white-ball era. Born on November 27, 1986, in Muradnagar, Uttar Pradesh, Raina was a true pioneer for India in the T20 format, becoming the first Indian batsman to score a century in all three international formats (Test, ODI, and T20I). Known for his aggressive stroke-play, exceptional ability to clear the boundary, and a handy right-arm off-spin option, he was a vital cog in the Indian team that won the 2011 ICC Cricket World Cup and the 2013 ICC Champions Trophy.",
    
    "Jaspreet Kaur, widely known by her online handle Behind the Netra, is an acclaimed British spoken-word artist, author, history educator, and researcher from London. She is celebrated for using her creative writing and public platform to advocate for gender equality, dismantle mental health stigma, and drive positive social change within both the South Asian diaspora and wider society.",
    
    "Ratan Tata (December 28, 1937 – October 9, 2024) was a visionary industrialist, philanthropist, and one of the most revered figures in Indian corporate history. Serving as the Chairman of the Tata Group from 1991 to 2012, and later as interim chairman, he transformed a historically conservative domestic conglomerate into a global powerhouse. Under his bold leadership, Tata Group revenues grew over forty-fold, driven by high-profile international acquisitions such as Tetley Tea, Jaguar Land Rover, and Corus Steel. Driven by a deep commitment to everyday citizens, he also spearheaded the development of the Tata Nano—conceived as an affordable car to give middle-class families a safer alternative to motorcycles)",
    
    "Pankaj Tripathi is one of the most celebrated, versatile, and deeply loved actors in contemporary Indian cinema and streaming entertainment. Born on September 28, 1976, in a small village in Gopalganj, Bihar, his journey from a humble farming background to the peak of Bollywood is a masterclass in patience, persistence, and raw talent.",
    
    "Artificial Intelligence (AI) is a branch of computer science dedicated to building software and systems capable of performing tasks that typically require human intelligence. This includes capabilities like reasoning, learning from past experiences, understanding natural language, recognizing visual pattern sequences, and solving complex problems.",
    
    "The multiverse is a theoretical concept in physics, cosmology, and philosophy suggesting that our observable universe is not the only reality, but merely one of countless coexisting universes.  While popular culture—like Marvel movies—frequently uses the multiverse as a backdrop for alternate timelines and doppelgängers, serious modern physicists take the hypothesis seriously because it naturally emerges from the math of established scientific frameworks",
    
    "India, officially known as the Republic of India (Bharatiya Ganarajya), is a vast, vibrant, and incredibly diverse nation located in South Asia. It is defined by its deep historical roots, staggering geographical variety, and its position as a fast-rising global superpower.",
    
    "Gaya is a deeply historic and holy city located in the state of Bihar, India. It is situated on the banks of the Falgu River and stands as the second-largest city in the state. Gaya holds immense spiritual, historical, and cultural significance, drawing millions of pilgrims and travelers from across the globe every year."

]

# Creation of Query
query = input("Ask About stars Only: >> ") 

# Embedding the Documents and Query Both.

Doc_Embeddings = Embeddings.embed_documents(documents)
Query_Documents = Embeddings.embed_query(query)

score = cosine_similarity([Query_Documents], Doc_Embeddings)[0]
print(score)
index, score = sorted(list(enumerate(score)), key = lambda pair:pair[1] ) [-1]  

print(query)
print(documents[index])
print("similarities Score is :", score)