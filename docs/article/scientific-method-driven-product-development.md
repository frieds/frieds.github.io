# A Recipe for Successful Software Product Development

In software product development, massive amounts of time and energy can be wasted on projects that don’t provide a significant impact for the company. This work may not be aligned with the company’s goals of increased revenue, decreased costs, and/or increased customer satisfaction.

You probably had this happen to you: someone asked you for a feature, you developed it, and this repeats to almost no end. You don't know the impact of your work. But, you keep on going. 

This post debunks how you should approach solving problems with software product development - a practice that I believe _every_ organization should follow.

Whether you’re a Software Developer, Product Manager, Data Analyst, or in _any_ role that deals with software development, this should be relevant to you!

Before I dive into the recipe for successful software product development, here are important principles to abide by in doing great work.

Principles for doing great software product development:

- Incorporate relevant stakeholders’ opinions, get their buy-in, and provide consistent updates to them. Ideally, this will help ensure your work can be impactful to the business.
- Document context, process, output, lessons learned, and recommended next steps.
- Make your work easily accessible for teammates.

### Outline: recipe for the software product development process:

1. Identify a problem and its significance
2. Brainstorm solutions to the problem
3. Pick one solution to implement
4. Identify a measurement plan to measure the effect of the solution implemented
5. Implement the solution and collect relevant data to measure change
6. Analyze the data and summarize insights as lessons learned
7. Optional: repeat steps 2-7 until you’re satisfied with a solution to the problem

### Explanation of each step

#### 1. Identify a problem and its significance

Identify the problem. Why is it a problem? How significant of a problem is it? A clear problem statement should answer these two questions in one sentence.

An example problem statement: on a 2-page signup flow for a software as a service (SaaS) app, users submit basic contact information on the first page, but then 80% of people drop off on the 2nd page, resulting in 800 lost signups per month - equivalent to $8,000 in monthly recurring revenue.

In this example, evidence of the problem was indicated through quantitative data. Alternatively, detailed qualitative user stories can indicate evidence of the problem. In collecting evidence, it’s important to show empathy for your users. Their pain point may not be one you have yourself using the product.

In finding evidence of problems in quantitative data, make sure you know the root source of the data, transformations applied to it, and the trustworthiness of it. As a Software Developer or Data Analyst, you will have to collect data from a database, customers, or another source, then clean it, analyze it, and summarize insights that can be easily understandable to others.

Most companies are reactive. They wait for feedback and let problems linger for long periods of time before fixing them. This is a mistake. Users will churn from your product and quickly spread negative word of mouth. Be proactive in getting user feedback and consistently examine important user data (ex - the signup funnel data in the example above). The more proactive you are, the quicker you’ll identify painful customer problems and fix them before they take a toll on your business.

#### 2. Brainstorm solutions to the problem

Brainstorm solutions to the problem. It doesn't need to be big sweeping change or something overly detailed. I'd recommend to keep it simple. Understand the skills and responsibilities of your teammates and how they can help implement a solution - be it with existing resources, a new tool, a code change or something else. 

#### 3. Pick one solution to implement

Every company has lots of problems. Generally, you want to identify the most significant problem that can be reasonably fixed in a short period of time. They’re the best “bang for the buck." In some companies like ones very focused on AI, they may want to solve the most challenging problems first. These could take months or years to solve but would give them a competitive advantage.

In the example above of drop-offs in the signup flow, a simple solution may be to add a few lines of copy. You could implement this as a treatment for an A/B test to try to prove the copy causes a decrease in drop-offs from the first page to the second.

#### 4. Create a measurement plan & goal(s) to measure the effect of the solution implemented

Create a plan to collect and measure data that helps you understand the effect of the solution being implemented.

In the signup funnel example, some relevant data to collect may be a cookie for each visitor along with their browser, platform, a flag for their treatment group, and a timestamp of each completed action.

The goal of the new copy could be to decrease signup drop-offs from 80% to 75%.

You should set up invariant metrics too. These are metrics that should stay the same or improve despite the change in the key goal metric. One ideal invariant metric is revenue. For example, the new copy on the second signup page could say “30-day money-back guarantee”. You may get a decrease in signup drop-offs from page one to page two, but after thirty days, you may find a larger percentage of customers demand and are granted a refund. Therefore, you need to calculate if the change is worth it to the business. 

Learn more about invariant metrics from this great [Harvard Business Review (HBR) article](https://hbr.org/2019/09/dont-let-metrics-undermine-your-business).

#### 5. Implement solution and collect relevant data to measure change

Collaborate with your team members to rock this!

#### 6. Analyze the data and summarize insights as lessons learned

Present clear insights on the data collected and whether your proposed solution to fix the problem was effective. Document steps 2-6 in detail. It’s great content to provide as evidence to the team on how product development is done, the direction of the business, and lessons learned.

Ideally, present insights in a dynamic environment such as a dashboard or a repeatable script. Translating your insights into a static document (i.e. PowerPoint) makes it immediately out of date with the current data.

If your proposed solution was ineffective, proceed to step 7.

#### 7. Optional: repeat steps 2-6 until you’re satisfied with a solution to the problem
Repetition of this process may yield a better solution to solve the problem!

<br>
<br>

**Thank you** to Ben Stern and Christine Song for their feedback on drafts of this post.