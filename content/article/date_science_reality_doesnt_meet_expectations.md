Title: Data Science: Reality Doesn't Meet Expectations
Slug: data-science-reality-vs-expectations
Summary: Sevem common ways a data science role may not meet your expectations through tens of data scientist interviews and anecdotes from popular median
Date: 2019-04-07 1:45
Category: Articles
Keywords: data science reality expectations
Tags: data science
Authors: Dan Friedman

Disclaimer: I use the term Data Scientist throughout this post; however, popular titles such as Machine Learning Engineer, Data Analyst, Data Engineers, BI analysts share similar responsibilities and could be used interchangeably here.

I had high hopes about the potential impact of being a Data Scientist. I felt every company should be a “data company”. 

My expectations did not meet reality.

Where did my expectations come from? 

I attended a 12-week data science bootcamp in mid-2016. 11 of the 12 weeks’ focus were on machine learning (ML) and artificial intelligence (AI). At this time, ML & AI news mentions had hit an <a href="https://www.google.com/url?q=https://www.gartner.com/smarterwithgartner/top-trends-on-the-gartner-hype-cycle-for-artificial-intelligence-2019/&sa=D&ust=1586278559727000&usg=AFQjCNG9wXSpgrRxikBtkGMJhDQVkhk3CA" target="_blank">all-time high</a>. Tesla was paving the way in <a href="https://www.tesla.com/autopilot" target="_blank">self-driving cars</a>, and even older behemoths like General Motors (GM) invested over a <a href="https://fortune.com/2016/03/11/gm-buying-self-driving-tech-startup-for-more-than-1-billion/" target="_blank">billion dollars</a> in an AI company to stay at the frontier of automotive tech. At the consumer level, headphones emerged that used AI to automatically translate your words to someone else as you speak, and an <a href="https://www.theverge.com/2019/4/13/18309459/openai-five-dota-2-finals-ai-bot-competition-og-e-sports-the-international-champion" target="_blank">AI beat the world’s best esports team</a>.

I figured I’d spend most of my time buried in code and data to find hidden patterns, implement machine learning models in production and optimize them. Executives would likely rely on me to help inform the product roadmap based on insights in data, and I would be highly valued.

However, practically none of that happened. 

Over the past few years, I’ve worked as a Data Scientist, a Data Engineer, and as an industry consultant. I’ve also learned from the stories of dozens of data scientists and similar professions, actively read articles on data science and followed data science thought leaders on Twitter. 

Across these diverse data experiences, I have noticed common themes. 

Below are seven most common (and at times flagrant) ways that data science has failed to meet expectations in industry. Throughout each section, I’ll propose solutions to these shortcomings.

1. People don’t know what “data science” does.
2. Data science leadership is sorely lacking.
3. Data science can’t always be built to specs.
4. You’re likely the only “data person.”
5. Your impact is tough to measure — data doesn’t always translate to value.
6. Data & infrastructure have serious quality problems.
7. Data work can be profoundly unethical. Moral courage required. 

### 1. People don’t know what “data science” does.

Some people think “data science” is all ML, AI and/or custom algorithms. Others think it’s simply analytics. Many data scientists may spend a significant portion of their time on Extract-Transform-Load (ETL). The truth is - all of these things are possible! 

Due to this, in interviews, you can be asked about any of these topics and more! In 50+ interviews for data related jobs, I’ve been asked about AB testing, SQL analytics questions, optimizing SQL queries, how to code a game in Python, Logistic Regression, Gradient Boosted Trees, data structures and algorithms programming problems and much more! 

It’s daunting to study a wide breadth and still have depth. Keep your chin up! Expect interviews to be confusing and frustrating, as there’s no de facto set of problems and questions. Ask your hiring managers for specific details on the interview process, technologies you’ll be asked to use and why those will be asked. The more context you have, the better you can prepare to ace it! 

On the job, you may be asked to solve a hard problem and have minimal to no direction on how to reach the solution. Because people don’t know what data science does, you may have to support yourself with work in devops, software engineering, data engineering, etc. If you end up as the only “data person” on the team, you may want to start building out a cohort of external mentors before you arrive on the job who can advise you as you proceed into uncharted waters. 

### 2. Data science leadership is sorely lacking

Most executives in charge of data science decision-making are neither educated nor trained in actual data science theory and techniques. Instead, they have relied upon non-data-driven, plug-and-play features that can be launched in a timely manner. 

Few teams have a Head of Data, Data Science Manager or other relevant role. As a Data Scientist, you may report to someone specialized in just product, engineering or even another discipline. 

These non-data proficient executives and managers are usually the ones to make important product decisions. In tech, top-down decision-making is still very prevalent. You may not have a “seat at the table” or be respected enough to be included in these decisions and your research may not be valued. Where does that leave you as a Data Scientist?

In one experience, a fellow researcher spent over a month researching a particular value among our customers through qualitative and quantitative data. She presented a well-written and evidence-backed report. Yet, a few days later, a key head of product outlined a vision for the team and supported it with a claim that was antithetical to the researcher’s findings! 

Even if a data science project you advocate for is greenlighted, you may be on your own as the rare knowledgeable person to plan and execute it. It’s unlikely leadership will be hands-on to help you research and plan out the project. This could be a very difficult road ahead - especially for someone junior in the industry.

### 3. Data science can’t always be built to specs

You and peers may have expectations on the potential of data science projects. Two common types of projects are in exploratory analyses and machine learning. 

In an exploratory analysis, someone or yourself may have questions on the data and you simply want to answer those. Common questions are: How many users click this button; what % of users that visit a screen click this button; how many users have signed up by region or account type? However, the data needed to answer those questions may not exist! If the data does exists, it’s likely “dirty” - undocumented, tough to find or could be factually inaccurate. It’ll be tough to work with! You could spend hours or days attempting to answer a single question only to discover that you can’t sufficiently answer it for a stakeholder.

In machine learning, you may be asked to optimize some process or experience for consumers. However, there’s uncertainty with how much, if at all, the experience can be improved! 

![Machine learning XKCD comic](https://imgur.com/7nPWUrS.jpeg)

In one engagement, the product had a newsfeed with posts from a large network of people - content often irrelevant for users. You may have noticed your Facebook or Twitter newsfeed content is ordered in a way to show posts most relevant to you near the top - optimized to consume the content and click through on what’s relevant. Similarly, the team I worked with was asked to optimize the feed. However, they didn’t know exactly how much the feed could be improved.

The team evaluated the optimization of the feed by an evaluation metric called uCTR - unique click through rate. This is essentially the probability the user would click on the post to like it or comment on it in a session.   

Executives had expectations that the experience would be drastically improved. The machine learning team did improve the metric by over 50% - but only for a small group of users who were very engaged because there was more signal in the data to improve that group’s experience. The majority of users still had a bad viewing experience even after the ML model was implemented! 

50% seems significant but may be rather insignificant too. It’s high on a relative change but still can be a small absolute change. Picture this: you have 10 dollars in cash and you increase it by 50% in a day. You now have 15 dollars in cash. Yet that’s still a small number on an absolute scale. You can only buy 1 or 2 meals out! 

Since many ML projects may not be built to the expectations of teams, most projects likey <a href="https://venturebeat.com/2019/07/19/why-do-87-of-data-science-projects-never-make-it-into-production/" target="_blank">don’t make it into production</a>.

### 4. You’re likely the only “data person”

Nearly every team in a business will want to know their progress through quantitative measures. All teams, whether sales, customer support, engineering, or marketing, want metrics and data-driven dashboards to measure their efficacy and progress. 

Most companies with <100 employees have few employees who are proficient in SQL, databases, data analysis and data visualizations. These are skills necessary to analyze data and produce these dashboard outputs. 

As the resident Data Scientist, you may become easily inundated with requests from multiple teams at once. Be prepared to ask these teams to qualify and defend their requests, and be prepared to say “no” if their needs fall outside the scope of your actual priority queue. I’d recommend utilizing the <a href="https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/" target="_blank">RICE prioritization technique</a> for projects.

Moreover, you may quickly realize much of this work is repetitive and while time-consuming, is “easy”. In fact, most analyses involve a great deal of time to understand the data, clean it and organize it. You may spend a minimal amount of time doing the “fun” parts that data scientists think of: complex statistics, machine learning and experimentation with tangible results.

### 5. Your impact is tough to measure — data doesn’t always translate to value

Two ways to interpret this section’s header come to mind. 

For one, Data Scientists are often in “support” roles. Most organizations make the majority of their decisions on intuition that stems from past readings and personal experiences - not from a Data Scientist’s analyses. I’d be shocked if you could find a small to medium size organization that acted otherwise. Generally, you want to err on the side of being decisive rather than being overly cautious in order to succeed in business. (Though, obviously this can backfire on you.) As a Data Scientist in the org, are you essential to the business? Probably not. The business could go on for a while and survive without you. Sales will still be made, features will still get built, customer support will handle customer concerns, etc. 

When I first started, I initially thought I’d be incredibly valued as the gatekeeper for helping justify business decisions. However, that was rarely the case. DJ Patil, the former Chief Data Scientist at the White House, once stated in a podcast episode that you as a Data Scientist should try to find a situation to be incredibly valuable on the job! It’s tough to find that from the outskirts of applying to jobs, but internally, you can make inroads supporting stakeholders with evidence for their decisions!

Another challenge being usually a “support” role in a company is quantifying your impact. A common data science task is to help a Product Manager answer a question about some recent activity in the data. You can also issue a product recommendation based on your insights. So what? How do you measure whether this work of yours was impactful? 

It’s tough to do. Most people don’t put a price or value on analyses. 

Did you save the company 10 million dollars through your analysis for the sales team that led them to avoiding a huge and costly new workflow, or did the sales team save the 10 million dollars? Truthfully, will anyone even value the 10 million dollars if it was simply “saved” and never spent? 

On the job, I’d recommend you document your work well and calculate the monetary value of your analyses based on factors like employee salary, capital investments, opportunity cost, etc. These analyses will come in handy for a promotion/review packet later too. 

I realize the actual analysis is challenging to do and I’ve only heard of one data science manager who executed on this well with his team! Seek help from others on how to best craft these analyses.

### 6. Data & infrastructure have serious quality problems

In data science books, online classes, online tutorials, and Kaggle competitions, the problems faced are radically different from what exists in industry.

In those online resources, you’ll have “clean” data that’s easily available, well-documented, and structured in an outline that allows you to apply data science techniques to answer the problem. 

In regards to quality of data on the job, I’d often compare it to a garbage bag that ripped, had its content spewed all over the ground and your partner has asked you to find a beautiful earring that was accidentally inside. Essentially, the data will be tough to find and poorly documented — or not documented at all. Data can also be presented in unstructured formats such as complicated JSON, submitted text responses with punctuation, emojis, and minimal context. Moreover, data that seems helpful can prove to be a red herring. 

![Futurama can't trust this data meme](https://imgur.com/zlBFq4G.jpeg)

Like the famous saying, “garbage in, garbage out”. If you don’t have quality data, you likely won’t produce a quality output to meet your stakeholders’ expectation. 

Cleaning data may likely become the majority of your work. In 2016, a <a href="https://visit.figure-eight.com/rs/416-ZBE-142/images/CrowdFlower_DataScienceReport_2016.pdf" target="_blank">survey</a> distributed to experienced Data Scientists by the popular ML-focused company Crowdflower claimed “3 out of every 5 data scientists we surveyed actually spend the most time cleaning and organizing data”. The Data Scientist, in many cases, should be called the <a href="https://en.wikipedia.org/wiki/Data_janitor" target="blank">Data Janitor</a>. 
¯\_(ツ)_/¯ 

Note, if you spend most of your time on data cleaning, that’s very little time left for coding, studying ML, and conducting analyses. 

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Have been extremely curious about this for a while now, so I decided to create a poll. <br>&quot;As someone titled &#39;data scientist&#39; in 2019, I spend most of (60%+) my time:&quot; <br>(&quot;Other&quot;) also welcome, add it in the replies.</p>&mdash; Vicki Boykis (@vboykis) <a href="https://twitter.com/vboykis/status/1089920316644704256?ref_src=twsrc%5Etfw">January 28, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

In addition to “dirty data”, another major challenge is handling data with poor infrastructure. Imagine a busy highway with lots of potholes, toll booths, and traffic. Your job is to somehow navigate these treacherous conditions to supply data insights at the end. 

![Lots of data prep and little time for analysis image](https://imgur.com/6lbm6cr.jpeg)

Image from the <a href="http://insightextractor.com/2013/04/22/business-analytics-projects-are-like-an-iceberg/" target="blank">Insight Extractor - Blog</a>.

You may be faced with a database that isn’t optimized for your queries or unable to identify the source of truth in the data through its data lineage. You may wait days or weeks to get access to a database or be stuck with poor infrastructure because people are afraid to change it for fear of breaking everything! There may be no centralized data store, multiple dashboard tools used making it difficult to find information, and no repository for past data science work.

When I worked at Target HQ in 2012, employees would arrive to work early - often around 7am - in order to query the database at a time when few others were doing so. They hoped they’d get database results quicker. Yet, they’d still often wait several hours just to get results. The traffic jam was real! 

Even my friends at big tech startups have complained about the same problems with data infrastructure and technical debt. One friend had to come to work on Saturdays just to be able to query the data without extreme wait times.

Imagine wanting to investigate a hunch in the data and having to wait hours for it! Then, imagine you made a mistake in the SQL query, had to re-implement it and wait hours again! That’s practically waiting a whole day without even getting the data! 

On the job, if you notice poor infrastructure, speak up to your manager early on. Clearly document the problem, and try to incorporate a data engineering, infrastructure, or devops team to help resolve the issue! 

### 7. Data work can be profoundly unethical. Moral courage required 

This is the scariest of concerns for me. I have seen and heard of shady practices of collecting and analyzing private user data, from their private messages to their every interaction on the app. As a Data Scientist, you likely won’t have ethics training or a say in product decisions made regarding them. 

Uber is infamous for a <a href="https://www.theguardian.com/technology/2017/mar/03/uber-secret-program-greyball-resignation-ed-baker" target="_blank">secret internal tool called Greyball</a> built to evade law enforcement. The tool could help identify law enforcement officials in their respective cities and provide them a “fake” Uber experience to show riders but no one would pick them up. What if you were the Data Scientist tasked with predicting who’s a law enforcement official or modifying the core driver routing algorithm to evade these individuals? Would you do it?

The recommendations of an ML model can also be unethical. I once worked on an engagement in which ML predictions were provided to consumers. These predictions were created based on flawed practices in ML model training and there was very little signal in the data. Later, the paying customers complained about how poor the recommendations were, yet the company never publicly apologized. 

There may come a time when an ecommerce company asks you as a Data Scientist: “If we wanted to figure out if a customer is pregnant, even if she didn’t want us to know, can you do that?” These were the <a href="https://www.nytimes.com/2012/02/19/magazine/shopping-habits.html" target="_blank">exact words</a> spoken to one only a few years ago at Target! But what are the ethical implications of figuring this out? Would you as a consumer want you and your family to be marketed this way? What if the significant other doesn’t know if their partner is pregnant? What if they’re considering an abortion? At companies, especially smaller ones, these ethical concerns may not be taken into consideration! 

### Conclusion: Where Does This Leave Us?

I don’t want to discourage people from applying to data science jobs. They can be incredibly impactful towards the company’s mission. 

Rather, try to ask about these concerns in interview questions to help you evaluate your next role. If you’re on the job and already facing these issues, work with your manager or coworkers to try and resolve them asap to improve your job experience.

Let me know if you have any questions or feedback on this post: dan [@] dfrieds.com

Additional and somewhat similar articles to this are:

- <a href="https://towardsdatascience.com/why-so-many-data-scientists-are-leaving-their-jobs-a1f0329d7ea4" target="_blank">Here's why so many data scientists are leaving their jobs</a> 
- <a href="http://veekaybee.github.io/2019/02/13/data-science-is-different/" target="_blank">Data science is different now</a>
- <a href="https://medium.com/@datasocietyco/the-plight-of-the-frustrated-data-scientist-320428bde6e0" target="_blank">The plight of the Frustrated Data Scientist</a>

I’d like to thank <a href="https://www.naveed.dev/" target="_blank">Naveed Nadjmabadi</a>, <a href="http://dateworking.com/" target="_blank">Steve Dean</a>, Andrew Ju, Julia Xu, and <a href="http://emilydegrandpre.com" target="_blank">Em deGrandpré</a> for their advice on drafts.