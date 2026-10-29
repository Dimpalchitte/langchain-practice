from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()
model1 = ChatOpenAI()
model2 = ChatAnthropic(model="claude-2")

prompt1 = PromptTemplate(
    template = "generate short and simple notes from the following text:\n\n{text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template = "generate 5 short question answers from the following text:\n\n{text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template = "MERGE THE PROVIDED NOTES & QUIZ INTO A SINGLE DOCUMENT \n\n{NOTES}\n\n{QUIZ}",
    input_variables=["NOTES", "QUIZ"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    NOTES=prompt1 | model1 | parser,
    QUIZ=prompt2 | model2 | parser,
)

merge_chain = prompt3 | model1 | parser
chain = parallel_chain | merge_chain

text = """The Bhagavad Gita is a sacred dialogue between Lord Krishna and Arjuna.
It takes place on the battlefield of **Kurukshetra**.  
Arjuna is a great warrior and prince of the Pandava family.  
Before the battle begins, Arjuna asks Krishna to place his chariot between the two armies.  
Arjuna sees his relatives, teachers, friends, and loved ones on both sides.  
He becomes overwhelmed with sorrow and confusion.  
Arjuna feels that winning the kingdom is meaningless if it requires killing his own people.  
He puts down his weapons and refuses to fight.  
Krishna begins guiding Arjuna through his crisis.  
Krishna teaches that the **Atman, or soul, is eternal**.  
The physical body is temporary, but the soul cannot be destroyed.  
Just as a person changes clothes, the soul changes bodies.  
Therefore, death is not the destruction of the eternal self.  
Krishna tells Arjuna that avoiding his duty because of fear is not the right solution.  
Every person has responsibilities according to their nature and circumstances.  
Arjuna's duty as a warrior is to fight for righteousness.  
Krishna introduces the principle of **Dharma**, or righteous duty.  
Dharma means living according to one's responsibilities and moral principles.  
Krishna teaches **Karma Yoga**, the path of selfless action.  
A person should perform their duties sincerely without becoming attached to the results.  
We control our actions, but we cannot completely control their outcomes.  
Therefore, we should focus on doing our best rather than worrying about rewards.  
Attachment to results creates anxiety, fear, and disappointment.  
Selfless action helps a person remain calm and balanced.  
Krishna says that true wisdom comes from understanding the difference between the eternal self and the temporary body.  
A wise person remains steady during both success and failure.  
Such a person does not become excessively happy with success or devastated by failure.  
Krishna calls this balanced state **Samatva**, or equanimity.  
The Gita teaches that desire can disturb the mind.  
Uncontrolled desire can lead to anger and confusion.  
Anger can destroy judgment and lead to destructive actions.  
Therefore, controlling the senses and mind is extremely important.  
The mind can either be our friend or our enemy.  
A disciplined mind helps us achieve peace and wisdom.  
An uncontrolled mind can create suffering and confusion.  
Krishna teaches **Jnana Yoga**, the path of knowledge.  
Through knowledge, a person understands their true nature.  
Knowledge helps remove ignorance and false identification with the body.  
Krishna also explains **Karma**, the law of action and consequence.  
Every action has consequences that influence our future experiences.  
However, selfless actions performed without attachment do not bind a person in the same way.  
Krishna encourages Arjuna to act without selfish motives.  
He explains that true renunciation does not mean abandoning all responsibilities.  
True renunciation means giving up attachment to the fruits of one's actions.  
Krishna teaches **Dhyana Yoga**, the path of meditation.  
Meditation helps calm the mind and develop concentration.  
A disciplined person can gradually control thoughts and emotions.  
Krishna advises moderation in food, sleep, work, and recreation.  
Extreme behavior is generally not helpful for spiritual progress.  
The Gita also presents **Bhakti Yoga**, the path of devotion.  
Krishna teaches that sincere devotion can lead a person toward spiritual realization.  
Devotion involves love, faith, surrender, and remembrance of the Divine.  
Krishna explains that the Divine exists within all living beings.  
Therefore, all beings should be treated with compassion and respect.  
A true devotee does not hate others.  
Such a person develops qualities like kindness, humility, forgiveness, and self-control.  
Krishna explains the three **Gunas**: Sattva, Rajas, and Tamas.  
**Sattva** represents purity, knowledge, harmony, and clarity.  
**Rajas** represents passion, activity, ambition, and attachment.  
**Tamas** represents ignorance, laziness, confusion, and inertia.  
Human behavior is influenced by these three qualities.  
Spiritual growth involves rising beyond their limitations.  
Krishna describes the characteristics of a person who has transcended the Gunas.  
Such a person remains calm regardless of changing circumstances.  
Krishna also discusses different types of faith.  
A person's faith influences their thoughts, choices, and behavior.  
The Gita explains that food, actions, charity, and discipline can also reflect the three Gunas.  
Krishna teaches that charity should be given selflessly and at the appropriate time and place.  
True spiritual discipline should not be performed merely for public recognition.  
Pride and ego can prevent spiritual progress.  
Humility is therefore an important quality for a seeker.  
Krishna reveals his **Vishvarupa**, or universal form, to Arjuna.  
Arjuna sees the entire universe within Krishna's divine form.  
This vision shows that Krishna represents the infinite and universal reality.  
Arjuna realizes that Krishna is the ultimate source of all creation and existence."""


result = chain.invoke({"text": text})
print(result)
chain.get_graph().print_ascii()
