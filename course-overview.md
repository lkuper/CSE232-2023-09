---
title: "Course overview"
layout: single
classes: wide
---

Welcome!  This is an overview of the fall 2023 edition of CSE232 ("Distributed Systems"), a graduate course in the Computer Science and Engineering Department at the UC Santa Cruz Baskin School of Engineering.

## Course staff

### Instructor

<img src="{{ site.url }}{{ site.baseurl }}/assets/images/lindsey-kuper.jpg" alt="Lindsey Kuper" width="140" style="float: right; margin: 0px 15px 0px 15px; padding: 0px 15px 0px 15px;" />


Hi, I'm [Lindsey Kuper](https://users.soe.ucsc.edu/~lkuper/)!  (Feel free to call me by my first name.)

  - Email: for anything CSE232-related, send a DM on the course Zulip instead.  Otherwise: <lkuper@ucsc.edu>
  - Office location: Engineering 2, Room 349B
  - Office hours: By appointment (DM me on Zulip anytime!)
  - Research areas: programming languages, distributed systems, software verification, concurrency (check out the [Languages, Systems, and Data Lab](https://lsd.ucsc.edu/) website for more information)
  - Pronouns: she/her/hers
  
### Teaching assistant

<img src="http://placekitten.com/140/200" alt="Jonathan Castello" width="140" style="float: right; margin: 0px 15px 0px 15px; padding: 0px 15px 0px 15px;" />
  
**Jonathan Castello**

  - Email: <jcaste14@ucsc.edu>
  
<br style="clear: both;" />

## A few essential details about the course

  - 5-unit graduate seminar course (in this context, "seminar" means a course where we discuss assigned readings and everyone participates actively in the discussion)
  - Class meets in person Mondays, Wednesdays, and Fridays, 4:00-5:05pm Pacific time, in [Social Sciences 2, Room 75](lsd-ucsc.github.io/content/lsd-seminar/)
  - Course GitHub repo (public; for class discussion summaries): <https://github.com/lkuper/CSE232-2023-09/>
  - Canvas (for reading responses and grades): <https://canvas.ucsc.edu/courses/65302>
  - Zulip (private; for announcements, live chat during lectures, Q&A, communicating with course staff, and socializing): <https://ucsc-cse232.zulipchat.com> (enrolled students will receive an invitation link)
  - Course web page (you're soaking in it): <https://decomposition.al/CSE232-2023-09/> (URLs are case-sensitive after the domain name, so be sure to capitalize "CSE"
  
## What's this course about?

The field of _distributed systems_ studies the design, implementation, and behavior of systems that involve independent components that communicate by passing messages to one another over a network. In addition to the usual challenges of _concurrency_, distributed systems may be characterized by unbounded _latency_ between components and independent _failure_ of components, making them challenging to reason about and debug.

Some of the foundational distributed systems concepts we'll explore in this course are:

  * **Time and asynchrony.**  No two computers can reason about each others' perception of time.  What does it mean to talk about time when we don't share a clock?
  * **Fault tolerance and replication.**  Given that computers crash and messages get lost, how can we write protocols and algorithms that have adequate redundancy to tolerate failure?  Maybe if I think a computer will crash, it's a good idea to run the same computation on more than one computer!  Maybe if I think messages will be lost, I should send the same message more than once!
  * **Consistency and consensus.**  Is our system storing the right data and providing the right responses?  I might have two "replicas" that aren't actually replicas!  If replicas disagree, how do we know which one is right?  Or is it better to try to ensure that they agree in the first place?
  
The [schedule](schedule.md) has more details!

### In this course, you will:

  - Become familiar with foundational distributed systems concepts.
  - Get a sense of the history of the field of distributed systems.
  - Improve your technical reading, writing, speaking, and listening skills.
  
All of these skills will serve you well in your future career, whether in industry or in academia.
  
## What will this course be like?

CSE232 will be a *combination lecture and discussion* course.  We will be reading and discussing papers from the distributed systems research literature, interleaved with lectures to give you the necessary background to get the most out of the papers. We'll alternate between lecture days and discussion days.  On discussion days, you'll come to class having read and responded to a reading assignment, and you'll spend 30 minutes of class in a small group of (at most) 7-8 students, discussing specific questions about the reading.

In these small-group discussions, each student will play a designated role of *ambassador*, *manager*, or *scribe* (discussed in further detail below).  Each student will play each role several times throughout the term.

Some people will like this format, while others won't like it at all -- so give some thought to whether it is what you want before you commit to taking this course.  (In particular, if you want to take a course where one student gives a slide presentation about a paper while other students listen silently, that's *not* what this course will be.)

On lecture days, the material we'll cover in CSE232 will be similar to my undergrad distributed systems course, CSE138, although the pace will be faster.  Some of you may find my [CSE138 lecture videos](https://decomposition.al/CSE138-2021-03/schedule.html) to be a helpful resource.

On discussion days, we'll discuss mostly older papers, primarily from the 80s and 90s, because a lot of our focus will be on the foundations of the field and the historical development of distributed systems ideas.  In fact, the most recent of the papers on the [schedule](schedule.html) was published in 2007.  If you're mostly interested in reading shiny new distributed systems papers instead of older ones, this course is probably not for you.

This course will _not_ have a required programming component.  If you were hoping for a course with a large distributed programming project, I recommend taking or auditing CSE138 instead of this course.

## Reading and responding to research papers

We will spend half our time in this course **reading, responding to, and discussing research papers**.  Reading research papers is a skill that requires a great deal of practice.  In this class, you will work on developing that skill.  You will need to finish each reading assignment in advance of the day we discuss it in class.  In fact, you will need to turn in a reading response by 11:59:59pm Pacific time on the day _before_ the day we discuss it in class.

### Some advice on how to read papers

Attempting to plow right through a paper from beginning to end is usually not the most productive approach.  Here's some great [advice from Manuel Blum on how to read and study](http://www.cs.cmu.edu/~mblum/research/pdf/grad.html):

> Books are not scrolls.  
> Scrolls must be read like the Torah from one end to the other.  
> Books are random access -- a great innovation over scrolls.  
> Make use of this innovation! Do NOT feel obliged to read a book from beginning to end.  
> Permit yourself to open a book and start reading from anywhere.  
> In the case of mathematics or physics or anything especially hard, try to find something  
> anything that you can understand.  
> Read what you can.  
> Write in the margins. (You know how useful that can be.)  
> Next time you come back to that book, you'll be able to read more.  
> You can gradually learn extraordinarily hard things this way.

You may also be interested in time-tested paper-reading advice [from Michael Mitzenmacher](https://www.eecs.harvard.edu/~michaelm/postscripts/ReadPaper.pdf) and [from S. Keshav](https://svr-sk818-web.cl.cam.ac.uk/keshav/wiki/index.php/HTRAP).

### What to include in your reading response

For each paper we read, you will submit a short reading response.  The reading response process is designed to help you develop the skill of **asking good questions** about the readings.  You should include the following in your reading response:

  * **Paper Summary**: Using only your own words, write an overview of the paper that can serve as an explanation of the paper for your classmates.  Your summary should answer the following questions: What problem does the paper address (1-2 sentences)?  What are the paper's key insights (1-2 sentences)?  What are the paper's key scientific and technical contributions (2-3 sentences)? What are its shortcomings or flaws (up to 3 sentences)?  (These guidelines for summarizing a paper are taken from the [ASPLOS 2021](https://asplos-conference.org/2021/) review process, with thanks to [Emery Berger](https://emeryberger.com/).)
  * **Discussion questions**: Please suggest 1-2 questions about the reading for our in-class discussion.  These must be **questions whose answers do not appear verbatim in the paper**.  Instead, try to go deeper.  Keep in mind that you may need **several sentences** just to provide sufficient context for a question.  For example, if a question has to do with how the paper's topic relates to other work you were previously familiar with, you'll need to summarize the relevant part of that other work as part of the question.  Furthermore, your questions must be _unique_ (after you submit, you'll get to see other people's submitted questions).

(By the way, the summary I'm asking you to write does _not_, by itself, comprise a _review_ of the paper, like those you would write if you were serving on a conference program committee.  A review is much longer and more detailed, and would, among other things, make a case for acceptance or rejection of the paper.)

### How to write discussion questions

A good discussion question should be specific to the paper being discussed.  (If the question would work just as well for some other paper, that's a sign that it's not a great discussion question.)

It should offer enough detail and context to be understandable by your classmates -- that is, people who have read the paper but may not have internalized every detail -- and who might not have any background on the topic aside from what has been discussed in this course.

Moreover, you should aim for discussion questions that will **start a lively and enlightening conversation**.

Here are examples of *good* discussion questions from students who've previously taken this course (but don't reuse these questions for the same papers; come up with your own!).  In each case, the question begins with a sentence or two of contextual information from the paper and then follows that up with a question.

  * "In Figure 1 of the paper, events `e_12` and `e_13` are message sends, while `e_21` and `e_22` are message receives. Notice that from the perspective of `P_2`, the messages were received (and possibly delivered) in an opposite order than they were sent. While in class we talked about how to implement FIFO delivery and causal delivery, are there scenarios where we might want to allow messages to be delivered out of order like this?" (for ["Detecting causal relationships in distributed computations: in search of the holy grail"](readings/holy-grail.pdf); discussion question contributed by Reese Levine)

  * "Chain replication improves on primary-backup replication by splitting the read and write responsibility amongst two nodes. Would this be sufficient for an unpredictable workload? Under what circumstances would you choose primary-backup replication over CR?" (for ["Chain Replication for Supporting High Throughput and Availability"](readings/chain-replication.pdf); discussion question contributed by Meghna Burli)
  
  * "The paper mentions at the end of section 5.2 that changing masters in networks with poor connectivity is undesirable and boosting sequence numbers with the “right” frequency should help avoid this. How exactly does a master prevent the cycle of changes of masters, using boosting?" (for ["Paxos Made Live: An Engineering Perspective"](readings/paxos-made-live.pdf); discussion question contributed by Ramtin Roshanmanesh)
  
Here are examples of how *not* to write a discussion question:

  * "How can the task of maintaining, implementing and designing fault-tolerant distributed systems be simplified?"  (for ["Fundamentals of Fault-Tolerant Distributed Computing in Asynchronous Environments"](readings/fault-tolerance.pdf))  This question is much too broadly scoped and not specific enough to the paper under discussion.
  
  * "How to deal with the scalability issue of vector time?"  (for ["Detecting Causal Relationships in Distributed Computations: In Search of the Holy Grail"](readings/holy-grail.pdf))  There's the start of a good question here, but more context is needed.  The question writer should explain what "scalability issue" they mean, and if possible, give a pointer to a particular section of the paper under discussion.

### Reading response submission logistics

Reading responses are due **at 11:59:59pm Pacific time on the day before we discuss the reading in class**.  The reason for this relatively early deadline is to give me time to look at the responses before class so that I can structure the in-class discussion based on them.  Don't be surprised if you see some of your questions used in the in-class discussions!

You will submit your reading response [on Canvas](https://canvas.ucsc.edu/courses/65302), in the discussion forums set up for each paper.  Once you submit, you'll get to see other people's submissions.  After submitting, take a look at the other submissions to make sure that your questions aren't a repeat (or very close to a repeat) of any already-submitted questions.  In that case, you should edit your questions to make them clearly distinct from the previously-submitted ones.  _It is to your advantage to turn in your reading response relatively early_, because the earlier you turn it in, the less likely it is that your questions will be a repeat of any previously-submitted questions!

## In-class discussion process

On discussion days, we'll use a structured in-class discussion process.  The process we will use is (loosely) inspired by one used by [Matthew Ahrens](https://www.eecs.tufts.edu/~mahrens/), [Kathleen Fisher](http://www.cs.tufts.edu/~kfisher/Kathleen_Fisher/Home.html), and [Norman Ramsey](https://www.cs.tufts.edu/~nr/) in courses taught at Tufts University, and the below description borrows heavily from [their](https://www.cs.tufts.edu/comp/150PLD/Consensus.pdf) [documentation](https://www.cs.tufts.edu/comp/150PLD/ic00-1.html), with their permission.

### Small-group discussion (30 minutes)

At the start of each discussion day, after at most 5 minutes for announcements, the class will split into small groups of (at most) 7-8 students for 30 minutes.

In your small group, three members of the group must take on the following **roles**, and carry out this role in addition to actively participating in the conversation.  Each student in the class should serve in each of the roles **two or more times** during the term, and we'll track roles in a spreadsheet.

  * **Scribe**: The role of the scribe is to take notes during the conversation, while participating in the conversation themselves.  After class, all the scribes will meet and contribute to a formal write-up of the class discussion on the course's public GitHub wiki.
  * **Manager**: The role of the manager is to keep track of time and make sure that all of the discussion questions get touched upon and that everyone has had a chance to speak.  Afterward, they will be responsible for recording everyone's role on a shared spreadsheet.
  * **Ambassador**: The role of the ambassador is to represent their small group in the large-group discussion afterward.  Ambassadors will also be the first ones to answer follow-up questions from the rest of the class, or to pose questions to the rest of the class that would be helpful to discuss.
  
Other members of the group should all participate in the discussion, but don't need to play a specific role.
  
The small-group discussion will use the following process:

1. Each member of the group should **introduce themselves**.
2. The group should **assign roles** to three people.
3. The group should **discuss answers to the provided questions about the reading assignment**.  On each discussion day, I'll provide a short list of discussion questions, many of which will be drawn from the reading responses that you and your classmates submitted previously.  During the discussion phase, feel free to work together in a shared document and use any resources you like.  This is a "brainstorming" phase.  Don't stop with a single answer; look at things from all angles.
4. The group should try to **reach consensus on the most satisfying answers**.  Perhaps the group will agree on answers that satisfy everyone.  Perhaps there will be significant dissent -- maybe even no majority view.
5. The group should **prepare to report verbally to the class as a whole**.  The ambassador's report should cover the following points:
   * The preferred answers according to the consensus reached by your group.
   * The _reasons_ that you prefer these answers.
   * Any significant minority views.
   * A few words about answers that your group considered but ultimately rejected.
	
### Large-group discussion (25 minutes)

After 30 minutes, small groups will conclude, and the entire group will reconvene for 25 minutes.  At this point, ambassadors from individual groups will present their groups' conclusions.  **Ambassadors should sit close to the front** during this part of class, and during the large-group discussion, **ambassadors speak first**, for a couple of minutes each.  Once all ambassadors have had a turn to speak, if there's time remaining, we'll open the floor to the whole class.

In the large-group discussion, we'll discuss and evaluate the groups' conclusions and try to forge a coherent consensus view that the whole class can agree on, but also be alert for gaps, inconsistencies, and incoherence.  When possible, I'll compare the conclusions reached by the class with my interpretation of the consensus position of the body of researchers interested in distributed systems.

### Wrap-up (5 minutes)

During the last five minutes of class:

  * **Ambassadors** will gather with Lindsey and discuss how they think the day went, how they think the pacing went, what they are looking forward to, any concerns they might have about the class, and so on.
  * **Managers** will update the shared _role spreadsheet_ (link to be distributed privately) to list the role that each member of their small group played.  They will then create an [issue on the course GitHub repository](https://github.com/lkuper/CSE232-2023-09/issues) for Lindsey to follow up on the scribes' class discussion summary once it is complete, @-mention all the scribes in the issue description, and assign the issue to Lindsey (@lkuper).  (There should be a single issue created per paper discussion, so only one manager needs to create it, but the other managers should make sure that the scribe from their group gets an @-mention.)
  * **Scribes** will gather to start writing a _discussion summary_ on the [course GitHub wiki](https://github.com/lkuper/CSE232-2023-09/wiki), to be finished by at most a week from the day the in-class discussion took place.  You may update the wiki either through the web interface, or by [cloning the wiki locally](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/adding-or-editing-wiki-pages#adding-or-editing-wiki-pages-locally).  I recommend doing the latter, *especially* if you're not yet particularly fluent with git, since it's a good idea to become comfortable with it.
  
## Discussion summaries

The discussion summary on the course GitHub wiki will include (1) a brief overview of the paper (which can draw from the paper summaries in reading responses previously written by the scribes, but should also incorporate any updated understanding gained from the in-class discussion), and (2) summaries of the in-class discussions about each discussion question.  The purpose of the discussion summary is to serve as a sort of annotated bibliography of the papers we read, for your future use as well as the use of anyone else in the world who might be interested in these papers (the wiki is public, after all).  Think of the discussion summary as an exercise in collaborative note-taking.  You may come back to these papers later on in your career, so when you are in the scribe role, it's a gift to your future self (as well as to anyone else reading the wiki!) to try to be as thorough and detailed as you can when creating the discussion summary.

After managers create a GitHub issue for use by the scribes, the scribes can use the issue throughout the week that they work on the discussion summary as a place to keep track of what needs to be done.  They can comment on the issue with an @-mention of me (@lkuper) to let me know when a draft of the discussion summary is ready for me to look at.  It's fine to ask for feedback from me before the deadline, and I may use the GitHub issue as a place to comment and give feedback on the in-progress discussion summaries.
  
## Grading

Your grade in this course will be based 50% on your participation in the course and 50% on your reading responses.  Credit for participation can be earned primarily by fulfilling your role on discussion days and completing the follow-up tasks for your role.  Credit for reading responses can be earned by submitting thoughtful, well-written paper summaries and discussion questions.

Needless to say, the above grading approach assumes no violations of academic integrity.

## Academic integrity

**Everything you write for this course must be your own original work.**  It is a very important part of your job as a scholar to understand what counts as plagiarism, and make sure you avoid it.

**Properly attribute any work that you use.**  If you use someone else's words, you must _quote_ and _cite_ them.  The only time you can leave out the citation is if it's obvious from context.  For example, if you're turning in a reading response for a given paper, you don't have to add a citation to the paper you're responding to.  However, you definitely do have to _quote_ any text from the paper that you use.

Because some students find plagiarism hard to identify, here is a real-world example of it from a previous iteration of this class.

Waldo et al.'s ["A Note on Distributed Computing"](readings/note-distributed-computing.pdf) contains the following sentence:

> In fact, the difference in latency between local and remote calls, because it is so obvious, has been the only difference most see between the two, and has tended to mask the more irreconcilable differences.

A student turned in a reading response for the Waldo et al. paper that said:

> The difference in latency between local and distributed object invocations has tended to mask the more incompatible differences.

Unfortunately, this is plagiarism.  It takes the above sentence from the original paper, removes the middle chunk of the sentence, replaces the word "irreconcilable" with "incompatible", and calls it a day.

What should the student have done here instead?  The right thing to do is to think about what the idea from the paper is that you want to convey, and then convey that idea in your own words while acknowledging that it comes from the paper.  For example, one might write:

> The paper says that people think too much about latency and don't pay enough attention to bigger differences between local and distributed programming.

Notice that this version is very casually written.  **That's fine!  In fact, it's great.**  Here's a more formal version:

> The paper argues that focusing exclusively on latency leads to an unfortunate lack of emphasis on the more "irreconcilable differences" between local and distributed computing.

But both sentences do what we're looking for in this course: they credit the paper with an idea and paraphrase that idea.  The second sentence uses a recognizable phrase, "irreconcilable differences", from the paper, but quotes it -- this is fine to do.

Many of the papers we're reading are classics, and much has been written and said about them.  It's absolutely fine to consult existing videos, blogs, etc. to check your understanding.  However, using other people's words without appropriately citing and quoting them is unacceptable.  **I would always much rather have you submit your own original writing, even if it is extremely casual and unpolished.**

If I see that the writing you do for this course contains material that is copied from a source without appropriate citation and quotation, *at a minimum*, you will get no credit for the assignment in question, and you risk further penalties, such as failing the course.

### Policy on the use of LLM-based tools like ChatGPT

In the writing you do for this course, you are *completely welcome* to use tools based on large language models (LLMs), such as ChatGPT.  Such tools can be incredibly useful, and it may be worth your while to learn how to use them.  However, it's important to be aware of the limits of LLM-based tools, and of how to use and cite them properly.  In particular, here's what you need to know for this class:

  - You must acknowledge your use of LLM-based tools.  **If you use LLM-based tools for any of the work you submit for this class, include a paragraph at the end of the submitted work, explaining what tool you used, what you used it for, and what prompts you used to get the results. Failure to do so is academic misconduct.**
  - If you provide low-effort prompts, you will get low-quality results. You will need to refine your prompts in order to get good outcomes. This will take work.
  - Don't trust anything that an LLM-based tool says.  It will often [make up fake citations or hallucinate plausible-but-wrong answers to questions](/blog/2023/01/23/an-underwhelming-conversation-with-chatgpt/).  If it gives you a number or fact, assume it is wrong unless you either know the answer or can check with another source. You will be responsible for any errors or omissions provided by the tool. It works best for topics you understand.
  
(This policy is based on the article ["Why All Our Classes Suddenly Became AI Classes"](https://hbsp.harvard.edu/inspiring-minds/why-all-our-classes-suddenly-became-ai-classes) by Ethan Mollick and Lilach Mollick.)

All that said, I will now make a case for why you might *not* want to use LLM-based tools in this course.

If you're enrolled in this (elective, graduate) course, it's presumably because you want to deeply understand the subject matter.  The knowledge and experiences you've gained in your life so far will inform that understanding.  By building on those experiences and putting them together with what you glean from this course, you will probably think of things that I've never thought of before.  You may even think of things that *no one* has thought of before!  I am excited to see those ideas emerge in the writing you do for this class.  However, as [Rob Ricci](https://ricci.io/) puts it, ["I can't tell you exactly what this should look like, because the point is that I want to see things that are different from what everyone else is writing."](https://recurse.social/@ricci@discuss.systems/111103870283618525)

LLM-based tools do not "understand"; rather, they produce statistically likely responses to prompts.  If you go to the effort of dumping the text of an assigned reading into ChatGPT and prompting it to produce a paper summary or a discussion question for this course, it will produce -- with great confidence, and in impeccable English prose -- ["a thoroughly mediocre response that is indistinguishable from all the other text it has ingested on the topic"](https://discuss.systems/@ricci/111103870175372635), to quote Rob again.

For instance, I tried using ChatGPT to produce discussion questions for Waldo et al.'s ["A Note on Distributed Computing"](readings/note-distributed-computing.pdf).  I provided the entire text of the paper, then prompted ChatGPT as follows (quoting from my own writing up above):

> Now, please suggest 1-2 questions about the reading that would be good for an in-class discussion in a graduate-level distributed systems course. These must be questions whose answers do not appear verbatim in the paper. Instead, try to go deeper. Keep in mind that you may need several sentences just to provide sufficient context for a question.

Here's the result:

> 1. In the article, the author argues against attempting to merge the computational models of local and distributed computing, emphasizing their irreconcilable differences. Given this perspective, discuss the practical challenges and potential benefits of designing software systems that acknowledge and embrace these differences. Can you provide examples of real-world applications where such an approach might be advantageous, and how would you go about designing interfaces for objects meant for remote access?
> 
> 2. The author highlights the importance of maintaining visibility of the differences between local and remote objects throughout the design and implementation of distributed applications. In your view, how can software engineers strike a balance between abstracting these differences to simplify development and keeping them visible to ensure robustness and reliability? Can you propose strategies or best practices for achieving this balance in the context of modern distributed systems?

The ChatGPT-produced prose truly does accurately summarize some key concepts from the paper.  However, aside from the fact that the resounding hollowness of the ChatGPT-produced prose has sucked away all of my zest for life, these questions are too vague and broadly scoped to be likely to lead to a focused, illuminating, and lively discussion in class.  (Also, in true ChatGPT fashion, its output contains information that is *plausible but false*: it refers to "the author", when in fact the article in question has four authors.)

So, please understand that while you are welcome to use LLM-based tools in this course, you should be aware of their limitations.

(Of course, I haven't even begun to address the topic of [the myriad environmental, social, and ethical problems involved in the training, deployment, and use of LLM-based tools](https://dl.acm.org/doi/10.1145/3442188.3445922), but that's a topic for another course.)
  
## A note on accessibility

If you have a disability and you require accommodations to achieve equal access in this course, please submit your Accommodation Authorization Letter from the [Disability Resource Center (DRC)](https://drc.ucsc.edu/index.html) to me via the Accommodate system, preferably within the first two weeks of the quarter.  I am eager to discuss ways we can ensure your full participation in the course.

I encourage all students who may benefit from learning more about DRC services to [contact the DRC](https://drc.ucsc.edu/about/contact-us/index.html).
